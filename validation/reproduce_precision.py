#!/usr/bin/env python3
"""Precision of the extractor's API-shaped set against a published OpenAPI specification.

Reproduces the precision figures in Section 6.2 of the manuscript.

Inputs, both recorded with digests in VALIDATION.json:
  openapi.json              Jellyfin API 12.1.0 specification (ground truth)
  recon/endpoints-api.txt   the extractor's API-shaped output

Outputs: precision over the set as emitted, the decomposition that sets absolute
third-party URLs aside, the client-router false-positive class, and specification
coverage. Prints every denominator rather than a single ratio.

Usage:  python reproduce_precision.py [run-dir] [--spec PATH] [--strip-prefix P[,P...]]

        run-dir defaults to recon/ (the original classifier, the source of every
        figure in the manuscript). Pass recon-v2/ for the repaired classifier.

        --spec selects the ground-truth specification; defaults to openapi.json here.
        --strip-prefix removes one leading prefix from EXTRACTED paths before the join,
        for applications whose spec declares bare paths while the client carries a base.
        Zulip needs --strip-prefix /json,/api/v1 ; Jellyfin needs none.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Client-side router prefixes in this application. NOTE: this class was identified
# post hoc by inspecting the misses, not defined in advance. The manuscript reports
# the resulting figure as a decomposition, never as an independent result.
ROUTER = re.compile(
    r'^/(dashboard|login|profile|search|home|movies|tv|music|livetv|mypreferences'
    r'|queue|video|details|list|edititemmetadata|addserver|selectserver|wizard'
    r'|installedplugins|configurationpage)(/|$)',
    re.I,
)


TIERS = ('request-construction', 'structural', 'none', 'router-definition')


def tier_table(run, spec_set, strip, normalise, strip_base):
    """Row count and precision per evidence tier, assigned by classifier_rule.py itself.

    Tiers are derived from the evidence fields recon.json records for every endpoint —
    clients, methods, request_parts, context — so the same rule can be applied to any
    run. The table is computed over every relative-path record in the extraction, not
    over the subset a particular rule admitted, which is why the two runs of one
    application yield the same table: they share an extraction and differ only in which
    rows they admit.

    Spread is defined as request-construction precision minus absent-evidence precision.
    """
    import importlib.util
    rule_path = Path(__file__).resolve().parent / 'classifier_rule.py'
    spec_m = importlib.util.spec_from_file_location('classifier_rule', rule_path)
    rule = importlib.util.module_from_spec(spec_m)
    spec_m.loader.exec_module(rule)

    data = json.loads((run / 'recon.json').read_text(encoding='utf-8'))
    rows = [e for e in data['endpoints'] if str(e.get('value', '')).startswith('/')]
    out = {}
    for t in TIERS:
        g = [e for e in rows
             if rule.classify_endpoint(e.get('value'), e.get('clients') or [],
                                       e.get('methods') or [], e.get('request_parts') or [],
                                       e.get('context') or '')[1] == t]
        hit = [e for e in g
               if normalise(strip_base(str(e['value']), strip)) in spec_set]
        out[t] = (len(g), (len(hit) / len(g)) if g else None)
    return out


def strip_base(path: str, prefixes) -> str:
    """Remove at most one leading base prefix. Reported separately, never silent."""
    for p in prefixes:
        if path == p:
            return '/'
        if path.startswith(p + '/'):
            return path[len(p):]
    return path


def normalise(path: str) -> str:
    """Collapse parameter placeholders so spec and extracted forms are comparable.

    OpenAPI writes /Items/{itemId}; React Router writes /dashboard/users/:userId.
    Both become /items/{}.
    """
    # Collapse template interpolation BEFORE brace collapsing. Without the ${...}
    # case a stray '$' survives -- /albums/${encodeURIComponent(id)} normalises to
    # /albums/${} and never joins /albums/{}. That defect understated recall on every
    # client that builds paths by interpolation, and left Jellyfin unaffected because
    # its bundles carry literal {itemId} braces with no dollar sign.
    p = re.sub(r'\$\{[^}]*\}', '{}', str(path).strip())
    p = re.sub(r'\{[^}]*\}', '{}', p)
    p = re.sub(r':[A-Za-z_]\w*', '{}', p)
    p = p.split('?')[0].split('#')[0]
    return '/' + p.strip('/').lower()


def main() -> int:
    argv = sys.argv[1:]
    spec_arg, strip = None, []
    pos = []
    i = 0
    while i < len(argv):
        if argv[i] == '--spec':
            spec_arg = argv[i + 1]; i += 2
        elif argv[i] == '--strip-prefix':
            strip = [x for x in argv[i + 1].split(',') if x]; i += 2
        else:
            pos.append(argv[i]); i += 1
    run = Path(pos[0]) if pos else HERE / 'recon'
    if not run.is_absolute():
        run = (HERE / run) if not run.exists() else run
    spec_file = Path(spec_arg) if spec_arg else HERE / 'openapi.json'
    if not spec_file.is_absolute() and not spec_file.exists():
        spec_file = HERE / spec_file
    ext_file = run / 'endpoints-api.txt'
    print(f'run directory : {run.name}/')
    print(f'specification : {spec_file.name}')
    if strip:
        print(f'prefix strip  : {", ".join(strip)}  (applied to EXTRACTED paths only)')
    for f in (spec_file, ext_file):
        if not f.exists():
            print(f'missing input: {f}', file=sys.stderr)
            return 2

    spec = json.loads(spec_file.read_text(encoding='utf-8'))
    declared = sorted(spec['paths'])
    spec_set = {normalise(p) for p in declared}

    rows = [l.strip() for l in ext_file.read_text(encoding='utf-8').splitlines() if l.strip()]
    relative = [r for r in rows if r.startswith('/')]
    absolute = [r for r in rows if not r.startswith('/')]

    stripped = sum(1 for r in relative if strip_base(r, strip) != r) if strip else 0
    pairs = [(r, normalise(strip_base(r, strip))) for r in relative]
    hits = [r for r, n in pairs if n in spec_set]
    misses = [r for r, n in pairs if n not in spec_set]
    router_fp = [m for m in misses if ROUTER.match(m)]
    other_fp = [m for m in misses if not ROUTER.match(m)]
    distinct_hits = {n for _, n in pairs if n in spec_set}

    print(f'declared paths in specification        : {len(declared)}')
    print(f'  distinct after normalisation         : {len(spec_set)}')
    print(f'API-shaped rows emitted by extractor   : {len(rows)}')
    print(f'  relative paths                       : {len(relative)}')
    print(f'  absolute third-party URLs            : {len(absolute)}  (all false positives)')
    print()
    if strip:
        print(f'rows whose prefix was stripped         : {stripped}/{len(relative)}')
    print(f'matching rows                          : {len(hits)}')
    print(f'  distinct paths they resolve to       : {len(distinct_hits)}'
          '   <- precision counts rows, recall counts paths')
    print()
    print(f'PRECISION, set as emitted              : {len(hits)}/{len(rows)} = '
          f'{len(hits)/len(rows):.1%}   <- headline')
    print(f'PRECISION, absolute URLs set aside     : {len(hits)}/{len(relative)} = '
          f'{len(hits)/len(relative):.1%}   (decomposition)')
    den = len(relative) - len(router_fp)
    print(f'PRECISION, router class also set aside : {len(hits)}/{den} = '
          f'{len(hits)/den:.1%}   (post-hoc class; see manuscript)')
    print()
    print(f'false positives, client-router class   : {len(router_fp)}')
    print(f'false positives, unexplained           : {len(other_fp)}  {other_fp}')
    print()
    print(f'SPECIFICATION COVERAGE (not recall)    : {len(distinct_hits)}/{len(spec_set)} = '
          f'{len(distinct_hits)/len(spec_set):.1%}')
    print('  a client is not obliged to invoke every route a server offers, so this')
    print('  ratio measures coverage of the published interface, not extractor accuracy.')

    print()
    print('EVIDENCE TIERS, assigned by classifier_rule.classify_endpoint over every')
    print('relative-path record in this extraction:')
    tt = tier_table(run, spec_set, strip, normalise, strip_base)
    for t in TIERS:
        n, pr = tt[t]
        print(f'  {t:22s} rows={n:5d}  precision=' + (f'{pr:7.1%}' if pr is not None else '      --'))
    rc, nn = tt['request-construction'][1], tt['none'][1]
    if rc is None or nn is None:
        print('  SPREAD (request-construction - none): not computable, a tier is empty')
    else:
        print(f'  SPREAD (request-construction - none): {(rc - nn) * 100:+.1f} pts')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

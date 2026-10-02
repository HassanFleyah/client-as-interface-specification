#!/usr/bin/env python3
"""Presence of specification paths in the client, and extractor recall over them.

Reproduces the two findings in Section 6.2 that separate extraction from
classification:

  1. how much of a published interface appears verbatim in the distributed client
     (the structural premise of Section 3.1, measured);
  2. how much of what is present the extractor reports at all, versus how much it
     admits to its API-shaped set.

This script needs the client bundles, which are not redistributed here (the Jellyfin
client is GPL-licensed and the set is 28 MB). Fetch them first from the version-pinned
URL; VALIDATION.json records the expected content digest of the extracted files:

    curl -L -o jellyfin_12.1.tar.gz \\
      https://repo.jellyfin.org/files/server/portable/stable/v12.1/any/jellyfin_12.1.tar.gz
    # Do NOT verify the archive by digest: the server re-compresses it, so the same
    # pinned URL yields different archive hashes. Verify the extracted client instead:
    #   expected content digest 3b636f45363b8561becb0ddf09303ed117210e4ebef89bce235c0e53a0249436
    #   over 986 .js files, 26,274,040 bytes (see VALIDATION.json for the recipe).
    mkdir -p js-loot/js
    tar -xzf jellyfin_12.1.tar.gz -C js-loot/js --strip-components=2 \\
      --wildcards 'jellyfin/jellyfin-web/*.js'

Usage:  python reproduce_recall.py [path-to-js-dir]
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def normalise(path: str) -> str:
    p = re.sub(r'\{[^}]*\}', '{}', str(path).strip())
    p = re.sub(r':[A-Za-z_]\w*', '{}', p)
    p = p.split('?')[0].split('#')[0]
    return '/' + p.strip('/').lower()


def load_rows(path: Path) -> set:
    if not path.exists():
        return set()
    return {
        normalise(l.strip())
        for l in path.read_text(encoding='utf-8', errors='replace').splitlines()
        if l.strip().startswith('/')
    }


def main() -> int:
    js_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'js-loot' / 'js'
    spec_file = HERE / 'openapi.json'
    if not spec_file.exists():
        print(f'missing input: {spec_file}', file=sys.stderr)
        return 2
    # rglob, not glob: 12 of the 986 bundles sit in subdirectories, and the extractor
    # walks recursively. A non-recursive glob finds 974 and understates the corpus.
    bundles = sorted(js_dir.rglob('*.js'))
    if not bundles:
        print(f'no .js files under {js_dir}', file=sys.stderr)
        print('fetch the client archive first; see the header of this file.', file=sys.stderr)
        return 2

    spec = json.loads(spec_file.read_text(encoding='utf-8'))
    declared = sorted(spec['paths'])

    # One concatenated blob: a verbatim substring test, deliberately the crudest
    # possible presence check, so that "present" cannot be an artefact of parsing.
    blob = '\n'.join(
        f.read_text(encoding='utf-8', errors='ignore') for f in bundles
    )
    present = [p for p in declared if p in blob]
    present_norm = {normalise(p) for p in present}

    api_shaped = load_rows(HERE / 'recon' / 'endpoints-api.txt')
    all_output = load_rows(HERE / 'recon' / 'endpoints.txt')

    found_any = present_norm & all_output
    found_api = present_norm & api_shaped
    missed = sorted(present_norm - all_output)

    print(f'bundles read                                  : {len(bundles)}'
          f'  ({len(blob):,} chars)')
    print(f'declared paths in specification               : {len(declared)}')
    print()
    print(f'PRESENT VERBATIM in the client                : {len(present)}/{len(declared)} = '
          f'{len(present)/len(declared):.1%}')
    print('  this is the structural premise of Section 3.1, measured')
    print(f'  distinct after normalisation                : {len(present_norm)}')
    print()
    print(f'RECALL over present paths, any output row     : {len(found_any)}/{len(present_norm)} = '
          f'{len(found_any)/len(present_norm):.1%}   <- extraction')
    print(f'RECALL over present paths, API-shaped set     : {len(found_api)}/{len(present_norm)} = '
          f'{len(found_api)/len(present_norm):.1%}   <- classification')
    print()
    print('The gap between those two lines is the finding: the extractor recovers')
    print('nearly everything present, then its own heuristic discards most of it.')
    print()
    print(f'present in client but never reported at all    : {len(missed)}  {missed}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

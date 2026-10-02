# Zulip Server 12.3 — measurement record

Measured 2026-10-01 against the criterion in `PRE-REGISTRATION.md`, fixed before measurement.
Reported per application; not pooled with Jellyfin or Immich.

## Inputs

| Input | Value |
|---|---|
| Release tag | `12.3`, published 2026-09-21 |
| Specification | `zulip.yaml` at the tag — sha256 `15c17a2d53da572191f064722102d819c200c63a5ee7d0fe20da3dcdfd74cec5` |
| Specification as JSON | `zulip-openapi.json` — sha256 `5fa7a3d0a9ffa8604fee85632a0b1928bd48de077029f4329c766e19063a8557`, converted once |
| Declared paths | 115 (114 distinct after placeholder normalisation) |
| Client bundles | 64 files, 11,321,957 bytes, from `*/prod-static/serve/webpack-bundles/*.js` |
| Bundle set content digest | `635e3ed4ba0b037a65639c5c16895cc0870c8e6bd306bcb5e662c45e1913149e` |

Two inputs are excluded from the bundle set deliberately: `starlight_help/dist/**`, the
documentation site rather than the application client, and `zerver/openapi/javascript_examples.js`,
which is generated from the specification and would inflate every join by construction.

## Path form, settled before measuring

The specification declares **bare paths** (`/messages`, `/users/me/subscriptions`) with `/api/v1`
in `servers:`, including a `.../json` server entry for the test suite. The client calls the same
handlers under a prefix: call sites in the 12.3 source show `/json/messages/`,
`/json/users/me/subscriptions`, `/json/settings`, and also `/api/v1/users/me/api_key/regenerate`.
`web/src/channel.ts` passes `args.url` to jQuery verbatim and prepends nothing, so callers carry
the prefix.

**Rule:** strip at most one leading `/json` or `/api/v1` from extracted paths; the specification
side is used verbatim. Without the strip both classifiers score under 2 per cent, which would
measure the normalisation rather than the classifier.

## The structural premise, measured

| Presence test | Result |
|---|---|
| Specification path appears verbatim | 48/115 = 41.7% |
| Specification path with `/json` prepended | 44/115 = 38.3% |
| Literal stem before the first `{param}` | 91/115 = 79.1% |
| **Present, union of the three** | **91/115 = 79.1%** |

Zulip builds parameterised paths by concatenation, so the `{param}` form is never a literal and a
verbatim test alone understates presence by 37 points. After normalisation, 90 distinct present
paths — the recall denominator.

## Results

Precision over **rows**, recall over **distinct paths**.

| Measure | Original | Repaired |
|---|---:|---:|
| API-shaped rows emitted | 53 | 358 |
| of which absolute third-party URLs | 12 | 108 |
| relative paths | 41 | 250 |
| rows whose prefix was stripped | 23/41 | 97/250 |
| matching rows | 18 | 74 |
| **Precision, set as emitted** | **18/53 = 34.0%** | **74/358 = 20.7%** |
| **Recall over the 90 present paths** | 14/90 = 15.6% | **56/90 = 62.2%** |
| Specification coverage | 14/114 = 12.3% | 56/114 = 49.1% |

**Extraction ceiling: 56/90 = 62.2 per cent**, identical for both runs. The repaired classifier's
recall equals that ceiling exactly, so the figure measures extraction rather than classification.
Roughly two fifths of the interface present in this client is never recovered.

## Evidence tier

| Tier | Rows | Precision |
|---|---:|---:|
| request-construction | 28 | 28.6% |
| structural | 177 | 36.2% |
| none | 62 | 19.4% |
| router-definition | 0 | — |

Tiers are assigned by `classifier_rule.classify_endpoint` over every relative-path record in the
extraction, so both runs yield this table; `reproduce_precision.py` prints it.

**Tier spread, request-construction minus absent-evidence: +9.2 points**, against a stated bar of
+20. The tier carries no signal here, and the ordering inverts: the structural tier outranks
request-construction, so the tier is not monotone in the strength of the evidence it records. Zulip routes every request through its own wrapper around
jQuery, so a URL literal sits beside `channel.post(` rather than beside `fetch`, `axios` or
`$.ajax`, and only 28 of 250 relative rows acquire request-construction evidence.

The navigation-exclusion class matched **0 rows**, as recorded in advance: that rule is written
against React Router shapes and Zulip has no such router. This measurement therefore exercises the
admission half of the repaired rule.

## Verdict under the single criterion

| Criterion | Required | Measured | Result |
|---|---|---|---|
| Primary | recall ≥ 90% of the measured ceiling | 62.2/62.2 = 100% | **met** |
| Secondary | as-emitted precision falls ≤ 5 points | −13.3 points | **missed** |

**Partially generalized.** The admission half reaches everything reachable; precision falls because
the repaired rule emits 6.8 times as many rows including 9 times as many absolute third-party URLs,
with no navigation exclusions to offset the cost.

## Reproduce

```
MSYS_NO_PATHCONV=1 python ../validation/reproduce_precision.py recon-zulip    --spec zulip-openapi.json --strip-prefix /json,/api/v1
MSYS_NO_PATHCONV=1 python ../validation/reproduce_precision.py recon-zulip-v2 --spec zulip-openapi.json --strip-prefix /json,/api/v1
```

`MSYS_NO_PATHCONV=1` is required under Git Bash, which rewrites a leading-slash argument into a
Windows path and then strips nothing.

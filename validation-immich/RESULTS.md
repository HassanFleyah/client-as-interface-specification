# Immich v3.2.4 — measurement record

Measured 2026-10-01 against the criterion in `PRE-REGISTRATION.md`, fixed before measurement.
Reported per application; not pooled with Jellyfin or Zulip.

## Artefact and its scope condition

| Input | Value |
|---|---|
| Release tag | `v3.2.4`, 2026-09-28 |
| Specification | `open-api/immich-openapi-specs.json`, OpenAPI 3.0.0, info.version 3.2.4, **192 declared paths**, `servers: ["/api"]` |
| Specification sha256 | `0583d80f74f2f3997e573c618195c4945b399afb00da15570888254e72654d5a` |
| Artefact | `@immich/sdk` 3.2.4 from npm, `package/build/*.js`, 3 files, 104,910 bytes |
| Artefact content digest | `b732fa421f1598992e63e6bc4dc7dd47e13fb8abc850a86b96298b0a10e80d88` |
| Generator | oazapfts — 200 `fetchJson` call sites, 0 bare `fetch(` |
| Prefix strip | `/api`, affecting 1 of 162 rows: the SDK stores bare paths and oazapfts prepends the base at runtime |

**The measured artefact is the generated API client, not a built web application.** Immich's web
client carries no URL literals; its own code calls named SDK functions such as `deleteAssets({…})`.
The release publishes mobile APKs and compose files but no web bundle.

**Precision on this artefact measures the generator, not the classifier.** `@immich/sdk` is
code-generated from the same specification used here as ground truth, so every path string in it
originates in the ground truth. Presence is 192 of 192 for the same reason and is reported only to
establish the recall denominator. **Immich is a valid test of the extraction ceiling and of the
evidence tier, and an invalid test of precision.**

## Results

Precision over **rows**, recall over **distinct paths**.

| Measure | Original | Repaired |
|---|---:|---:|
| API-shaped rows emitted | 62 | 163 |
| of which absolute third-party URLs | 0 | 1 |
| matching rows | 61 | 161 |
| Precision, set as emitted — *not a classifier measurement* | 98.4% | 98.8% |
| **Recall over the 192 present paths** | 60/192 = 31.2% | **159/192 = 82.8%** |
| Specification coverage | 31.2% | 82.8% |

**Extraction ceiling: 159/192 = 82.8 per cent**, identical for both runs. The repaired
classifier's recall equals that ceiling exactly, so the figure measures extraction rather than
classification.

## Evidence tier

| Tier | Rows | Precision |
|---|---:|---:|
| request-construction | 107 | 100.0% |
| structural | 40 | 97.5% |
| none | 20 | 100.0% |
| router-definition | 0 | — |

**Tier spread, request-construction minus absent-evidence: +0.0 points**, against a stated bar of
+20 for the tier to be said to carry signal. The tier carries no signal on this artefact. oazapfts
emits a literal `method` beside each path, so method detection assigns request-construction
evidence to most rows; evidence quantity and evidence quality are not the same thing.

## Verdict under the single criterion

| Criterion | Required | Measured | Result |
|---|---|---|---|
| Primary | recall ≥ 90% of the measured ceiling | 82.8/82.8 = 100% | **met** |
| Secondary | as-emitted precision falls ≤ 5 points | **not assessable** | — |

**Primary met; secondary not assessable.** The secondary cannot be evaluated on an artefact whose
path strings are generated from the ground truth.

## Residual ceiling gap

33 of 192 paths unrecovered, with two causes and no unexplained residue:

| Cause | Count | Example |
|---|---:|---|
| Template interpolation containing a nested object | 27 | a generated query-string helper |
| Two or more interpolations in one path | 6 | `/assets/{id}/metadata/{key}` |

Both reduce to one mechanism: neither relative-path pattern spans a template interpolation whose
contents are non-trivial. The plain-path character class excludes parentheses, so an interpolation
holding a function call breaks the match; the template pattern tolerates one interpolation of at
most sixty characters containing no closing brace, which a query-string builder exceeds.

An interpolation-aware scanner is the correct fix. It is **proposed and not applied**, with the
prediction recorded in advance: the ceiling should move from 82.8 per cent to approximately 99 per
cent, and Jellyfin's should be essentially unchanged because its bundles carry literal `{itemId}`
braces rather than interpolations.

## Reproduce

```
MSYS_NO_PATHCONV=1 python ../validation/reproduce_precision.py recon-immich    --spec immich-openapi.json --strip-prefix /api
MSYS_NO_PATHCONV=1 python ../validation/reproduce_precision.py recon-immich-v2 --spec immich-openapi.json --strip-prefix /api
```

`MSYS_NO_PATHCONV=1` is required under Git Bash, which rewrites a leading-slash argument into a
Windows path and then strips nothing.

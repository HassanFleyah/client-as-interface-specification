# Validation of the extractor — Section 6.2

Three applications, two of them held out. This directory is Jellyfin; `../validation-zulip/`
and `../validation-immich/` are its siblings and each carries its own specification,
pre-registration and `*-VALIDATION.json`. The scripts here serve all three.

| Application | Package | Precision orig → repaired | Ceiling | Repaired recall | Tier spread |
|---|---|---|---|---|---|
| Jellyfin | `validation/` | 32.9% → 45.3% | 98.8% | 98.8% = 100% of ceiling | +40.1 pts |
| Zulip 12.3 | `../validation-zulip/` | 34.0% → 20.7% | 62.2% | 62.2% = 100% of ceiling | +9.2 pts |
| Immich v3.2.4 | `../validation-immich/` | 98.4% → 98.8% **not assessable** | 82.8% | 82.8% = 100% of ceiling | **not assessable** |

**The two `PRE-REGISTRATION.md` files are dated commitment records and are not edited.** They state
what was fixed before each held-out measurement, which is the only property that makes them evidence;
their file timestamps are part of that. Any calibration figure quoted inside them is the figure that
was available when the commitment was written. The authoritative figures are the ones
`reproduce_precision.py` prints.

**Tier figures.** The spread is the request-construction tier's precision minus the
absent-evidence tier's, over every relative-path record in an extraction, with tiers assigned by
`classifier_rule.classify_endpoint`. `reproduce_precision.py` prints the full table for any run.
Immich admits no assessment of the tier: the artefact yields one false positive among 167 relative
rows, so no tier has anything to discriminate.

**Immich precision is not a classifier measurement.** `@immich/sdk` is code-generated from the
specification used here as ground truth, so every path string in the artefact originates in the
ground truth. Immich is a valid test of the ceiling and the tier and an invalid test of precision.

One criterion, applied to all three: **primary** — repaired recall reaches at least 90% of the
measured extraction ceiling; **secondary** — as-emitted precision falls by no more than 5 points.
Verdicts: Jellyfin generalized on both axes; Zulip partially generalized; Immich primary met with
the secondary not assessable.

Reproduce any column:

```
python reproduce_precision.py recon-v2
MSYS_NO_PATHCONV=1 python ../validation/reproduce_precision.py recon-zulip-v2  --spec zulip-openapi.json  --strip-prefix /json,/api/v1
MSYS_NO_PATHCONV=1 python ../validation/reproduce_precision.py recon-immich-v2 --spec immich-openapi.json --strip-prefix /api
```

`MSYS_NO_PATHCONV=1` is required under Git Bash, which rewrites a leading-slash argument into a
Windows path and silently strips nothing.

Measures the extractor used throughout the manuscript against a published OpenAPI
specification serving as ground truth. The reporting commitment was recorded in the
manuscript before the measurement was taken.

## Contents

| File | Purpose |
|---|---|
| `openapi.json` | Jellyfin API 12.1.0 specification — ground truth, 294 declared paths |
| `recon/` | output of the ORIGINAL classifier — every figure in the manuscript derives from this |
| `recon-v2/` | output of the REPAIRED classifier, retained as the second data point in Section 6.2 |
| `classifier_rule.py` | both classification rules, verbatim from the extractor, with a self-test |
| `reproduce_precision.py` | regenerates precision and coverage for a given run; `python reproduce_precision.py recon-v2` for the repaired one |
| `reproduce_recall.py` | regenerates the presence and recall figures; needs the client bundles |
| `VALIDATION.json` | every published figure, with the pinned URL and digest of each input |
| `validation-results.json` | Jellyfin, original classifier: the row, hit and false-positive counts behind 32.9%, 38.7%, 88.9% and the 7.8% coverage figure. Regenerable with `reproduce_precision.py recon`. |
| `validation-recall.json` | Jellyfin presence and ceiling: 244 of 294 paths present verbatim, 240 of 243 reported anywhere, 23 of 243 admitted, and the three paths missed entirely. **Not regenerable from this directory** — `reproduce_recall.py` needs the client bundles, which are not redistributed. |

## Reproduce

```
python reproduce_precision.py
```

For the recall figures, fetch the client first. The archive is version-pinned, so
this remains valid after later releases:

```
curl -L -o jellyfin_12.1.tar.gz https://repo.jellyfin.org/files/server/portable/stable/v12.1/any/jellyfin_12.1.tar.gz
sha256sum jellyfin_12.1.tar.gz
mkdir -p js-loot/js
tar -xzf jellyfin_12.1.tar.gz -C js-loot/js --strip-components=2 --wildcards 'jellyfin/jellyfin-web/*.js'
python reproduce_recall.py
```

**Do not verify the archive by digest.** The server re-compresses it, so two fetches of
the same pinned URL gave `56c1c79a...` and `ae7f2d57...`. Verify the extracted client by
content digest instead: `3b636f45363b8561becb0ddf09303ed117210e4ebef89bce235c0e53a0249436`
over 986 `.js` files totalling 26,274,040 bytes, each file contributing its repo-relative
path then the SHA-256 of its bytes, ordered by path.

The bundles are not redistributed here — Jellyfin's client is GPL-licensed and the set is
28 MB — only the measurements taken over them. The `latest-stable` alias used during
collection is mutable and should not be cited.

## Headline figures

| Measure | Value |
|---|---|
| Specification paths present verbatim in the client | 244 / 294 = 83.0% |
| Of those present, reported anywhere by the extractor | 240 / 243 = 98.8% |
| Of those present, admitted to the API-shaped set | 23 / 243 = 9.5% |
| Precision, set as emitted | 24 / 73 = 32.9% |
| Precision, absolute third-party URLs set aside | 24 / 62 = 38.7% |
| Precision, post-hoc router class also set aside | 24 / 27 = 88.9% |
| Specification coverage (not recall) | 23 / 293 = 7.8% |

Precision against a published specification is a lower bound: a route absent from a
specification is not necessarily absent from the server. The client-router class was
identified after inspecting the misses, so 88.9% is a decomposition and not an
independent result.

## The repaired classifier

The measurement above diagnosed a keyword allowlist as the cause of both failure
directions. The classifier in `js_recon.py` was rewritten to use call-site evidence and
re-measured on the same ground truth; `recon-v2/` is that run.

| Measure | Original | Repaired |
|---|---|---|
| Precision, **set as emitted** | 32.9% (24/73) | **45.3%** (247/545) |
| Precision, absolute third-party URLs set aside | 38.7% (24/62) | 62.4% (247/396) |
| Recall over the 243 present paths | 9.5% | **98.8%** |
| Navigation class excluded | — | 28 rows, 0% precision, no real route lost |
| Absolute third-party rows admitted | 11 of 73 (15%) | 149 of 545 (27%) — the cost |

**Quote the set-as-emitted row.** Pairing 32.9% with 62.4% mixes two denominators and
overstates the gain by more than double; the honest pairs are 32.9 → 45.3 and 38.7 → 62.4.

98.8% recall is the extraction ceiling, not a classification gain: 240 of the 243 present
paths were always being found, and the repaired rule simply stops rejecting them. What is
new is the per-route evidence tier, which makes the operating point a choice.

Manuscript figures are **not** restated under the repaired tool: Section 6 describes a
corpus that was assessed with the original one.

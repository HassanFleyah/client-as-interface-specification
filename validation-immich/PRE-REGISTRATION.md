# Pre-registration — third-application test

**Written 2026-10-01, before any Immich precision or recall figure was computed.**
Held-out application: Immich v3.2.4. Reported per application, never pooled; three
applications estimate nothing more than two do.

## Pre-flight changed why this application is being used

It was selected as a direct-`fetch` application, to isolate the wrapper variable that
explained the Zulip failure. **Pre-flight falsified that premise and the record should say
so rather than quietly re-describing the test.** Immich's web client depends on
`@immich/sdk`, a code-generated API client, and its own source calls named SDK functions —
`bulkTagAssets({...})`, `deleteAssets({...})` — with no URL literal at any call site. Immich
is therefore not a direct-`fetch` case. It is a third and more extreme wrapper case, in
which the path literals and the application code live in different modules.

Two consequences, both recorded before measuring:

1. **The artefact is the generated SDK, not the built web client.** The release publishes
   mobile APKs and compose files but no web bundle; no Docker is available here; and the
   paths exist only inside the SDK. The measured artefact is `@immich/sdk` 3.2.4 from the npm
   registry, whose version matches the release tag exactly. This is a narrower artefact than
   the Jellyfin and Zulip bundle sets, and results are not comparable to them on scope.
2. **Presence is tautological here and is not evidence for Section 3.1.** The SDK is
   generated from the specification, so specification paths appear in it by construction. A
   presence figure will be reported as a sanity check on the harvest and must not be read as
   replicating the structural premise, which Jellyfin and Zulip tested on hand-written
   application code.

## The commitment

Both classifiers run over the same artefact. Precision over **rows**, recall over **distinct
paths**, on both precision bases — set as emitted, and absolute third-party URLs set aside —
reported as a pair or not at all. Every figure carries its denominator. If recall lands on
the extraction ceiling, that is stated as an extraction result and not a classification
result. The classifier is not touched after any Immich figure exists; selection stays by
file, `js_recon.py.bak` against `js_recon.py`, with no edit to either.

## Recorded prediction

**The tiering cannot discriminate between paths on generated code.** Every path in a
generated SDK sits in the same surrounding construct emitted by the same generator template,
so evidence read from the call site is identical for all of them. The prediction is therefore
not "the navigation class is near-empty", as it was for Zulip, but something stronger and
falsifiable: **the overwhelming majority of extracted paths will land in a single evidence
tier**, whichever one the generator's wrapper happens to trip, and the spread in precision
between tiers will be near zero. If instead the tiers separate, the wrapper explanation
offered for the Zulip result is wrong and must be withdrawn.

## Thresholds, fixed in advance

The Zulip primary threshold was defective: an absolute point-gain requirement was placed on
a quantity bounded by a per-application ceiling. The correction recorded at that time is
applied here, and only here.

- **Primary — admission half, ceiling-relative.** The repaired classifier's recall over
  distinct present paths reaches at least **90 per cent of the measured extraction ceiling**
  for this artefact. Jellyfin and Zulip both reached 100 per cent of their ceilings.
- **Secondary — no precision regression.** As-emitted precision falls no more than
  **5 percentage points** below the original classifier's. Held identical to Zulip so the two
  applications are judged on the same criterion.
- **Tertiary — does the tiering carry signal.** The request-construction tier's precision
  exceeds the absent-evidence tier's by at least **20 percentage points**. Jellyfin: 90.8
  against 50.4, a spread of 40.4, signal present. Zulip: 21.4 against 20.9, a spread of 0.5,
  no signal. This is the criterion the wrapper hypothesis actually predicts on.

**Verdict labels.** Primary and secondary met → the repair generalized to this artefact.
Primary met, secondary missed → partially generalized, cost quantified. Primary missed → did
not generalize. The tertiary is reported separately and decides whether the wrapper
explanation survives; it does not feed the generalisation verdict.

## Normalisation, decided before measuring, with its evidence

- The specification declares **192 bare paths** (`/activities`, `/admin/config`) with the
  base in `servers: ["/api"]`.
- The extracted side is therefore expected to carry a leading `/api`.

**Rule:** strip at most one leading `/api` from extracted paths; the specification side is
used verbatim; trailing slashes and `{param}` placeholders are collapsed on both sides as in
the earlier runs. The join is reported both with and without the strip, and the number of
rows affected is reported, so the result's dependence on this decision is visible. The
argument will be passed under `MSYS_NO_PATHCONV=1`, because Git Bash rewrote `/json` to a
Windows path during the Zulip run and produced a precision figure of 1.9 per cent before the
fault was caught.

## Inputs fixed at this point

| Input | Value |
|---|---|
| Release tag | `v3.2.4`, published 2026-09-28 |
| Specification | `open-api/immich-openapi-specs.json` at the tag |
| Specification sha256 | `0583d80f74f2f3997e573c618195c4945b399afb00da15570888254e72654d5a` |
| Specification | OpenAPI 3.0.0, info.version 3.2.4, 926,155 bytes, **192 declared paths** |
| Artefact | `@immich/sdk` 3.2.4 from the npm registry |
| Original classifier | `js_recon.py.bak` — `bool(API_HINT.search(value))` |
| Repaired classifier | `js_recon.py` — `classify_endpoint` |

The artefact will be identified by a content digest over the extracted JavaScript files, not
by the tarball digest.

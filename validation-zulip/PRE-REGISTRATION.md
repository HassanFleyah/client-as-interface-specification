# Pre-registration — second-application test of the repaired classifier

**Written 2026-10-01, before any Zulip precision or recall figure was computed.**
Held-out application: Zulip Server 12.3. Specification and client are taken from the
same release tag, which is the confound this evaluation exists to remove.

## The commitment

Both classifiers — the original keyword allowlist and the repaired evidence-based rule —
will be run over the same Zulip bundle set, and results reported per application, never
pooled with Jellyfin. Two applications estimate nothing, so no mean, no combined figure.
Precision is reported over **rows** and recall over **distinct paths**, on both precision
bases: the set as emitted, and the set with absolute third-party URLs set aside. Both
pairs are reported or neither, because pairing one basis against the other already
overstated a gain by more than double in this manuscript. Every figure carries its
denominator. If Zulip's recall lands on its own extraction ceiling, that is stated
explicitly as not a classification result, exactly as it was for Jellyfin. The classifier
will not be touched after any Zulip number is held; an underperforming repair is the
result, and a more interesting one than a pass.

## Recorded prediction

The navigation-exclusion half of the repair is expected to be **near-empty on Zulip**.
That rule was written against React Router shapes — link targets, `navigate` calls, route
objects pairing `path:` with `element:` or `lazy:`. Zulip's frontend is webpack plus
Handlebars plus TypeScript with no React and no React Router, so those shapes should be
absent. This evaluation therefore tests the **admission** half of the repair: whether
default-include plus call-site evidence recovers the interface, not whether the exclusion
rule removes navigation noise. If the exclusion class is non-empty, that is a finding in
its own right and will be reported with the matched rows.

## Threshold, fixed in advance

Stated on both halves, because the exclusion half is predicted inert and a single
combined criterion would hide that.

- **Primary — the admission half.** Recall over distinct specification paths present in
  the client rises by at least **+40 percentage points** over the original classifier,
  **and** lands within **10 points** of the measured extraction ceiling for Zulip. On
  Jellyfin recall rose 89.3 points and landed exactly on the ceiling.
- **Secondary — no precision regression.** As-emitted precision does not fall more than
  **5 percentage points** below the original classifier's as-emitted precision. A gain is
  welcome but is not required, because the mechanism that produced the Jellyfin precision
  gain is predicted absent here.

**Verdict labels.** Both met → the repair generalized. Primary met, secondary missed →
partially generalized, with the precision cost quantified. Primary missed → the repair did
not generalize, reported as such with no reinterpretation of the threshold.

## Normalisation, decided before measuring, with its evidence

Pre-flight established that spec and client do not use the same path form, which is the
Grafana failure mode in miniature:

- The specification declares **115 bare paths** (`/messages`, `/users/me/subscriptions`,
  `/settings`) with `/api/v1` living in `servers:`, including a `.../json` server entry
  for the test suite.
- The client calls the same handlers under a prefix. Call sites in the 12.3 source show
  `/json/messages/`, `/json/users/me/subscriptions`, `/json/fetch_api_key`,
  `/json/settings`, and also `/api/v1/users/me/api_key/regenerate`. `web/src/channel.ts`
  passes `args.url` to jQuery verbatim and prepends nothing, so callers carry the prefix.

**Rule:** on the extracted side, strip a single leading `/json` or `/api/v1` before
comparison; the spec side is used verbatim. Trailing slashes and `{param}` placeholders
are collapsed on both sides as in the Jellyfin run. The number of rows the strip affects
will be reported, and the join will also be reported without the strip, so that the
dependence of the result on this decision is visible rather than assumed.

## Not yet established

The location of built bundles inside `zulip-server-12.3.tar.gz` is unverified; it is
step-4 work and will be recorded when the archive is opened. The archive will not be
identified by its own digest — Jellyfin's is re-compressed server-side and returned two
different hashes for one pinned URL — so a content digest over the extracted bundle set
will be recorded instead.

## Inputs fixed at this point

| Input | Value |
|---|---|
| Release tag | `12.3`, published 2026-09-21 |
| Specification | `zerver/openapi/zulip.yaml` at tag 12.3 |
| Specification sha256 | `15c17a2d53da572191f064722102d819c200c63a5ee7d0fe20da3dcdfd74cec5` |
| Specification size | 1,507,348 bytes, 31,231 lines, 115 declared paths |
| Client archive | `zulip-server-12.3.tar.gz`, 141,699,780 bytes |
| Original classifier | `js_recon.py.bak` — `bool(API_HINT.search(value))` |
| Repaired classifier | `js_recon.py` — `classify_endpoint` |

Selection between classifiers is by file, with no edit to either, so neither rule can be
altered once a Zulip figure exists.

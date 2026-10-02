# The Client as Interface Specification

**API attack surface recovery for AI-assisted web security assessment**

Hasan Flayyih Abdullah · working manuscript, 1 October 2026 · not peer reviewed

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23099358.svg)](https://doi.org/10.5281/zenodo.23099358)

A web application's server can only be reached through its interface, and the client
that calls that interface is delivered in full to every browser. The client is
therefore a recoverable specification of the interface, and this paper argues that for
the vulnerability classes the OWASP API Security Top 10 ranks highest, that
specification is sufficient — both to form a hypothesis and to confirm it.

The paper's main contribution is a consequence for measurement rather than for
discovery: **the specification is what makes a request well-formed, and a malformed
request is observationally indistinguishable from an enforced authorization
boundary.** A procedure that recovers paths without recovering identifier encodings
and body schemas therefore produces negative results that are void rather than
informative, and cannot tell that this has happened.

📄 **[paper.pdf](paper.pdf)** · 15 pages · source in [manuscript.md](manuscript.md)

---

## Reproduce any figure in the paper

No account, no network, no running system. Python 3.11, standard library only.

```bash
python validation/reproduce_precision.py validation/recon
```

That regenerates every precision, coverage and evidence-tier figure for the original
classifier on Jellyfin. Change the run directory and the specification to get any
other column:

```bash
# Jellyfin, repaired classifier
python validation/reproduce_precision.py validation/recon-v2

# Zulip 12.3, both classifiers
python validation/reproduce_precision.py validation-zulip/recon-zulip \
    --spec validation-zulip/zulip-openapi.json --strip-prefix /json,/api/v1
python validation/reproduce_precision.py validation-zulip/recon-zulip-v2 \
    --spec validation-zulip/zulip-openapi.json --strip-prefix /json,/api/v1

# Immich 3.2.4, both classifiers
python validation/reproduce_precision.py validation-immich/recon-immich \
    --spec validation-immich/immich-openapi.json
python validation/reproduce_precision.py validation-immich/recon-immich-v2 \
    --spec validation-immich/immich-openapi.json
```

The script prints every denominator rather than a single ratio, because the same
measurement is describable two ways depending on which rows you count — and the paper
reports both.

The classification rules themselves are in
[`validation/classifier_rule.py`](validation/classifier_rule.py), lifted verbatim from
the extractor, with a self-test that shows each failure direction:

```bash
python validation/classifier_rule.py
```

> **On Git Bash for Windows:** prefix the Zulip commands with `MSYS_NO_PATHCONV=1`.
> Git Bash rewrites a leading-slash argument into a Windows path, so `--strip-prefix
> /json` silently becomes `C:/Program Files/Git/json` and the measurement collapses to
> 1.9 per cent precision with no error. This is the same class of trap the paper is
> about, and it cost a re-run.

---

## What was measured

One extractor, two classification rules, three applications — Jellyfin, plus Zulip and
Immich held out. Each application supplies a published OpenAPI specification as ground
truth and a publicly distributed client. Precision is counted over emitted **rows**;
recall over **distinct paths**.

| | Jellyfin 12.1 | Zulip 12.3 | Immich 3.2.4 |
|---|---:|---:|---:|
| Declared spec paths | 294 | 115 | 192 |
| **Extraction ceiling** | **98.8%** | **62.2%** | **82.8%** |
| Repaired recall | 98.8% | 62.2% | 82.8% |
| — as share of ceiling | 100% | 100% | 100% |
| Precision, original rule | 32.9% | 34.0% | 98.4% ⚠ |
| Precision, repaired rule | 45.3% | 20.7% | 98.8% ⚠ |
| Evidence-tier spread | +40.1 pts | +9.2 pts | not assessable |

⚠ **Immich's precision figures measure the generator, not the classifier.** Its web
client carries no URL literals; the paths exist only inside `@immich/sdk`, which is
code-generated from the same specification used here as ground truth, so every path
string originates in the ground truth and precision approaches 100 per cent by
construction. Immich is a valid test of the ceiling and an invalid test of precision
and of the tier. The paper states this rather than reporting the number as a success.

**What the three applications show.** One result generalizes: the repaired rule reaches
100 per cent of the extraction ceiling on all three, which is the effect of no longer
rejecting rather than of classifying better. Two do not. Precision is
application-dependent and can fall sharply. The per-route evidence tier separates
precision strongly on one application, weakly on a second, and is not assessable on the
third, so it is not a general operating point. And the ceilings themselves relocate the
larger loss from classification to extraction wherever a client builds its paths at
runtime.

---

## Layout

```
paper.pdf                       the paper
manuscript.md                   its source

validation/                     Jellyfin — the application the diagnosis came from
  openapi.json                  ground truth (third party, see THIRD-PARTY.md)
  recon/                        output of the ORIGINAL classifier
  recon-v2/                     output of the REPAIRED classifier
  reproduce_precision.py        precision, coverage and tier figures
  reproduce_recall.py           presence and recall figures (needs the bundles)
  classifier_rule.py            both rules, verbatim, with a self-test
  VALIDATION.json               every published figure, with its inputs

validation-zulip/               Zulip — held out
  PRE-REGISTRATION.md           thresholds, fixed before the measurement
  RESULTS.md  ZULIP-VALIDATION.json
  zulip.yaml  zulip-openapi.json
  recon-zulip/  recon-zulip-v2/

validation-immich/              Immich — held out
  PRE-REGISTRATION.md  RESULTS.md  IMMICH-VALIDATION.json
  immich-openapi.json
  recon-immich/  recon-immich-v2/
```

The two held-out packages each carry the pre-registration recording their thresholds.
No pre-registration exists for Jellyfin, which is the application the repair was
developed on and is not held out — the paper says so, because the one application where
the evidence tier separates most strongly is the one that was not held out.

---

## What is not included, and why

**The client bundles.** They are the other projects' code, they are large, and two of
the three are copyleft. `reproduce_recall.py` prints the pinned URL and the expected
digest and exits rather than proceeding without them.

| | Source | Content digest |
|---|---|---|
| Jellyfin | [v12.1 portable archive](https://repo.jellyfin.org/files/server/portable/stable/v12.1/any/jellyfin_12.1.tar.gz) | `3b636f45…49436` over 986 `.js`, 26,274,040 bytes |
| Zulip | tag `12.3`, `*/prod-static/serve/webpack-bundles/*.js` | `635e3ed4…3149e` over 64 files, 11,321,957 bytes |
| Immich | `@immich/sdk` 3.2.4 from npm, `package/build/*.js` | `b732fa42…e80d88` over 3 files, 104,910 bytes |

**Do not verify the Jellyfin archive by its own digest.** The server re-compresses it,
so two fetches of the same pinned URL returned different archive hashes. Verify the
extracted bundle set by content digest instead: each file contributes its
repository-relative POSIX path, then the SHA-256 of its bytes, ordered by path.

**The 45-target field corpus of Section 6** is not included. It is authorized bug
bounty work against production systems under programme rules, and the targets are not
named anywhere in the paper.

---

## Status

Not peer reviewed. Not yet on arXiv — a first cs.CR submission requires endorsement
from an established author in that archive, which is in progress. This repository is
the citable form in the meantime, archived on Zenodo with the concept DOI
[10.5281/zenodo.23099358](https://doi.org/10.5281/zenodo.23099358), which always
resolves to the latest version.

Corrections are welcome, including to the figures. Every one of them regenerates from
the scripts above, so a disagreement can be settled rather than argued.

## License

The paper is CC BY 4.0. The scripts are MIT. The three OpenAPI specifications belong to
their projects and are redistributed under their own licenses — see
**[THIRD-PARTY.md](THIRD-PARTY.md)** and [LICENSE](LICENSE).

## Citation

```bibtex
@misc{abdullah2026client,
  author = {Hasan Flayyih Abdullah},
  title  = {The Client as Interface Specification: API Attack Surface
            Recovery for AI-Assisted Web Security Assessment},
  year   = {2026},
  doi    = {10.5281/zenodo.23099358},
  url    = {https://doi.org/10.5281/zenodo.23099358},
  note   = {Working manuscript, not peer reviewed}
}
```

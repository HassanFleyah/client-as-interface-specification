# Third-party material in this repository

The three OpenAPI specification files used as ground truth belong to their projects,
not to this work. They are redistributed here so that the measurements can be
reproduced against the exact bytes they were taken from. Each is listed below with
its project, its license, the URL it came from, and its SHA-256 as redistributed —
every digest recomputed from the file in this repository, not copied from a record.

Neither the CC BY 4.0 license on the paper nor the MIT license on the scripts applies
to these files.

---

## Jellyfin — GPL-2.0

| | |
|---|---|
| File | `validation/openapi.json` |
| Project | [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) |
| License | GNU General Public License v2.0 |
| Spec version | OpenAPI 3.0.4, `info.version` 12.1.0 |
| Source | https://api.jellyfin.org/openapi/jellyfin-openapi-stable.json |
| Size | 1,895,106 bytes |
| SHA-256 | `6cc7386ebf8a52a7264969fa63a786dc746e9e37af573babf8b35bcfa1b5021d` |

The matching client — the 986 JavaScript bundles of the Jellyfin web client — is
**not** redistributed here, because it is GPL-licensed and 28 MB. The README gives the
version-pinned archive URL and the content digest needed to reconstruct it.

## Zulip — Apache-2.0

| | |
|---|---|
| Files | `validation-zulip/zulip.yaml`, `validation-zulip/zulip-openapi.json` |
| Project | [zulip/zulip](https://github.com/zulip/zulip) |
| License | Apache License 2.0 |
| Spec path in repo | `zerver/openapi/zulip.yaml` at tag `12.3` |
| Size | 1,507,348 bytes (YAML) · 1,272,966 bytes (JSON) |
| SHA-256 | `15c17a2d53da572191f064722102d819c200c63a5ee7d0fe20da3dcdfd74cec5` (YAML) |
| SHA-256 | `5fa7a3d0a9ffa8604fee85632a0b1928bd48de077029f4329c766e19063a8557` (JSON) |

`zulip-openapi.json` is the YAML file above converted to JSON once, unchanged in
content, because the comparison script reads JSON. Both are included so the
conversion itself can be checked.

## Immich — AGPL-3.0

| | |
|---|---|
| File | `validation-immich/immich-openapi.json` |
| Project | [immich-app/immich](https://github.com/immich-app/immich) |
| License | GNU Affero General Public License v3.0 |
| Spec version | OpenAPI 3.0.0, `info.version` 3.2.4 |
| Size | 926,155 bytes |
| SHA-256 | `0583d80f74f2f3997e573c618195c4945b399afb00da15570888254e72654d5a` |

The measured client artefact was `@immich/sdk` 3.2.4 from npm, which is generated from
the specification above. It is not redistributed here; the README records its content
digest.

---

## A note on what these files are used for

They are used only as ground truth to measure this work's own extraction tool. No
request was made to any running instance of any of these projects, and no
vulnerability in any of them is claimed or reported. The measurement is entirely
static: a published specification compared against strings found in a publicly
distributed client.

If a maintainer of any of these projects would prefer their specification not be
redistributed here, open an issue and it will be removed and replaced with a
download step.

# JavaScript Recon Report

- **Source:** `validation-immich\js-loot\js`
- **Generated:** 2026-10-01 21:07:06
- **Files analysed:** 3 (104,910 bytes)

- **First-party domains:** `immich.app`
- **Denominator:** 168 total · 167 first-party · 1 third-party SDK · 0 unresolved base
- **API-shaped only:** 63 total · 63 first-party · 0 third-party SDK · 0 unresolved base
- Quote coverage against the **first-party** number, and say which number you quoted. Nothing was dropped: every row is in `recon.json` with its `party` field.

| Finding | Count |
|---|---|
| API-looking endpoints | 63 |
|   ...of those, first-party | 63 |
|   ...of those, third-party SDK | 0 |
|   ...of those, unresolved base | 0 |
| Other URLs / paths | 105 |
| GraphQL operations | 0 |
| Secret candidates | 0 |
| DOM-XSS sink sites | 0 |

## 1. Hardcoded secrets & credentials

_No secret candidates above the configured thresholds._

## 2. API endpoints

| Endpoint | Party | Method(s) | Client | Request parts | Hits | File:Line |
|---|---|---|---|---|---|---|
| `/admin/users/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:277 |
| `/auth/pin-code` | first | DELETE, POST, PUT | - | body | 3 | `fetch-client.js`:912 |
| `/users/me/license` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:2550 |
| `/users/me/onboarding` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:2577 |
| `/admin/config` | first | PUT | - | body | 2 | `fetch-client.js`:74 |
| `/admin/database-backups` | first | DELETE | - | body | 2 | `fetch-client.js`:100 |
| `/admin/users/${encodeURIComponent(id)}/preferences` | first | PUT | - | body | 2 | `fetch-client.js`:317 |
| `/api` | first | ? | - | headers | 2 | `fetch-client.js`:11 |
| `/users/me` | first | PUT | - | body | 2 | `fetch-client.js`:2520 |
| `/users/me/preferences` | first | PUT | - | body | 2 | `fetch-client.js`:2604 |
| `/users/profile-image` | first | DELETE, POST | - | body | 2 | `fetch-client.js`:2622 |
| `/admin/auth/unlink-all` | first | POST | - | - | 1 | `fetch-client.js`:65 |
| `/admin/config/defaults` | first | ? | - | - | 1 | `fetch-client.js`:92 |
| `/admin/database-backups/${encodeURIComponent(filename)}` | first | ? | - | - | 1 | `fetch-client.js`:137 |
| `/admin/database-backups/start-restore` | first | POST | - | - | 1 | `fetch-client.js`:118 |
| `/admin/database-backups/upload` | first | POST | - | body | 1 | `fetch-client.js`:127 |
| `/admin/integrity/report/${encodeURIComponent($type)}/csv` | first | ? | - | - | 1 | `fetch-client.js`:174 |
| `/admin/integrity/report/${encodeURIComponent(id)}` | first | DELETE | - | - | 1 | `fetch-client.js`:157 |
| `/admin/integrity/report/${encodeURIComponent(id)}/file` | first | ? | - | - | 1 | `fetch-client.js`:166 |
| `/admin/integrity/summary` | first | ? | - | - | 1 | `fetch-client.js`:182 |
| `/admin/maintenance` | first | POST | - | body | 1 | `fetch-client.js`:190 |
| `/admin/maintenance/detect-install` | first | ? | - | - | 1 | `fetch-client.js`:200 |
| `/admin/maintenance/login` | first | POST | - | body | 1 | `fetch-client.js`:208 |
| `/admin/maintenance/status` | first | ? | - | - | 1 | `fetch-client.js`:218 |
| `/admin/notifications` | first | POST | - | body | 1 | `fetch-client.js`:226 |
| `/admin/notifications/templates/${encodeURIComponent(name)}` | first | POST | - | body | 1 | `fetch-client.js`:236 |
| `/admin/notifications/test-email` | first | POST | - | body | 1 | `fetch-client.js`:246 |
| `/admin/users` | first | POST | - | body | 1 | `fetch-client.js`:267 |
| `/admin/users/${encodeURIComponent(id)}/restore` | first | POST | - | - | 1 | `fetch-client.js`:335 |
| `/admin/users/${encodeURIComponent(id)}/sessions` | first | ? | - | - | 1 | `fetch-client.js`:344 |
| `/albums/${encodeURIComponent(id)}/users` | first | PUT | - | body | 1 | `fetch-client.js`:486 |
| `/api-keys/me` | first | ? | - | - | 1 | `fetch-client.js`:514 |
| `/asset-files/${encodeURIComponent(id)}/download` | first | ? | - | - | 1 | `fetch-client.js`:589 |
| `/auth/admin-sign-up` | first | POST | - | body | 1 | `fetch-client.js`:873 |
| `/auth/change-password` | first | POST | - | body | 1 | `fetch-client.js`:883 |
| `/auth/login` | first | POST | - | body | 1 | `fetch-client.js`:893 |
| `/auth/logout` | first | POST | - | - | 1 | `fetch-client.js`:903 |
| `/auth/session/lock` | first | POST | - | - | 1 | `fetch-client.js`:942 |
| `/auth/session/unlock` | first | POST | - | body | 1 | `fetch-client.js`:951 |
| `/auth/status` | first | ? | - | - | 1 | `fetch-client.js`:961 |
| `/auth/validateToken` | first | POST | - | - | 1 | `fetch-client.js`:969 |
| `/cluster-groups/${encodeURIComponent(id)}/users` | first | ? | - | - | 1 | `fetch-client.js`:1040 |
| `/config` | first | ? | - | - | 1 | `fetch-client.js`:1048 |
| `/config/defaults` | first | ? | - | - | 1 | `fetch-client.js`:1056 |
| `/oauth/authorize` | first | POST | - | body | 1 | `fetch-client.js`:1446 |
| `/oauth/backchannel-logout` | first | POST | - | body | 1 | `fetch-client.js`:1456 |
| `/oauth/callback` | first | POST | - | body | 1 | `fetch-client.js`:1466 |
| `/oauth/link` | first | POST | - | body | 1 | `fetch-client.js`:1476 |
| `/oauth/mobile-redirect` | first | ? | - | - | 1 | `fetch-client.js`:1486 |
| `/oauth/unlink` | first | POST | - | - | 1 | `fetch-client.js`:1494 |
| `/public/config` | first | ? | - | - | 1 | `fetch-client.js`:1717 |
| `/public/config/defaults` | first | ? | - | - | 1 | `fetch-client.js`:1725 |
| `/search/cities` | first | ? | - | - | 1 | `fetch-client.js`:1779 |
| `/search/explore` | first | ? | - | - | 1 | `fetch-client.js`:1787 |
| `/search/random` | first | POST | - | body | 1 | `fetch-client.js`:1870 |
| `/search/smart` | first | POST | - | body | 1 | `fetch-client.js`:1880 |
| `/search/statistics` | first | POST | - | body | 1 | `fetch-client.js`:1890 |
| `/server/config` | first | ? | - | - | 1 | `fetch-client.js`:1932 |
| `/users` | first | ? | - | - | 1 | `fetch-client.js`:2512 |
| `/users/${encodeURIComponent(id)}` | first | ? | - | - | 1 | `fetch-client.js`:2641 |
| `/users/${encodeURIComponent(id)}/profile-image` | first | ? | - | - | 1 | `fetch-client.js`:2649 |
| `/users/${userId}/profile-image` | first | ? | - | - | 1 | `index.js`:58 |
| `/users/${userId}/profile-image` | first | ? | - | - | 1 | `index.js`:58 |

### Other URLs and paths

<details><summary>Show 105 entries</summary>

| Value | Kind | File:Line |
|---|---|---|
| `/activities` | relative-path | `fetch-client.js`:35 |
| `/activities/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:56 |
| `/albums` | relative-path | `fetch-client.js`:378 |
| `/albums/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:406 |
| `/albums/${encodeURIComponent(id)}/assets` | template-path | `fetch-client.js`:436 |
| `/albums/assets` | relative-path | `fetch-client.js`:388 |
| `/albums/statistics` | relative-path | `fetch-client.js`:398 |
| `/api-keys` | relative-path | `fetch-client.js`:496 |
| `/api-keys/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:522 |
| `/api-keys/${encodeURIComponent(id)}/rotate` | template-path | `fetch-client.js`:549 |
| `/asset-files/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:572 |
| `/assets` | relative-path | `fetch-client.js`:597 |
| `/assets/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:706 |
| `/assets/${encodeURIComponent(id)}/edits` | template-path | `fetch-client.js`:716 |
| `/assets/${encodeURIComponent(id)}/metadata` | template-path | `fetch-client.js`:743 |
| `/assets/${encodeURIComponent(id)}/ocr` | template-path | `fetch-client.js`:778 |
| `/assets/${id}/original` | relative-path | `index.js`:55 |
| `/assets/${id}/original` | template-path | `index.js`:55 |
| `/assets/${id}/thumbnail` | relative-path | `index.js`:56 |
| `/assets/${id}/thumbnail` | template-path | `index.js`:56 |
| `/assets/${id}/video/playback` | relative-path | `index.js`:57 |
| `/assets/${id}/video/playback` | template-path | `index.js`:57 |
| `/assets/bulk-upload-check` | relative-path | `fetch-client.js`:633 |
| `/assets/copy` | relative-path | `fetch-client.js`:643 |
| `/assets/jobs` | relative-path | `fetch-client.js`:653 |
| `/assets/metadata` | relative-path | `fetch-client.js`:663 |
| `/cluster-groups/${encodeURIComponent(id)}/leave` | template-path | `fetch-client.js`:1004 |
| `/cluster-groups/${encodeURIComponent(id)}/regenerate-people` | template-path | `fetch-client.js`:1013 |
| `/cluster-groups/${encodeURIComponent(id)}/requests` | template-path | `fetch-client.js`:1022 |
| `/cluster-groups/requests` | relative-path | `fetch-client.js`:978 |
| `/cluster-groups/requests/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:986 |
| `/cluster-groups/requests/${encodeURIComponent(id)}/accept` | template-path | `fetch-client.js`:995 |
| `/duplicates` | relative-path | `fetch-client.js`:1090 |
| `/duplicates/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:1118 |
| `/duplicates/resolve` | relative-path | `fetch-client.js`:1108 |
| `/faces` | relative-path | `fetch-client.js`:1137 |
| `/faces/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:1147 |
| `/jobs` | relative-path | `fetch-client.js`:1167 |
| `/jobs/${encodeURIComponent(name)}` | template-path | `fetch-client.js`:1185 |
| `/libraries` | relative-path | `fetch-client.js`:1195 |
| `/libraries/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:1213 |
| `/libraries/${encodeURIComponent(id)}/scan` | template-path | `fetch-client.js`:1240 |
| `/libraries/${encodeURIComponent(id)}/statistics` | template-path | `fetch-client.js`:1249 |
| `/libraries/${encodeURIComponent(id)}/validate` | template-path | `fetch-client.js`:1257 |
| `/memories` | relative-path | `fetch-client.js`:1311 |
| `/memories/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:1339 |
| `/memories/${encodeURIComponent(id)}/assets` | template-path | `fetch-client.js`:1366 |
| `/notifications` | relative-path | `fetch-client.js`:1386 |
| `/notifications/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:1419 |
| `/partners` | relative-path | `fetch-client.js`:1513 |
| `/partners/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:1523 |
| `/people` | relative-path | `fetch-client.js`:1551 |
| `/people/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:1605 |
| `/people/${encodeURIComponent(id)}/merge` | template-path | `fetch-client.js`:1632 |
| `/people/${encodeURIComponent(id)}/reassign` | template-path | `fetch-client.js`:1642 |
| `/people/${encodeURIComponent(id)}/statistics` | template-path | `fetch-client.js`:1652 |
| `/people/${encodeURIComponent(id)}/thumbnail` | template-path | `fetch-client.js`:1660 |
| `/people/${personId}/thumbnail` | relative-path | `index.js`:59 |
| `/people/${personId}/thumbnail` | template-path | `index.js`:59 |
| `/people/merge` | relative-path | `fetch-client.js`:1595 |
| `/plugins/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:1709 |
| `/plugins/templates` | relative-path | `fetch-client.js`:1701 |
| `/queues` | relative-path | `fetch-client.js`:1733 |
| `/queues/${encodeURIComponent(name)}` | template-path | `fetch-client.js`:1741 |
| `/queues/${encodeURIComponent(name)}/jobs` | template-path | `fetch-client.js`:1759 |
| `/server/about` | relative-path | `fetch-client.js`:1916 |
| `/server/apk-links` | relative-path | `fetch-client.js`:1924 |
| `/server/features` | relative-path | `fetch-client.js`:1940 |
| `/server/license` | relative-path | `fetch-client.js`:1948 |
| `/server/media-types` | relative-path | `fetch-client.js`:1975 |
| `/server/ping` | relative-path | `fetch-client.js`:1983 |
| `/server/statistics` | relative-path | `fetch-client.js`:1991 |
| `/server/storage` | relative-path | `fetch-client.js`:1999 |
| `/server/version` | relative-path | `fetch-client.js`:2007 |
| `/server/version-check` | relative-path | `fetch-client.js`:2015 |
| `/server/version-history` | relative-path | `fetch-client.js`:2023 |
| `/sessions` | relative-path | `fetch-client.js`:2031 |
| `/sessions/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:2058 |
| `/sessions/${encodeURIComponent(id)}/lock` | template-path | `fetch-client.js`:2077 |
| `/shared-links` | relative-path | `fetch-client.js`:2097 |
| `/shared-links/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:2131 |
| `/shared-links/${encodeURIComponent(id)}/assets` | template-path | `fetch-client.js`:2158 |
| `/stacks` | relative-path | `fetch-client.js`:2178 |
| `/stacks/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:2208 |
| `/sync/ack` | relative-path | `fetch-client.js`:2244 |
| `/sync/stream` | relative-path | `fetch-client.js`:2272 |
| `/system-config` | relative-path | `fetch-client.js`:2282 |
| `/system-config/defaults` | relative-path | `fetch-client.js`:2300 |
| `/system-config/storage-template-options` | relative-path | `fetch-client.js`:2308 |
| `/system-metadata/admin-onboarding` | relative-path | `fetch-client.js`:2316 |
| `/system-metadata/reverse-geocoding-state` | relative-path | `fetch-client.js`:2334 |
| `/system-metadata/version-check-state` | relative-path | `fetch-client.js`:2342 |
| `/tags` | relative-path | `fetch-client.js`:2350 |
| `/tags/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:2388 |
| `/tags/${encodeURIComponent(id)}/assets` | template-path | `fetch-client.js`:2415 |
| `/tags/assets` | relative-path | `fetch-client.js`:2378 |
| `/trash/empty` | relative-path | `fetch-client.js`:2484 |
| `/trash/restore` | relative-path | `fetch-client.js`:2493 |
| `/trash/restore/assets` | relative-path | `fetch-client.js`:2502 |
| `/view/folder/unique-paths` | relative-path | `fetch-client.js`:2667 |
| `/workflows` | relative-path | `fetch-client.js`:2690 |
| `/workflows/${encodeURIComponent(id)}` | template-path | `fetch-client.js`:2708 |
| `/workflows/${encodeURIComponent(id)}/share` | template-path | `fetch-client.js`:2747 |
| `/workflows/triggers` | relative-path | `fetch-client.js`:2700 |
| `https://www.npmjs.com/package/oazapfts` | absolute-url | `fetch-client.js`:5 |

</details>

## 3. GraphQL operations

_None found._

## 4. DOM-XSS sinks

_None found._

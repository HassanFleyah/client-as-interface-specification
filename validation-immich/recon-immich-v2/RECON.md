# JavaScript Recon Report

- **Source:** `validation-immich\js-loot\js`
- **Generated:** 2026-10-01 21:07:06
- **Files analysed:** 3 (104,910 bytes)

- **First-party domains:** `immich.app`
- **Denominator:** 168 total · 167 first-party · 1 third-party SDK · 0 unresolved base
- **API-shaped only:** 168 total · 167 first-party · 1 third-party SDK · 0 unresolved base
- Quote coverage against the **first-party** number, and say which number you quoted. Nothing was dropped: every row is in `recon.json` with its `party` field.

| Finding | Count |
|---|---|
| API-looking endpoints | 168 |
|   ...of those, first-party | 167 |
|   ...of those, third-party SDK | 1 |
|   ...of those, unresolved base | 0 |
| Other URLs / paths | 0 |
| GraphQL operations | 0 |
| Secret candidates | 0 |
| DOM-XSS sink sites | 0 |

## 1. Hardcoded secrets & credentials

_No secret candidates above the configured thresholds._

## 2. API endpoints

| Endpoint | Party | Method(s) | Client | Request parts | Hits | File:Line |
|---|---|---|---|---|---|---|
| `/admin/users/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:277 |
| `/api-keys/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body, auth | 3 | `fetch-client.js`:522 |
| `/assets/${encodeURIComponent(id)}/edits` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:716 |
| `/auth/pin-code` | first | DELETE, POST, PUT | - | body | 3 | `fetch-client.js`:912 |
| `/libraries/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:1213 |
| `/memories/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:1339 |
| `/notifications/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:1419 |
| `/partners/${encodeURIComponent(id)}` | first | DELETE, POST, PUT | - | body | 3 | `fetch-client.js`:1523 |
| `/people` | first | DELETE, POST, PUT | - | body | 3 | `fetch-client.js`:1551 |
| `/people/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:1605 |
| `/server/license` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:1948 |
| `/sessions` | first | DELETE, POST | - | body | 3 | `fetch-client.js`:2031 |
| `/shared-links/${encodeURIComponent(id)}` | first | DELETE, PATCH | - | body | 3 | `fetch-client.js`:2131 |
| `/stacks/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:2208 |
| `/sync/ack` | first | DELETE, POST | - | body | 3 | `fetch-client.js`:2244 |
| `/tags` | first | POST, PUT | - | body | 3 | `fetch-client.js`:2350 |
| `/tags/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:2388 |
| `/users/me/license` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:2550 |
| `/users/me/onboarding` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:2577 |
| `/workflows/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 3 | `fetch-client.js`:2708 |
| `/admin/config` | first | PUT | - | body | 2 | `fetch-client.js`:74 |
| `/admin/database-backups` | first | DELETE | - | body | 2 | `fetch-client.js`:100 |
| `/admin/users/${encodeURIComponent(id)}/preferences` | first | PUT | - | body | 2 | `fetch-client.js`:317 |
| `/albums/${encodeURIComponent(id)}` | first | DELETE, PATCH | - | body | 2 | `fetch-client.js`:406 |
| `/albums/${encodeURIComponent(id)}/assets` | first | DELETE, PUT | - | body | 2 | `fetch-client.js`:436 |
| `/api` | first | ? | - | headers | 2 | `fetch-client.js`:11 |
| `/api-keys` | first | POST | - | body, auth | 2 | `fetch-client.js`:496 |
| `/asset-files/${encodeURIComponent(id)}` | first | DELETE | - | - | 2 | `fetch-client.js`:572 |
| `/assets` | first | DELETE, PUT | - | body | 2 | `fetch-client.js`:597 |
| `/assets/${encodeURIComponent(id)}/metadata` | first | PUT | - | body | 2 | `fetch-client.js`:743 |
| `/assets/metadata` | first | DELETE, PUT | - | body | 2 | `fetch-client.js`:663 |
| `/cluster-groups/${encodeURIComponent(id)}/requests` | first | PUT | - | body | 2 | `fetch-client.js`:1022 |
| `/duplicates` | first | DELETE | - | body | 2 | `fetch-client.js`:1090 |
| `/faces/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 2 | `fetch-client.js`:1147 |
| `/jobs` | first | POST | - | body | 2 | `fetch-client.js`:1167 |
| `/libraries` | first | POST | - | body | 2 | `fetch-client.js`:1195 |
| `/memories/${encodeURIComponent(id)}/assets` | first | DELETE, PUT | - | body | 2 | `fetch-client.js`:1366 |
| `/notifications` | first | DELETE, PUT | - | body | 2 | `fetch-client.js`:1386 |
| `/queues/${encodeURIComponent(name)}` | first | PUT | - | body | 2 | `fetch-client.js`:1741 |
| `/sessions/${encodeURIComponent(id)}` | first | DELETE, PUT | - | body | 2 | `fetch-client.js`:2058 |
| `/shared-links/${encodeURIComponent(id)}/assets` | first | DELETE, PUT | - | body | 2 | `fetch-client.js`:2158 |
| `/stacks` | first | DELETE, POST | - | body | 2 | `fetch-client.js`:2178 |
| `/system-config` | first | PUT | - | body | 2 | `fetch-client.js`:2282 |
| `/system-metadata/admin-onboarding` | first | POST | - | body | 2 | `fetch-client.js`:2316 |
| `/tags/${encodeURIComponent(id)}/assets` | first | DELETE, PUT | - | body | 2 | `fetch-client.js`:2415 |
| `/users/me` | first | PUT | - | body | 2 | `fetch-client.js`:2520 |
| `/users/me/preferences` | first | PUT | - | body | 2 | `fetch-client.js`:2604 |
| `/users/profile-image` | first | DELETE, POST | - | body | 2 | `fetch-client.js`:2622 |
| `/activities` | first | POST | - | body | 1 | `fetch-client.js`:35 |
| `/activities/${encodeURIComponent(id)}` | first | DELETE | - | - | 1 | `fetch-client.js`:56 |
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
| `/albums` | first | POST | - | body | 1 | `fetch-client.js`:378 |
| `/albums/${encodeURIComponent(id)}/users` | first | PUT | - | body | 1 | `fetch-client.js`:486 |
| `/albums/assets` | first | PUT | - | body | 1 | `fetch-client.js`:388 |
| `/albums/statistics` | first | ? | - | - | 1 | `fetch-client.js`:398 |
| `/api-keys/${encodeURIComponent(id)}/rotate` | first | POST | - | - | 1 | `fetch-client.js`:549 |
| `/api-keys/me` | first | ? | - | - | 1 | `fetch-client.js`:514 |
| `/asset-files/${encodeURIComponent(id)}/download` | first | ? | - | - | 1 | `fetch-client.js`:589 |
| `/assets/${encodeURIComponent(id)}` | first | PUT | - | body | 1 | `fetch-client.js`:706 |
| `/assets/${encodeURIComponent(id)}/ocr` | first | ? | - | - | 1 | `fetch-client.js`:778 |
| `/assets/${id}/original` | first | ? | - | - | 1 | `index.js`:55 |
| `/assets/${id}/original` | first | ? | - | - | 1 | `index.js`:55 |
| `/assets/${id}/thumbnail` | first | ? | - | - | 1 | `index.js`:56 |
| `/assets/${id}/thumbnail` | first | ? | - | - | 1 | `index.js`:56 |
| `/assets/${id}/video/playback` | first | ? | - | - | 1 | `index.js`:57 |
| `/assets/${id}/video/playback` | first | ? | - | - | 1 | `index.js`:57 |
| `/assets/bulk-upload-check` | first | POST | - | body | 1 | `fetch-client.js`:633 |
| `/assets/copy` | first | PUT | - | body | 1 | `fetch-client.js`:643 |
| `/assets/jobs` | first | POST | - | body | 1 | `fetch-client.js`:653 |
| `/auth/admin-sign-up` | first | POST | - | body | 1 | `fetch-client.js`:873 |
| `/auth/change-password` | first | POST | - | body | 1 | `fetch-client.js`:883 |
| `/auth/login` | first | POST | - | body | 1 | `fetch-client.js`:893 |
| `/auth/logout` | first | POST | - | - | 1 | `fetch-client.js`:903 |
| `/auth/session/lock` | first | POST | - | - | 1 | `fetch-client.js`:942 |
| `/auth/session/unlock` | first | POST | - | body | 1 | `fetch-client.js`:951 |
| `/auth/status` | first | ? | - | - | 1 | `fetch-client.js`:961 |
| `/auth/validateToken` | first | POST | - | - | 1 | `fetch-client.js`:969 |
| `/cluster-groups/${encodeURIComponent(id)}/leave` | first | POST | - | - | 1 | `fetch-client.js`:1004 |
| `/cluster-groups/${encodeURIComponent(id)}/regenerate-people` | first | POST | - | - | 1 | `fetch-client.js`:1013 |
| `/cluster-groups/${encodeURIComponent(id)}/users` | first | ? | - | - | 1 | `fetch-client.js`:1040 |
| `/cluster-groups/requests` | first | ? | - | - | 1 | `fetch-client.js`:978 |
| `/cluster-groups/requests/${encodeURIComponent(id)}` | first | DELETE | - | - | 1 | `fetch-client.js`:986 |
| `/cluster-groups/requests/${encodeURIComponent(id)}/accept` | first | POST | - | - | 1 | `fetch-client.js`:995 |
| `/config` | first | ? | - | - | 1 | `fetch-client.js`:1048 |
| `/config/defaults` | first | ? | - | - | 1 | `fetch-client.js`:1056 |
| `/duplicates/${encodeURIComponent(id)}` | first | DELETE | - | - | 1 | `fetch-client.js`:1118 |
| `/duplicates/resolve` | first | POST | - | body | 1 | `fetch-client.js`:1108 |
| `/faces` | first | POST | - | body | 1 | `fetch-client.js`:1137 |
| `/jobs/${encodeURIComponent(name)}` | first | PUT | - | body | 1 | `fetch-client.js`:1185 |
| `/libraries/${encodeURIComponent(id)}/scan` | first | POST | - | - | 1 | `fetch-client.js`:1240 |
| `/libraries/${encodeURIComponent(id)}/statistics` | first | ? | - | - | 1 | `fetch-client.js`:1249 |
| `/libraries/${encodeURIComponent(id)}/validate` | first | POST | - | body | 1 | `fetch-client.js`:1257 |
| `/memories` | first | POST | - | body | 1 | `fetch-client.js`:1311 |
| `/oauth/authorize` | first | POST | - | body | 1 | `fetch-client.js`:1446 |
| `/oauth/backchannel-logout` | first | POST | - | body | 1 | `fetch-client.js`:1456 |
| `/oauth/callback` | first | POST | - | body | 1 | `fetch-client.js`:1466 |
| `/oauth/link` | first | POST | - | body | 1 | `fetch-client.js`:1476 |
| `/oauth/mobile-redirect` | first | ? | - | - | 1 | `fetch-client.js`:1486 |
| `/oauth/unlink` | first | POST | - | - | 1 | `fetch-client.js`:1494 |
| `/partners` | first | POST | - | body | 1 | `fetch-client.js`:1513 |
| `/people/${encodeURIComponent(id)}/merge` | first | POST | - | body | 1 | `fetch-client.js`:1632 |
| `/people/${encodeURIComponent(id)}/reassign` | first | PUT | - | body | 1 | `fetch-client.js`:1642 |
| `/people/${encodeURIComponent(id)}/statistics` | first | ? | - | - | 1 | `fetch-client.js`:1652 |
| `/people/${encodeURIComponent(id)}/thumbnail` | first | ? | - | - | 1 | `fetch-client.js`:1660 |
| `/people/${personId}/thumbnail` | first | ? | - | - | 1 | `index.js`:59 |
| `/people/${personId}/thumbnail` | first | ? | - | - | 1 | `index.js`:59 |
| `/people/merge` | first | POST | - | body | 1 | `fetch-client.js`:1595 |
| `/plugins/${encodeURIComponent(id)}` | first | ? | - | - | 1 | `fetch-client.js`:1709 |
| `/plugins/templates` | first | ? | - | - | 1 | `fetch-client.js`:1701 |
| `/public/config` | first | ? | - | - | 1 | `fetch-client.js`:1717 |
| `/public/config/defaults` | first | ? | - | - | 1 | `fetch-client.js`:1725 |
| `/queues` | first | ? | - | - | 1 | `fetch-client.js`:1733 |
| `/queues/${encodeURIComponent(name)}/jobs` | first | DELETE | - | body | 1 | `fetch-client.js`:1759 |
| `/search/cities` | first | ? | - | - | 1 | `fetch-client.js`:1779 |
| `/search/explore` | first | ? | - | - | 1 | `fetch-client.js`:1787 |
| `/search/random` | first | POST | - | body | 1 | `fetch-client.js`:1870 |
| `/search/smart` | first | POST | - | body | 1 | `fetch-client.js`:1880 |
| `/search/statistics` | first | POST | - | body | 1 | `fetch-client.js`:1890 |
| `/server/about` | first | ? | - | - | 1 | `fetch-client.js`:1916 |
| `/server/apk-links` | first | ? | - | - | 1 | `fetch-client.js`:1924 |
| `/server/config` | first | ? | - | - | 1 | `fetch-client.js`:1932 |
| `/server/features` | first | ? | - | - | 1 | `fetch-client.js`:1940 |
| `/server/media-types` | first | ? | - | - | 1 | `fetch-client.js`:1975 |
| `/server/ping` | first | ? | - | - | 1 | `fetch-client.js`:1983 |
| `/server/statistics` | first | ? | - | - | 1 | `fetch-client.js`:1991 |
| `/server/storage` | first | ? | - | - | 1 | `fetch-client.js`:1999 |
| `/server/version` | first | ? | - | - | 1 | `fetch-client.js`:2007 |
| `/server/version-check` | first | ? | - | - | 1 | `fetch-client.js`:2015 |
| `/server/version-history` | first | ? | - | - | 1 | `fetch-client.js`:2023 |
| `/sessions/${encodeURIComponent(id)}/lock` | first | POST | - | - | 1 | `fetch-client.js`:2077 |
| `/shared-links` | first | POST | - | body | 1 | `fetch-client.js`:2097 |
| `/sync/stream` | first | POST | - | body | 1 | `fetch-client.js`:2272 |
| `/system-config/defaults` | first | ? | - | - | 1 | `fetch-client.js`:2300 |
| `/system-config/storage-template-options` | first | ? | - | - | 1 | `fetch-client.js`:2308 |
| `/system-metadata/reverse-geocoding-state` | first | ? | - | - | 1 | `fetch-client.js`:2334 |
| `/system-metadata/version-check-state` | first | ? | - | - | 1 | `fetch-client.js`:2342 |
| `/tags/assets` | first | PUT | - | body | 1 | `fetch-client.js`:2378 |
| `/trash/empty` | first | POST | - | - | 1 | `fetch-client.js`:2484 |
| `/trash/restore` | first | POST | - | - | 1 | `fetch-client.js`:2493 |
| `/trash/restore/assets` | first | POST | - | body | 1 | `fetch-client.js`:2502 |
| `/users` | first | ? | - | - | 1 | `fetch-client.js`:2512 |
| `/users/${encodeURIComponent(id)}` | first | ? | - | - | 1 | `fetch-client.js`:2641 |
| `/users/${encodeURIComponent(id)}/profile-image` | first | ? | - | - | 1 | `fetch-client.js`:2649 |
| `/users/${userId}/profile-image` | first | ? | - | - | 1 | `index.js`:58 |
| `/users/${userId}/profile-image` | first | ? | - | - | 1 | `index.js`:58 |
| `/view/folder/unique-paths` | first | ? | - | - | 1 | `fetch-client.js`:2667 |
| `/workflows` | first | POST | - | body | 1 | `fetch-client.js`:2690 |
| `/workflows/${encodeURIComponent(id)}/share` | first | ? | - | - | 1 | `fetch-client.js`:2747 |
| `/workflows/triggers` | first | ? | - | - | 1 | `fetch-client.js`:2700 |
| `https://www.npmjs.com/package/oazapfts` | third | ? | - | headers | 1 | `fetch-client.js`:5 |

### Other URLs and paths

_None._

## 3. GraphQL operations

_None found._

## 4. DOM-XSS sinks

_None found._

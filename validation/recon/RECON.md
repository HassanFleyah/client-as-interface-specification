# JavaScript Recon Report

- **Source:** `validation\js-loot\js`
- **Generated:** 2026-10-01 19:09:09
- **Files analysed:** 986 (24,564,597 bytes)

- **First-party domains:** `jellyfin.org`
- **Denominator:** 588 total · 438 first-party · 149 third-party SDK · 1 unresolved base
- **API-shaped only:** 73 total · 65 first-party · 8 third-party SDK · 0 unresolved base
- Quote coverage against the **first-party** number, and say which number you quoted. Nothing was dropped: every row is in `recon.json` with its `party` field.

| Finding | Count |
|---|---|
| API-looking endpoints | 73 |
|   ...of those, first-party | 65 |
|   ...of those, third-party SDK | 8 |
|   ...of those, unresolved base | 0 |
| Other URLs / paths | 515 |
| GraphQL operations | 0 |
| Secret candidates | 225 |
| DOM-XSS sink sites | 264 |

## 1. Hardcoded secrets & credentials

### MEDIUM (7)

| Rule | Variable | Value (redacted) | Entropy | File | Line |
|---|---|---|---|---|---|
| Generic secret assignment | `api_key` | `.conca...,t+=` | 3.52 | `node_modules.jellyfin-apiclient.bundle.js` | 2 |
| Generic secret assignment | `credentials` | `same-origin` | 3.28 | `libraries\subtitles-octopus-worker-legacy.js` | 1 |
| Generic secret assignment | `credentials` | `same-origin` | 3.28 | `libraries\subtitles-octopus-worker.js` | 1 |
| Generic secret assignment | `credentials` | `same-origin` | 3.28 | `libraries\worker-bundle.js` | 2 |
| Generic secret assignment | `credentials` | `same-origin` | 3.28 | `main.jellyfin.bundle.js` | 2 |
| Generic secret assignment | `credentials` | `same-origin` | 3.28 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Generic secret assignment | `credentials` | `same-origin` | 3.28 | `node_modules.jellyfin-apiclient.bundle.js` | 2 |

<details><summary><code>Generic secret assignment</code> @ node_modules.jellyfin-apiclient.bundle.js:2</summary>

```js
"emby/socket","embywebsocket"),t=m(t,"https:","wss:"),t=m(t,"http:","ws:"),t+="?api_key=".concat(e),t+="&deviceId=".concat(this.deviceId()),console.log("opening web socket with url: ".
```
</details>

<details><summary><code>Generic secret assignment</code> @ libraries\subtitles-octopus-worker-legacy.js:1</summary>

```js
unction"==typeof fetch&&!isFileURI(wasmBinaryFile))return fetch(wasmBinaryFile,{credentials:"same-origin"}).then((function(A){if(!A.ok)throw"failed to load wasm binary file at '"+wasmBi
```
</details>

<details><summary><code>Generic secret assignment</code> @ libraries\subtitles-octopus-worker.js:1</summary>

```js
unction"==typeof fetch&&!isFileURI(wasmBinaryFile))return fetch(wasmBinaryFile,{credentials:"same-origin"}).then((function(e){if(!e.ok)throw"failed to load wasm binary file at '"+wasmBi
```
</details>

<details><summary><code>Generic secret assignment</code> @ libraries\worker-bundle.js:2</summary>

```js
n function(e){if(!w&&(c||d)){if("function"==typeof fetch&&!Y(e))return fetch(e,{credentials:"same-origin"}).then((r=>{if(!r.ok)throw"failed to load wasm binary file at '"+e+"'";return r
```
</details>

<details><summary><code>Generic secret assignment</code> @ main.jellyfin.bundle.js:2</summary>

```js
son"===e.dataType&&(t.accept="application/json");var n={headers:t,method:e.type,credentials:"same-origin"},r=e.contentType;e.data&&("string"==typeof e.data?n.body=e.data:(n.body=o(e.dat
```
</details>

<details><summary><code>Generic secret assignment</code> @ node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js:1</summary>

```js
tart=self.performance.now();var s=function(e,t){var r={method:"GET",mode:"cors",credentials:"same-origin",signal:t,headers:new self.Headers(a({},e.headers))};return e.rangeEnd&&r.header
```
</details>

<details><summary><code>Generic secret assignment</code> @ node_modules.jellyfin-apiclient.bundle.js:2</summary>

```js
tion w(e,t,r){return new Promise((function(n,i){var o=setTimeout(i,r);(t=t||{}).credentials="same-origin",fetch(e,t).then((function(e){clearTimeout(o),n(e)})).catch((function(e){clearTi
```
</details>

### LOW (218)

| Rule | Variable | Value (redacted) | Entropy | File | Line |
|---|---|---|---|---|---|
| Internal host / private IP | `-` | `timeZo...test` | 3.26 | `81682.2fcce69da4ca7cd56c6a.chunk.js` | 1 |
| Internal host / private IP | `-` | `timeZo...test` | 3.26 | `node_modules.date-fns.esm.bundle.js` | 1 |
| Internal host / private IP | `-` | `linkify.test` | 3.25 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `this.i...rnal` | 3.24 | `node_modules.@remix-run.router.bundle.js` | 2 |
| Internal host / private IP | `-` | `http:/...host` | 3.2 | `node_modules.@jellyfin.sdk.bundle.js` | 2 |
| Internal host / private IP | `-` | `http:/...host` | 3.2 | `node_modules.axios.bundle.js` | 2 |
| Internal host / private IP | `-` | `rnames...test` | 3.19 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `z.internal` | 3.12 | `networking.00621ef246e29e594e41.chunk.js` | 1 |
| Internal host / private IP | `-` | `CHILD.test` | 3.12 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `mailto.test` | 3.03 | `node_modules.linkify-it.266387235d0d805c1962.chunk.js` | 1 |
| Internal host / private IP | `-` | `a.internal` | 2.92 | `networking.00621ef246e29e594e41.chunk.js` | 1 |
| Internal host / private IP | `-` | `e.internal` | 2.92 | `networking.00621ef246e29e594e41.chunk.js` | 1 |
| Internal host / private IP | `-` | `e.internal` | 2.92 | `node_modules.@remix-run.router.bundle.js` | 2 |
| Internal host / private IP | `-` | `a.internal` | 2.92 | `node_modules.react-router-dom.bundle.js` | 2 |
| Internal host / private IP | `-` | `needsC...test` | 2.91 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `protot...test` | 2.81 | `node_modules.dompurify.bundle.js` | 2 |
| Internal host / private IP | `-` | `protot...test` | 2.81 | `node_modules.linkify-it.266387235d0d805c1962.chunk.js` | 1 |
| Internal host / private IP | `-` | `localhost` | 2.73 | `chromecastPlayer-plugin.22f3e0fb29fa08af7bd7.chunk.js` | 1 |
| Internal host / private IP | `-` | `localhost` | 2.73 | `main.jellyfin.bundle.js` | 2 |
| Internal host / private IP | `-` | `localhost` | 2.73 | `node_modules.core-js.bundle.js` | 1 |
| Internal host / private IP | `-` | `bool.test` | 2.73 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `localhost` | 2.73 | `node_modules.linkify-it.266387235d0d805c1962.chunk.js` | 1 |
| Internal host / private IP | `-` | `boston.test` | 2.66 | `libraries\subtitles-octopus-worker-legacy.js` | 1 |
| Internal host / private IP | `-` | `boston.test` | 2.66 | `libraries\subtitles-octopus-worker.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ar-json.c7d0bcd3c951b26aaf8e.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `be-by-json.5136177f84cd0f2692f6.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `bg-bg-json.a3958d06385f14d8c0f8.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `bs-json.888af1fec5132e054bd9.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ca-json.9cf66fd9ab1691865e13.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `cs-json.b38ca5a1ae26d3c78945.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `da-json.8c7096bd37a47ffe76d5.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `de-json.197d7f9a2769b47d7f9b.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `el-json.8b3e021a636589754c39.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `en-gb-json.ae23385fe3db09546776.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `en-us-json.45f09214281c189457b1.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `eo-json.0e4eddd23d5f6229ebe0.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `es-ar-json.742685c313a61fbd889d.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `es-json.a88be5075063eb0230fe.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `es-mx-json.a3b33d9dd2c82f6aea43.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `es_419-json.d35ca79fd24dd46990e9.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `et-json.7d10b3b61e0abbf2ba3b.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `eu-json.d525eac32aa449292365.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `fa-json.e117df5db7e439b9bb32.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `fi-json.099a8d5c74a5f360df6d.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `fil-json.ab6ec9d05b7d30d6a1db.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `fo-json.6b60bc20642e180402f9.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `fr-ca-json.80bffb6b2565c55f7f17.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ga-json.6897f2d0334cdec5a475.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `he-json.5be4d08a67cc40bfb349.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `hr-json.5f4cf15fb30914445449.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `hu-json.05f4e4b31a982d066659.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `hy-json.ec590cba937b6d04b6c7.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `id-json.d3cccb38ab9c5417a044.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `is-is-json.fa6a22a9e4fbacb2f178.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `it-json.d07d888067b47a984e4b.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ja-json.54d3b40411ed025a5c6b.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ka-json.04a3073679855d1739fa.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `kk-json.12b6d61073c6882b4180.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ko-json.fd55c75f905f535d0cc5.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `lt-lt-json.0eee5fb08e6deeb85238.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `lv-json.37659dbd851100b3736f.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ml-json.bf01787e06468e2a1c1d.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `mn-json.0ff71a4da32ae77bd02a.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `nb-json.7237dfe8ad0c3fed595d.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `nl-json.f3e1a929551f6a04662f.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `nn-json.e72736a65a96d03929f0.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `pl-json.09ce1692fa30fb58bd97.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `pt-br-json.8546ed310415ca42ce04.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `pt-json.baef342e82e433c2a677.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `pt-pt-json.b33dd797e363cdceacfc.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ro-json.05ff981de9bd7c1cf7a6.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ru-json.bdef797046f4224d8f8a.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `sk-json.fa7b2a2f2d5cd17bf53e.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `sl-si-json.82c6692656179f2924b8.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `sr-json.6eac79c8c490c60a9ea7.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `sv-json.e5ae235d18d612ebcc5c.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ta-json.50ed6fe09ec0c3641ce7.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `te-json.e527668a0195c20113dd.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `tr-json.b4ec0bff4a109d111559.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `uk-json.a62f56f89f2545693fc6.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `ur_PK-json.c6bc6718d3a64da2c938.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `vi-json.375fb1e9c01b208d4528.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `zh-cn-json.ef424cbe681c8d85c742.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `zh-hk-json.bf97bbc64405ed5689ea.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.16....100` | 2.57 | `zh-tw-json.d45af8d193709928584e.chunk.js` | 1 |
| Internal host / private IP | `-` | `gi.test` | 2.52 | `libraries\pdf.worker.js` | 2 |
| Internal host / private IP | `-` | `dr.test` | 2.52 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `Wr.test` | 2.52 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `Pn.test` | 2.52 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `Zo.test` | 2.52 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `gi.test` | 2.52 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `hl.test` | 2.52 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `pl.test` | 2.52 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `pretest.test` | 2.36 | `node_modules.linkify-it.266387235d0d805c1962.chunk.js` | 1 |
| Internal host / private IP | `-` | `192.168.1.1` | 2.3 | `fr-json.8383b4e2107aea4df8f0.chunk.js` | 1 |
| Internal host / private IP | `-` | `http.test` | 2.28 | `node_modules.linkify-it.266387235d0d805c1962.chunk.js` | 1 |
| Internal host / private IP | `-` | `l.test` | 2.25 | `1133.bundle.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `1133.bundle.js` | 2 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `1133.bundle.js` | 2 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `67734.f5a6f7c78346909ea9ca.chunk.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `70712.9c36c0bc25d212f7dfd1.chunk.js` | 1 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `70712.9c36c0bc25d212f7dfd1.chunk.js` | 1 |
| Internal host / private IP | `-` | `l.test` | 2.25 | `78701.d06a72f873e03eaaa404.chunk.js` | 1 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `78701.d06a72f873e03eaaa404.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `78701.d06a72f873e03eaaa404.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `85401.7a16f94bd4b18fe0ff55.chunk.js` | 1 |
| Internal host / private IP | `-` | `u.test` | 2.25 | `85401.7a16f94bd4b18fe0ff55.chunk.js` | 1 |
| Internal host / private IP | `-` | `o.test` | 2.25 | `85401.7a16f94bd4b18fe0ff55.chunk.js` | 1 |
| Internal host / private IP | `-` | `c.test` | 2.25 | `98610.e621f71280a871f60c2c.chunk.js` | 1 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `98610.e621f71280a871f60c2c.chunk.js` | 1 |
| Internal host / private IP | `-` | `u.test` | 2.25 | `98610.e621f71280a871f60c2c.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `98610.e621f71280a871f60c2c.chunk.js` | 1 |
| Internal host / private IP | `-` | `p.test` | 2.25 | `blurhash.worker.bundle.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `comicsPlayer-plugin.c358c35860fc41e92b05.chunk.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `libraries\pdf.worker.js` | 2 |
| Internal host / private IP | `-` | `g.test` | 2.25 | `libraries\pdf.worker.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `libraries\subtitles-octopus-worker-legacy.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `libraries\subtitles-octopus-worker.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `main.jellyfin.bundle.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.@jellyfin.sdk.bundle.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.@mui.material.bundle.js` | 1 |
| Internal host / private IP | `-` | `c.test` | 2.25 | `node_modules.@mui.x-date-pickers.6abcdebd9403e77c393a.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.@popperjs.core.bundle.js` | 1 |
| Internal host / private IP | `-` | `W.test` | 2.25 | `node_modules.@remix-run.router.bundle.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.@xmldom.xmldom.31b21537a7a5efcdbb4e.chunk.js` | 1 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `node_modules.@xmldom.xmldom.31b21537a7a5efcdbb4e.chunk.js` | 1 |
| Internal host / private IP | `-` | `n.test` | 2.25 | `node_modules.axios.bundle.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.axios.bundle.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.core-js.bundle.js` | 1 |
| Internal host / private IP | `-` | `u.test` | 2.25 | `node_modules.core-js.bundle.js` | 1 |
| Internal host / private IP | `-` | `h.test` | 2.25 | `node_modules.core-js.bundle.js` | 1 |
| Internal host / private IP | `-` | `o.test` | 2.25 | `node_modules.core-js.bundle.js` | 1 |
| Internal host / private IP | `-` | `k.test` | 2.25 | `node_modules.date-fns.parse.6f03b3a7f2424df5555f.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `o.test` | 2.25 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `k.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `p.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `F.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `G.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `B.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `U.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `X.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `W.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `z.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `J.test` | 2.25 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.jszip.c4a58cbf99c347b50bc6.chunk.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.libbitsub.16f6cbda1921fa9cb713.chunk.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.linkify-it.266387235d0d805c1962.chunk.js` | 1 |
| Internal host / private IP | `-` | `x.test` | 2.25 | `node_modules.localforage.4b2a2f8b573f0c35e266.chunk.js` | 2 |
| Internal host / private IP | `-` | `r.test` | 2.25 | `node_modules.lodash-es.bundle.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.lodash-es.bundle.js` | 1 |
| Internal host / private IP | `-` | `A.test` | 2.25 | `node_modules.lodash-es.bundle.js` | 1 |
| Internal host / private IP | `-` | `l.test` | 2.25 | `node_modules.lodash-es.bundle.js` | 1 |
| Internal host / private IP | `-` | `g.test` | 2.25 | `node_modules.lodash-es.bundle.js` | 1 |
| Internal host / private IP | `-` | `y.test` | 2.25 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `M.test` | 2.25 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `A.test` | 2.25 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.pdfjs-dist.b983b688d208acfb7ec1.chunk.js` | 2 |
| Internal host / private IP | `-` | `n.test` | 2.25 | `node_modules.pdfjs-dist.b983b688d208acfb7ec1.chunk.js` | 2 |
| Internal host / private IP | `-` | `d.test` | 2.25 | `node_modules.react-dom.bundle.js` | 2 |
| Internal host / private IP | `-` | `u.test` | 2.25 | `node_modules.react-lazy-load-image-component.4c0850deb4bb234feecf.chunk.js` | 1 |
| Internal host / private IP | `-` | `c.test` | 2.25 | `node_modules.react-lazy-load-image-component.4c0850deb4bb234feecf.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.react-lazy-load-image-component.4c0850deb4bb234feecf.chunk.js` | 1 |
| Internal host / private IP | `-` | `l.test` | 2.25 | `node_modules.react-lazy-load-image-component.4c0850deb4bb234feecf.chunk.js` | 1 |
| Internal host / private IP | `-` | `H.test` | 2.25 | `node_modules.react-router-dom.bundle.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.sortablejs.da8670ce4017345f437e.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `node_modules.swiper.eed8ade7c72bcddcaf1e.chunk.js` | 1 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `node_modules.webcomponents.js.bundle.js` | 2 |
| Internal host / private IP | `-` | `o.test` | 2.25 | `search.0b435db6b8a8a2156d0a.chunk.js` | 1 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `search.0b435db6b8a8a2156d0a.chunk.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `search.0b435db6b8a8a2156d0a.chunk.js` | 1 |
| Internal host / private IP | `-` | `De.test` | 2.24 | `node_modules.@remix-run.router.bundle.js` | 2 |
| Internal host / private IP | `-` | `Rs.test` | 2.24 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `Ms.test` | 2.24 | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js` | 1 |
| Internal host / private IP | `-` | `le.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `qe.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `je.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `Se.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `We.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `Ie.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `Qe.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `Ge.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `Ke.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `nn.test` | 2.24 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `re.test` | 2.24 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `ne.test` | 2.24 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `le.test` | 2.24 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `Ne.test` | 2.24 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `De.test` | 2.24 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `Xe.test` | 2.24 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `Ye.test` | 2.24 | `node_modules.markdown-it.577ee674061f4f85a169.chunk.js` | 1 |
| Internal host / private IP | `-` | `127.0.0.1` | 2.2 | `main.jellyfin.bundle.js` | 2 |
| Internal host / private IP | `-` | `Ut.test` | 2.13 | `node_modules.axios.bundle.js` | 2 |
| Internal host / private IP | `-` | `Jt.test` | 2.13 | `node_modules.date-fns.esm.bundle.js` | 1 |
| Internal host / private IP | `-` | `ot.test` | 2.13 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `ht.test` | 2.13 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `gt.test` | 2.13 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `Ct.test` | 2.13 | `node_modules.jquery.bundle.js` | 2 |
| Internal host / private IP | `-` | `kt.test` | 2.13 | `node_modules.jquery.bundle.js` | 2 |

<details><summary><code>Internal host / private IP</code> @ 81682.2fcce69da4ca7cd56c6a.chunk.js:1</summary>

```js
elimiter);if(u.length>2)return a;if(/:/.test(u[0])?t=u[0]:(a.date=u[0],t=u[1],o.timeZoneDelimiter.test(a.date)&&(a.date=e.split(o.timeZoneDelimiter)[0],t=e.substr(a.date.length,e.len
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.date-fns.esm.bundle.js:1</summary>

```js
elimiter);if(r.length>2)return n;if(/:/.test(r[0])?e=r[0]:(n.date=r[0],e=r[1],u.timeZoneDelimiter.test(n.date)&&(n.date=t.split(u.timeZoneDelimiter)[0],e=t.substr(n.date.length,t.len
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.markdown-it.577ee674061f4f85a169.chunk.js:1</summary>

```js
/^<a[>\s]/i.test(t)&&o>0&&o--,te(c.content)&&o++),!(o>0)&&"text"===c.type&&e.md.linkify.test(c.content)){var l=c.content,u=e.md.linkify.match(l),h=[],p=c.level,f=0;u.length
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.@remix-run.router.bundle.js:2</summary>

```js
ion e(t,r,n,a){b(this,e),void 0===a&&(a=!1),this.status=t,this.statusText=r||"",this.internal=a,n instanceof Error?(this.data=n.toString(),this.error=n):this.data=n}));funct
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.@jellyfin.sdk.bundle.js:2</summary>

```js
e instanceof t))throw new TypeError("Cannot call a class as a function")}var p="http://localhost".replace(/\/+$/,""),v=l((function e(t){var n,o=arguments.length>1&&void 0!==arg
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.axios.bundle.js:2</summary>

```js
lobalScope&&"function"==typeof self.importScripts,ot=et&&window.location.href||"http://localhost";function it(e){return it="function"==typeof Symbol&&"symbol"==typeof Symbol.it
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.jquery.bundle.js:2</summary>

```js
s[n++])&&!u.isImmediatePropagationStopped();)u.rnamespace&&!1!==o.namespace&&!u.rnamespace.test(o.namespace)||(u.handleObj=o,u.data=o.data,void 0!==(r=((S.event.special[o.orig
```
</details>

<details><summary><code>Internal host / private IP</code> @ networking.00621ef246e29e594e41.chunk.js:1</summary>

```js
erText:i.Ay.translate("LabelInternalServerUriHelp"),defaultValue:null==z?void 0:z.internal}),(0,l.jsx)(b.A,{sx:{flexGrow:1},name:"ExternalPublishedServerUri",label:i.Ay.t
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.jquery.bundle.js:2</summary>

```js
==e[3])):e[3]&&Z.error(e[0]),e},PSEUDO:function(e){var t,n=!e[6]&&e[2];return z.CHILD.test(e[0])?null:(e[3]?e[2]=e[4]||e[5]||"":n&&B.test(n)&&(t=ce(n,!0))&&(t=n.indexOf("
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.linkify-it.266387235d0d805c1962.chunk.js:1</summary>

```js
Exp("^".concat(e.re.src_email_name,"@").concat(e.re.src_host_strict),"i")),e.re.mailto.test(c)?c.match(e.re.mailto)[0].length:0}}},m="biz|com|edu|gov|net|org|pro|web|xxx|a
```
</details>

<details><summary><code>Internal host / private IP</code> @ networking.00621ef246e29e594e41.chunk.js:1</summary>

```js
erverUri?a.all=null===(w=l.PublishedServerUri)||void 0===w?void 0:w.toString():(a.internal=null===(I=l.InternalPublishedServerUri)||void 0===I?void 0:I.toString(),a.exter
```
</details>

<details><summary><code>Internal host / private IP</code> @ networking.00621ef246e29e594e41.chunk.js:1</summary>

```js
erUriBySubnet=function(e){if(e.all)return["all=".concat(e.all)];var t=[];return e.internal&&t.push("internal=".concat(e.internal)),e.external&&t.push("external=".concat(e
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.@remix-run.router.bundle.js:2</summary>

```js
=e&&"number"==typeof e.status&&"string"==typeof e.statusText&&"boolean"==typeof e.internal&&"data"in e}var ve=["post","put","patch","delete"],me=new Set(ve),ye=["get"].co
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.react-router-dom.bundle.js:2</summary>

```js
"RouteErrorResponse"===a.__type)e[i]=new c.VV(a.status,a.statusText,a.data,!0===a.internal);else if(a&&"Error"===a.__type){if(a.__subType){var u=window[a.__subType];if("f
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.jquery.bundle.js:2</summary>

```js
|[])[0]))return r;c&&(n=n.parentNode),e=e.slice(a.shift().value.length)}for(o=z.needsContext.test(e)?0:a.length;o--&&(s=a[o],!t.relative[u=s.type]);)if((l=t.find[u])&&(i=l(s.mat
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.dompurify.bundle.js:2</summary>

```js
pe.replace),S=k(String.prototype.indexOf),w=k(String.prototype.trim),_=k(RegExp.prototype.test),x=(g=TypeError,function(){for(var e=arguments.length,t=new Array(e),n=0;n<e;n+
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.linkify-it.266387235d0d805c1962.chunk.js:1</summary>

```js
is},d.prototype.set=function(t){return this.__opts__=i(this.__opts__,t),this},d.prototype.test=function(t){if(!t.length)return!1;var _,e;if(this.re.schema_test.test(t))for((e
```
</details>

<details><summary><code>Internal host / private IP</code> @ chromecastPlayer-plugin.22f3e0fb29fa08af7bd7.chunk.js:1</summary>

```js
[0].ServerId):c.tF.currentApiClient()).serverAddress(),y=new URL(d).hostname,m="localhost"===y||y.startsWith("127.")||"[::1]"===y?o.serverInfo().LocalAddress:d;e=Object.
```
</details>

<details><summary><code>Internal host / private IP</code> @ main.jellyfin.bundle.js:2</summary>

```js
IsInNetwork){if(!t.IsLocal){var n=(e.Path||"").toLowerCase();if(-1!==n.indexOf("localhost")||-1!==n.indexOf("127.0.0.1"))return Promise.resolve(!1)}return Promise.resolv
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.core-js.bundle.js:1</summary>

```js
lse if(""===l){if(f.host="",r)return;s=Ut}else{if(u=f.parseHost(l))return u;if("localhost"===f.host&&(f.host=""),r)return;l="",s=Ut}continue}l+=i;break;case Ut:if(f.isSp
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.jquery.bundle.js:2</summary>

```js
op(e,t,n):(1===o&&S.isXMLDoc(e)||(i=S.attrHooks[t.toLowerCase()]||(S.expr.match.bool.test(t)?wt:void 0)),void 0!==n?null===n?void S.removeAttr(e,t):i&&"set"in i&&void 0!
```
</details>

<details><summary><code>Internal host / private IP</code> @ node_modules.linkify-it.266387235d0d805c1962.chunk.js:1</summary>

```js
=_.tpl_host_no_ip_fuzzy+_.src_port+_.src_host_terminator,_.tpl_host_fuzzy_test="localhost|www\\.|\\.\\d{1,3}\\.|(?:\\.(?:%TLDS%)(?:".concat(_.src_ZPCc,"|>|$))"),_.tpl_em
```
</details>

<details><summary><code>Internal host / private IP</code> @ libraries\subtitles-octopus-worker-legacy.js:1</summary>

```js
n.fasteragents<body 10px 0pragmafridayjuniordollarplacedcoversplugin5,000 page">boston.test(avatartested_countforumsschemaindex,filledsharesreaderalert(appearSubmitline">b
```
</details>

<details><summary><code>Internal host / private IP</code> @ libraries\subtitles-octopus-worker.js:1</summary>

```js
n.fasteragents<body 10px 0pragmafridayjuniordollarplacedcoversplugin5,000 page">boston.test(avatartested_countforumsschemaindex,filledsharesreaderalert(appearSubmitline">b
```
</details>

<details><summary><code>Internal host / private IP</code> @ ar-json.c7d0bcd3c951b26aaf8e.chunk.js:1</summary>

```js
gPath":"مسار تسجيل المسلسلات","LabelServerHost":"المضيف","LabelServerHostHelp":"192.168.1.100:8096 أو https://myserver.com","LabelSkipIfAudioTrackPresent":"تخطّي إذا كان مسا
```
</details>

<details><summary><code>Internal host / private IP</code> @ be-by-json.5136177f84cd0f2692f6.chunk.js:1</summary>

```js
мае ніякага эфекту, калі сервер не праслухоўвае HTTPS.","LabelServerHostHelp":"192.168.1.100:8096 або https://myserver.com","LabelServerName":"Назва сервера","LabelServerNa
```
</details>

<details><summary><code>Internal host / private IP</code> @ bg-bg-json.a3958d06385f14d8c0f8.chunk.js:1</summary>

```js
едновременни потоци","LabelServerName":"Име на сървъра","LabelServerHostHelp":"192.168.1.100:8096 или https://myserver.com","LabelServerHost":"Хост","LabelSelectFolderGroup
```
</details>

<details><summary><code>Internal host / private IP</code> @ bs-json.888af1fec5132e054bd9.chunk.js:1</summary>

```js
ath":"Staza snimanja serije","LabelServerHost":"Domaćin","LabelServerHostHelp":"192.168.1.100:8096 ili https://myserver.com","LabelServerName":"Naziv servera","LabelServerNa
```
</details>

<details><summary><code>Internal host / private IP</code> @ ca-json.9cf66fd9ab1691865e13.chunk.js:1</summary>

```js
usConnectionLimit":"Límit de fluxos simultanis de dades","LabelServerHostHelp":"192.168.1.100:8096 o https://myserver.com","LabelServerHost":"Amfitrió","LabelScheduledTaskLa
```
</details>

<details><summary><code>Internal host / private IP</code> @ cs-json.b38ca5a1ae26d3c78945.chunk.js:1</summary>

```js
belSeriesRecordingPath":"Umístění pro nahrávání seriálů","LabelServerHostHelp":"192.168.1.100:8096 nebo https://mujserver.cz","LabelSkipBackLength":"Délka posunu zpět","Labe
```
</details>

<details><summary><code>Internal host / private IP</code> @ da-json.8c7096bd37a47ffe76d5.chunk.js:1</summary>

```js
h":"Serieoptagelsessti","LabelServerHost":"Vært","LabelServerHostHelp":"F. eks: 192.168.1.100:8096 eller https://myserver.com","LabelSimultaneousConnectionLimit":"Begrænsnin
```
</details>

<details><summary><code>Internal host / private IP</code> @ de-json.197d7f9a2769b47d7f9b.chunk.js:1</summary>

```js
h":"Aufnahmepfad für Serien","LabelServerHost":"Adresse","LabelServerHostHelp":"192.168.1.100:8096 oder https://myserver.com","LabelSimultaneousConnectionLimit":"Paralleler
```
</details>

<details><summary><code>Internal host / private IP</code> @ el-json.8b3e021a636589754c39.chunk.js:1</summary>

```js
η","LabelSeriesRecordingPath":"Διαδρομή εγγραφής σειρών","LabelServerHostHelp":"192.168.1.100:8096 ή https://myserver.com","LabelSkipBackLength":"Παράλειψη προς τα πίσω","La
```
</details>

<details><summary><code>Internal host / private IP</code> @ en-gb-json.ae23385fe3db09546776.chunk.js:1</summary>

```js
lTunerType":"Tuner type","LabelServerName":"Server name","LabelServerHostHelp":"192.168.1.100:8096 or https://myserver.com","LabelSeriesRecordingPath":"Series recording path
```
</details>

<details><summary><code>Internal host / private IP</code> @ en-us-json.45f09214281c189457b1.chunk.js:1</summary>

```js
ngPath":"Series recording path","LabelServerHost":"Host","LabelServerHostHelp":"192.168.1.100:8096 or https://myserver.com","LabelServerName":"Server name","LabelServerNameH
```
</details>

<details><summary><code>Internal host / private IP</code> @ eo-json.0e4eddd23d5f6229ebe0.chunk.js:1</summary>

```js
ta fonkoloro","LabelStopWhenPossible":"Halti kiam eblas","LabelServerHostHelp":"192.168.1.100:8096 aŭ https://myserver.com","LabelSeriesRecordingPath":"Seria rikordada serĉv
```
</details>

<details><summary><code>Internal host / private IP</code> @ es-ar-json.742685c313a61fbd889d.chunk.js:1</summary>

```js
nes simultáneas","LabelServerName":"Nombre del servidor","LabelServerHostHelp":"192.168.1.100:8096 o https://miservidor.com","LabelServerHost":"Host","LabelSeriesRecordingPa
```
</details>

<details><summary><code>Internal host / private IP</code> @ es-json.a88be5075063eb0230fe.chunk.js:1</summary>

```js
abelSeriesRecordingPath":"Ruta de grabaciones de Series","LabelServerHostHelp":"192.168.1.100:8096 o https://miservidor.com","LabelSimultaneousConnectionLimit":"Límite de tr
```
</details>

<details><summary><code>Internal host / private IP</code> @ es-mx-json.a3b33d9dd2c82f6aea43.chunk.js:1</summary>

```js
las grabaciones de series","LabelServerHost":"Servidor","LabelServerHostHelp":"192.168.1.100:8096 o https://miservidor.com","LabelSimultaneousConnectionLimit":"Límite de tr
```
</details>

<details><summary><code>Internal host / private IP</code> @ es_419-json.d35ca79fd24dd46990e9.chunk.js:1</summary>

```js
nes simultáneas","LabelServerName":"Nombre del servidor","LabelServerHostHelp":"192.168.1.100:8096 o https://miservidor.com","LabelServerHost":"Servidor","LabelSeriesRecordi
```
</details>

> Verify each candidate before reporting: a public/anon key (Firebase apiKey, Stripe pk_, Sentry DSN, Algolia search key) is by design client-side and is normally **not** a vulnerability. What matters is whether the key grants privileged access.

## 2. API endpoints

| Endpoint | Party | Method(s) | Client | Request parts | Hits | File:Line |
|---|---|---|---|---|---|---|
| `/dashboard/users/` | first | ? | - | - | 7 | `activity.3f7371ceea7d76fda9a7.chunk.js`:1 |
| `/dashboard/settings` | first | ? | - | - | 4 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/login` | first | ? | - | - | 4 | `main.jellyfin.bundle.js`:2 |
| `/profile` | first | ? | - | - | 4 | `activity.3f7371ceea7d76fda9a7.chunk.js`:1 |
| `/Playlists/{playlistId}/Users/{userId}` | first | GET, DELETE, POST | - | headers, auth | 3 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/dashboard/devices` | first | ? | - | - | 3 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/libraries` | first | ? | - | - | 3 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/playback/transcoding` | first | ? | - | - | 3 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/plugins` | first | ? | - | - | 3 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/plugins/repositories` | first | ? | - | - | 3 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/tasks` | first | ? | - | - | 3 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/users` | first | ? | - | - | 3 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/Auth/Keys` | first | ? | - | - | 2 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Download` | first | ? | - | - | 2 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Password` | first | ? | - | - | 2 | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Sessions/{sessionId}/User/{userId}` | first | POST, DELETE | - | headers, auth | 2 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users` | first | ? | - | - | 2 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/` | first | GET? | axios | query-params | 2 | `main.jellyfin.bundle.js`:2 |
| `/Users/{userId}` | first | DELETE, GET | - | headers, auth | 2 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/dashboard` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/backups` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/branding` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/libraries/display` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/libraries/metadata` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/libraries/nfo` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/livetv` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/livetv/tuner` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/networking` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/playback/resume` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/playback/streaming` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/playback/trickplay` | first | ? | - | - | 2 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/search` | first | GET | - | - | 2 | `78701.d06a72f873e03eaaa404.chunk.js`:1 |
| `/Auth/Keys/{key}` | first | DELETE | - | headers, auth | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Auth/PasswordResetProviders` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Auth/Providers` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/ClientLog/Document` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Download` | first | GET | - | headers, auth | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/File` | first | GET | - | headers, auth | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Playlists/{playlistId}/Users` | first | GET | - | headers, auth | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/RemoteImages/Download` | first | ? | - | - | 1 | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Sessions/Logout` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/AuthenticateByName` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/AuthenticateWithQuickConnect` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/Configuration` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/ForgotPassword` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/ForgotPassword/Pin` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/Me` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/New` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/Password` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/Public` | first | ? | - | - | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Users/{userId}/Policy` | first | POST | - | headers, auth | 1 | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/dashboard/activity` | first | ? | - | - | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/keys` | first | ? | - | auth | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/livetv/guide` | first | ? | - | - | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/livetv/recordings` | first | ? | - | - | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/logs` | first | ? | - | - | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/logs/` | first | ? | - | - | 1 | `logs.7eea0ac5ee65a13342ec.chunk.js`:1 |
| `/dashboard/plugins/` | first | ? | - | - | 1 | `plugins.79bfe246fe2f89e392d3.chunk.js`:1 |
| `/dashboard/recordings` | first | ? | - | - | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/tasks/` | first | ? | - | - | 1 | `tasks.02f46ed3a885ee5252cb.chunk.js`:1 |
| `/dashboard/users/:userId/:tab` | first | ? | - | - | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/dashboard/users/add` | first | ? | - | - | 1 | `users.f5b80a5f1b08bc92de28.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/settings` | first | ? | - | - | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/users/` | first | ? | - | - | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/users/adding-managing-users` | first | ? | - | - | 1 | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://www.gstatic.com/cv/js/sender/v1/cast_sender.js` | third | ? | - | - | 2 | `chromecastPlayer-castSenderApi.9464cdc56b94a114d819.chunk.js`:1 |
| `https://reactrouter.com/v6/upgrading/future#v7_fetcherpersist` | third | ? | - | - | 1 | `node_modules.react-router.bundle.js`:2 |
| `https://reactrouter.com/v6/upgrading/future#v7_normalizeformmethod` | third | ? | - | - | 1 | `node_modules.react-router.bundle.js`:2 |
| `https://reactrouter.com/v6/upgrading/future#v7_partialhydration` | third | ? | - | - | 1 | `node_modules.react-router.bundle.js`:2 |
| `https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath` | third | ? | - | - | 1 | `node_modules.react-router.bundle.js`:2 |
| `https://reactrouter.com/v6/upgrading/future#v7_skipactionerrorrevalidation` | third | ? | - | - | 1 | `node_modules.react-router.bundle.js`:2 |
| `https://reactrouter.com/v6/upgrading/future#v7_starttransition` | third | ? | - | - | 1 | `node_modules.react-router.bundle.js`:2 |
| `https://www.openstreetmap.org/search?query=` | third | ? | - | - | 1 | `itemDetails.ea83c659375b31117215.chunk.js`:1 |

### Other URLs and paths

<details><summary>Show 515 entries</summary>

| Value | Kind | File:Line |
|---|---|---|
| `${e.name}/string` | template-literal | `libraries\worker-bundle.js`:2 |
| `/${(0,i.escapePDFName)(e.name)}` | template-path | `libraries\pdf.worker.js`:2 |
| `/./` | relative-path | `node_modules.core-js.bundle.js`:1 |
| `/AdditionalParts` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Albums/{itemId}/Similar` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/AlternateSources` | relative-path | `itemDetails.ea83c659375b31117215.chunk.js`:1 |
| `/Ancestors` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Artists` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Artists/AlbumArtists` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Artists/{itemId}/Similar` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Artists/{name}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Artists/{name}/Images/{imageType}/{imageIndex}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Audio/{itemId}/Lyrics` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Audio/{itemId}/RemoteSearch/Lyrics` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Audio/{itemId}/RemoteSearch/Lyrics/{lyricId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Backup` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Backup/Create` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Backup/Manifest` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Backup/Restore` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Branding/Configuration` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Branding/Css` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Branding/Splashscreen` | relative-path | `32721.fad93419ec89a0acfbfd.chunk.js`:2 |
| `/Channels` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Channels/Features` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Channels/Items/Latest` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Channels/{channelId}/Features` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Channels/{channelId}/Items` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Command` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Configuration` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/ContentType` | relative-path | `26855.ad7a271624659e1f2d6e.chunk.js`:1 |
| `/CriticReviews` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Devices` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Devices/Info` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Devices/Options` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Disable` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/DisplayPreferences/{displayPreferencesId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/EasyPassword` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Enable` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Episodes` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/ExternalIdInfos` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/FallbackFont/Fonts` | relative-path | `htmlVideoPlayer-plugin.75e5631714895cbf4ff3.chunk.js`:2 |
| `/FallbackFont/Fonts/` | relative-path | `htmlVideoPlayer-plugin.75e5631714895cbf4ff3.chunk.js`:2 |
| `/FallbackFont/Fonts/{name}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/FavoriteItems/` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Genres` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Genres/{genreName}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Genres/{name}/Images/{imageType}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Genres/{name}/Images/{imageType}/{imageIndex}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/GetUtcTime` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/GroupingOptions` | relative-path | `user-home.e4ae606b60dda7eefc69.chunk.js`:2 |
| `/Image` | relative-path | `plugins-plugin.f3b592c7af3f85e514ee.chunk.js`:1 |
| `/Images` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Images/` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Images/Primary` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Index` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/InstantMix` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Intros` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Items` | relative-path | `3380.bc7dedf9f3abf676881e.chunk.js`:1 |
| `/Items/` | relative-path | `55802.52fbf988646b0db27075.chunk.js`:2 |
| `/Items/Counts` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/Filters` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/Filters2` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/Latest` | relative-path | `movies-moviesrecommended.6f024cdedc30ed291501.chunk.js`:1 |
| `/Items/Resume` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Items/Root` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Ancestors` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Collections` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Images` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Images/{imageType}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Images/{imageType}/{imageIndex}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Images/{imageType}/{imageIndex}/Index` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Intros` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/LocalTrailers` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/PlaybackInfo` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Refresh` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/RemoteSearch/Subtitles/{language}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/RemoteSearch/Subtitles/{subtitleId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/Similar` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/SpecialFeatures` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/ThemeMedia` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/ThemeSongs` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Items/{itemId}/ThemeVideos` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Libraries/AvailableOptions` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/Media/Updated` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/MediaFolders` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/Movies/Added` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/Movies/Updated` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/PhysicalPaths` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/Refresh` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/Series/Added` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/Series/Updated` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/VirtualFolders` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/VirtualFolders/LibraryOptions` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/VirtualFolders/Name` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/VirtualFolders/Paths` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Library/VirtualFolders/Paths/Update` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveStreams/Close` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveStreams/Open` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/ChannelMappingOptions` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/ChannelMappings` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Channels` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Channels/{channelId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/GuideInfo` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Info` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/ListingProviders` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/ListingProviders/Default` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/ListingProviders/Lineups` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/ListingProviders/SchedulesDirect/Countries` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/LiveRecordings/{recordingId}/stream` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/LiveStreamFiles/{streamId}/stream.{container}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Programs` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Programs/Recommended` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Programs/{programId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Recordings` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Recordings/Folders` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Recordings/{recordingId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/SeriesTimers` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/SeriesTimers/{timerId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Timers` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Timers/Defaults` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Timers/{timerId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/TunerHosts` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/TunerHosts/Types` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Tuners/Discover` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Tuners/Discvover` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LiveTv/Tuners/{tunerId}/Reset` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/LocalTrailers` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Localization/Countries` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Localization/Cultures` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Localization/Options` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Localization/ParentalRatings` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Lyrics` | relative-path | `46634.f6ccb8872278a2ffa676.chunk.js`:1 |
| `/MediaSegments/{itemId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Message` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/MetadataEditor` | relative-path | `26855.ad7a271624659e1f2d6e.chunk.js`:1 |
| `/Move/` | relative-path | `55802.52fbf988646b0db27075.chunk.js`:2 |
| `/Move/0` | relative-path | `55802.52fbf988646b0db27075.chunk.js`:2 |
| `/Movies/Recommendations` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Movies/{itemId}/Similar` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/MusicGenres/{name}/Images/{imageType}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/MusicGenres/{name}/Images/{imageType}/{imageIndex}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Packages` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Packages/Installed/{name}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Packages/Installing/{packageId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Packages/{name}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Persons` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Persons/{name}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Persons/{name}/Images/{imageType}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Persons/{name}/Images/{imageType}/{imageIndex}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Playback/BitrateTest` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/PlaybackInfo` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/PlayedItems/` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Playing` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Playing/` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Playlists` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Playlists/{playlistId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Playlists/{playlistId}/Items` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Playlists/{playlistId}/Items/{itemId}/Move/{newIndex}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Plugins` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Plugins/` | relative-path | `plugins-plugin.f3b592c7af3f85e514ee.chunk.js`:1 |
| `/Plugins/{pluginId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Plugins/{pluginId}/Configuration` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Plugins/{pluginId}/Manifest` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Plugins/{pluginId}/{version}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Plugins/{pluginId}/{version}/Disable` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Plugins/{pluginId}/{version}/Enable` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Plugins/{pluginId}/{version}/Image` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Policy` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Providers/Lyrics/{lyricId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Providers/Subtitles/Subtitles/{subtitleId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/QuickConnect/` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/QuickConnect/Authorize` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/QuickConnect/Connect` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/QuickConnect/Enabled` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/QuickConnect/Initiate` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Rating` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Refresh` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/RemoteImages` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/RemoteImages/Providers` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/RemoteSearch/Subtitles/` | relative-path | `39345.2e097a87c2a50b2c2838.chunk.js`:1 |
| `/Repositories` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Reset` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Reviews` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/ScheduledTasks` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/ScheduledTasks/Running/{taskId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/ScheduledTasks/{taskId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/ScheduledTasks/{taskId}/Triggers` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Seasons` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Sessions` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/Capabilities` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/Capabilities/Full` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/Playing` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/Playing/Ping` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/Playing/Progress` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/Playing/Stopped` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/Viewing` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/{sessionId}/Command` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/{sessionId}/Command/{command}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/{sessionId}/Message` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/{sessionId}/Playing` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/{sessionId}/Playing/{command}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/{sessionId}/System/{command}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Sessions/{sessionId}/Viewing` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Shows/NextUp` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Shows/Upcoming` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Shows/{itemId}/Similar` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Shows/{seriesId}/Episodes` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Shows/{seriesId}/Seasons` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Similar` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/SpecialFeatures` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Status` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Studios` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Studios/{name}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Studios/{name}/Images/{imageType}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Studios/{name}/Images/{imageType}/{imageIndex}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Subtitles` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Subtitles/` | relative-path | `39345.2e097a87c2a50b2c2838.chunk.js`:1 |
| `/Summary` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/SyncPlay/Buffering` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/Join` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/Leave` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/List` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/MovePlaylistItem` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/New` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/NextItem` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/Pause` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/Ping` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/PreviousItem` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/Queue` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/Ready` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/RemoveFromPlaylist` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/Seek` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/SetIgnoreWait` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/SetNewQueue` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/SetPlaylistItem` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/SetRepeatMode` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/SetShuffleMode` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/Stop` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/Unpause` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/SyncPlay/{id}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/ActivityLog/Entries` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Configuration` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Configuration/Branding` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Configuration/MetadataOptions/Default` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Configuration/{key}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Endpoint` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Info` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/System/Info/Public` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/System/Info/Storage` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Logs` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Logs/Log` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Ping` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Restart` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/System/Shutdown` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/ThemeMedia` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Trailers/{itemId}/Similar` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Transferred` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/Trickplay/` | relative-path | `playback-video.7de109744f4737bdf440.chunk.js`:2 |
| `/Triggers` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/UserFavoriteItems/{itemId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/UserImage` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/UserItems/Resume` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/UserItems/{itemId}/Rating` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/UserItems/{itemId}/UserData` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/UserPlayedItems/{itemId}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/UserViews` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/UserViews/GroupingOptions` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Videos/{itemId}/Subtitles` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Videos/{itemId}/Subtitles/{index}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/subtitles.m3u8` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/Stream.{routeFormat}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/{routeStartPositionTicks}/Stream.{routeFormat}` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/Views` | relative-path | `node_modules.jellyfin-apiclient.bundle.js`:2 |
| `/a/b` | relative-path | `blurhash.worker.bundle.js`:1 |
| `/a/i` | relative-path | `node_modules.core-js.bundle.js`:1 |
| `/addserver` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/assets` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/books` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/boxsets` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/configurationpage` | relative-path | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `/details` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/dev` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/dev/null` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/dev/shm` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/dev/shm/tmp` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/dev/stderr` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/dev/stdin` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/dev/stdout` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/dev/tty` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/dev/tty1` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/fonts` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/fonts/.fallback-` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/forgotpassword` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/forgotpasswordpin` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/home` | relative-path | `78701.d06a72f873e03eaaa404.chunk.js`:1 |
| `/home/web_user` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/homevideos` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/index.html` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/index.js` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/libbitsub/libbitsub.js` | relative-path | `node_modules.libbitsub.16f6cbda1921fa9cb713.chunk.js`:2 |
| `/libbitsub/libbitsub_bg.wasm` | relative-path | `node_modules.libbitsub.16f6cbda1921fa9cb713.chunk.js`:2 |
| `/libraries/pdf.worker.js` | relative-path | `pdfPlayer-plugin.0e5794750bc919e9fcd7.chunk.js`:1 |
| `/libraries/subtitles-octopus-worker-legacy.js` | relative-path | `htmlVideoPlayer-plugin.75e5631714895cbf4ff3.chunk.js`:2 |
| `/libraries/subtitles-octopus-worker.js` | relative-path | `htmlVideoPlayer-plugin.75e5631714895cbf4ff3.chunk.js`:2 |
| `/libraries/worker-bundle.js` | relative-path | `comicsPlayer-plugin.c358c35860fc41e92b05.chunk.js`:2 |
| `/list` | relative-path | `78701.d06a72f873e03eaaa404.chunk.js`:1 |
| `/livetv` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/lyrics` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/metadata` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/mixed` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/movies` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/music` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/musicvideos` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/mypreferencesmenu` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/playlists` | relative-path | `8463.5024adce4ba13b0c6c59.chunk.js`:1 |
| `/proc` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/proc/self` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/proc/self/fd` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/queue` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/quickconnect` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/selectserver` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/stream.` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/sub.ass` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/themes` | relative-path | `node_modules.jstree.06059368d3e505ed6e71.chunk.js`:2 |
| `/tmp` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/universal` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/v//////7/////9/` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAAERBAIBEQQC` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAAIiCAACIggAMAAAAwDAAAAG` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAAIiSBQCIkgU` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAAQEEhIEBBIS7p/5///95fOfOQcA//8B` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAATGEAAExhCA` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAABAAYBAQAGAQ` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAABRPUJgUT1AY` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAADQAIAA0ACAAADADAAAAAAAADAAAAwAAYAAAAAAAAIAAAAAAAPDD` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAGEGHAFhBhwB7o/5///95cOPOQEA8P8B` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAI8nPBSPJzwU` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAIAAAACA` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAIAIAACACAAABI///f8B//3/AQSP` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAIBEAAiARAAI` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAIGjDBSBowwUAAAAAAAAAIAB` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAIQAQhCEAEIQAAAAwAAAAwAAAADA` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/v//B/7//wcAAAAAAAAAAMXPEBrFzxCa` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/video` | relative-path | `78701.d06a72f873e03eaaa404.chunk.js`:1 |
| `/wAAAAABAQEAAAIBAgADAQAAAAAAAAAABAEaAAkACQAJAAkABQEa` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/wCHAogCAACJAooC` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/web` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/web/` | relative-path | `55802.52fbf988646b0db27075.chunk.js`:2 |
| `/web/ConfigurationPage` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/web/ConfigurationPages` | relative-path | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `/web/configurationpage` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/wizard/` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/wizard/start` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/wizardfinish` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/wizardlibrary` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/wizardremoteaccess` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/wizardsettings` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/wizardstart` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/wizarduser` | relative-path | `main.jellyfin.bundle.js`:2 |
| `/wrapper` | relative-path | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `/xdp:xdp` | relative-path | `libraries\pdf.worker.js`:2 |
| `http://An` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://Descriptionrelatively` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://In` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://UA-Compatible` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://a` | absolute-url | `node_modules.webcomponents.js.bundle.js`:2 |
| `http://a/c%20d` | absolute-url | `node_modules.webcomponents.js.bundle.js`:2 |
| `http://according` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://addEventListenerresponsible` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://applicationslink` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://ator` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://cript` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://dictionaryperceptionrevolutionfoundationpx` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://ejemplo.com/` | absolute-url | `es-ar-json.742685c313a61fbd889d.chunk.js`:1 |
| `http://eksempel.no/` | absolute-url | `nn-json.e72736a65a96d03929f0.chunk.js`:1 |
| `http://encoding` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://example.com/` | absolute-url | `af-json.f567ef266abedd10318d.chunk.js`:1 |
| `http://exemplo.com/` | absolute-url | `pt-br-json.8546ed310415ca42ce04.chunk.js`:1 |
| `http://familiar` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://fb.me/use-check-prop-types` | absolute-url | `67734.f5a6f7c78346909ea9ca.chunk.js`:2 |
| `http://heading` | template-literal | `libraries\pdf.worker.js`:2 |
| `http://html4/loose.dtd` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://i` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://imEnglish` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://interested` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://interpreted` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://iparticipation` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://jellyfin.ejemplo.com` | absolute-url | `es-ar-json.742685c313a61fbd889d.chunk.js`:1 |
| `http://jellyfin.eksempel.no` | absolute-url | `nn-json.e72736a65a96d03929f0.chunk.js`:1 |
| `http://jellyfin.example.com` | absolute-url | `es-mx-json.a3b33d9dd2c82f6aea43.chunk.js`:1 |
| `http://link` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://localhost` | absolute-url | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `http://mathematicsmargin-top` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://navigation` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://ns.adobe.com/xdp/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://ns.adobe.com/xdp/pdf/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://ns.adobe.com/xfdf/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://ns.adobe.com/xmpmeta/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://option` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://pelda.com/` | absolute-url | `hu-json.05f4e4b31a982d066659.chunk.js`:1 |
| `http://purl.org/dc/elements/1.1/` | absolute-url | `node_modules.epubjs.fc1e2c6aec473df47a5b.chunk.js`:1 |
| `http://px` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://s` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://site_name` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://staticsuggested` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://style` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://w` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://whether` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www-//W3C//DTD` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www./div` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.C//DTD` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.a` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.hortcut` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.icon` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.idpf.org/2007/ops` | absolute-url | `node_modules.epubjs.fc1e2c6aec473df47a5b.chunk.js`:1 |
| `http://www.interpretation` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.language` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.schedulesdirect.org` | absolute-url | `1451.72037c81d39190d14e0f.chunk.js`:1 |
| `http://www.style` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.text-decoration` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.w3.org/1998/Math/MathML` | absolute-url | `node_modules.dompurify.bundle.js`:2 |
| `http://www.w3.org/1999/XSL/Transform` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.w3.org/1999/xhtml` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.w3.org/1999/xlink` | absolute-url | `node_modules.pdfjs-dist.b983b688d208acfb7ec1.chunk.js`:2 |
| `http://www.w3.org/2000/09/xmldsig#` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.w3.org/2000/svg` | absolute-url | `1133.bundle.js`:2 |
| `http://www.w3.org/2000/xmlns/` | absolute-url | `node_modules.@xmldom.xmldom.31b21537a7a5efcdbb4e.chunk.js`:1 |
| `http://www.w3.org/XML/1998/namespace` | absolute-url | `node_modules.@xmldom.xmldom.31b21537a7a5efcdbb4e.chunk.js`:1 |
| `http://www.w3.org/ns/ttml#styling` | absolute-url | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js`:1 |
| `http://www.w3.org/shortcut` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.wencodeURIComponent` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://www.xfa.org/schema/xci/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.xfa.org/schema/xdc/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.xfa.org/schema/xfa-connection-set/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.xfa.org/schema/xfa-data/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.xfa.org/schema/xfa-data/1.0/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.xfa.org/schema/xfa-form/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.xfa.org/schema/xfa-locale-set/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.xfa.org/schema/xfa-source-set/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.xfa.org/schema/xfa-template/` | absolute-url | `libraries\pdf.worker.js`:2 |
| `http://www.years` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `http://xt/css` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `https://a` | absolute-url | `node_modules.core-js.bundle.js`:1 |
| `https://a/c%20d?a=1&c=3` | absolute-url | `node_modules.core-js.bundle.js`:1 |
| `https://aIn` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `https://aomedia.org/emsg/ID3` | absolute-url | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js`:1 |
| `https://d` | absolute-url | `fo-json.6b60bc20642e180402f9.chunk.js`:1 |
| `https://ejemplo.com/` | absolute-url | `es-json.a88be5075063eb0230fe.chunk.js`:1 |
| `https://esempio.com/` | absolute-url | `it-json.d07d888067b47a984e4b.chunk.js`:1 |
| `https://esimerkki.com/` | absolute-url | `fi-json.099a8d5c74a5f360df6d.chunk.js`:1 |
| `https://example.com` | absolute-url | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `https://example.com/` | absolute-url | `ar-json.c7d0bcd3c951b26aaf8e.chunk.js`:1 |
| `https://ffmpeg.org/ffmpeg-all.html#tonemap_005fopencl` | absolute-url | `playback-transcoding.943e8888f8a425d83ca9.chunk.js`:1 |
| `https://github.com/date-fns/date-fns/blob/master/docs/unicodeTokens.md` | absolute-url | `node_modules.date-fns._lib.0bf806a445536aa36201.chunk.js`:1 |
| `https://github.com/date-fns/date-fns/blob/master/docs/upgradeGuide.md#string-arguments` | absolute-url | `10647.0d875f6ca76017c508bf.chunk.js`:1 |
| `https://github.com/jellyfin/jellyfin` | absolute-url | `92974.57b22fb2be1d5695f8d9.chunk.js`:2 |
| `https://github.com/mui/mui-x/issues/new/choose` | absolute-url | `node_modules.@mui.x-date-pickers.6abcdebd9403e77c393a.chunk.js`:1 |
| `https://github.com/zloirock/core-js` | absolute-url | `blurhash.worker.bundle.js`:1 |
| `https://github.com/zloirock/core-js/blob/v3.49.0/LICENSE` | absolute-url | `blurhash.worker.bundle.js`:1 |
| `https://jellyfin.ejemplo.com` | absolute-url | `es-ar-json.742685c313a61fbd889d.chunk.js`:1 |
| `https://jellyfin.eksempel.no` | absolute-url | `nn-json.e72736a65a96d03929f0.chunk.js`:1 |
| `https://jellyfin.example.com` | absolute-url | `es-mx-json.a3b33d9dd2c82f6aea43.chunk.js`:1 |
| `https://jellyfin.example.com.` | absolute-url | `es-mx-json.a3b33d9dd2c82f6aea43.chunk.js`:1 |
| `https://jellyfin.org/docs/general/administration/backup-and-restore/` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/administration/configuration#fonts` | absolute-url | `playback-transcoding.943e8888f8a425d83ca9.chunk.js`:1 |
| `https://jellyfin.org/docs/general/administration/hardware-acceleration` | absolute-url | `playback-transcoding.943e8888f8a425d83ca9.chunk.js`:1 |
| `https://jellyfin.org/docs/general/contributing/#translating` | absolute-url | `settings-index-tsx.0623441d097e656c1672.chunk.js`:1 |
| `https://jellyfin.org/docs/general/networking/` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/post-install/setup-wizard/` | absolute-url | `start-index-html.8799498149b52451853c.chunk.js`:1 |
| `https://jellyfin.org/docs/general/post-install/transcoding/hardware-acceleration/intel#configure-and-verify-lp-mode-on-linux` | absolute-url | `playback-transcoding.943e8888f8a425d83ca9.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/devices` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/libraries` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/live-tv/` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/live-tv/setup-guide#adding-guide-data` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/media/books` | absolute-url | `library.92743168712c9d91aa54.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/media/external-files` | absolute-url | `39345.2e097a87c2a50b2c2838.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/media/movies` | absolute-url | `library.92743168712c9d91aa54.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/media/music` | absolute-url | `library.92743168712c9d91aa54.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/media/shows` | absolute-url | `library.92743168712c9d91aa54.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/plugins/` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/plugins/#repositories` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/tasks` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/docs/general/server/transcoding` | absolute-url | `6496.59e71d86fcea8244ef07.chunk.js`:1 |
| `https://jellyfin.org/downloads/server/` | absolute-url | `main.jellyfin.bundle.js`:2 |
| `https://m` | absolute-url | `fo-json.6b60bc20642e180402f9.chunk.js`:1 |
| `https://manoserveris.lt` | absolute-url | `lt-lt-json.0eee5fb08e6deeb85238.chunk.js`:1 |
| `https://meuservidor.com` | absolute-url | `pt-br-json.8546ed310415ca42ce04.chunk.js`:1 |
| `https://mijnserver.nl` | absolute-url | `nl-json.f3e1a929551f6a04662f.chunk.js`:1 |
| `https://min-servar.no` | absolute-url | `nn-json.e72736a65a96d03929f0.chunk.js`:1 |
| `https://min.server.com` | absolute-url | `sv-json.e5ae235d18d612ebcc5c.chunk.js`:1 |
| `https://minnthjonn.is` | absolute-url | `is-is-json.fa6a22a9e4fbacb2f178.chunk.js`:1 |
| `https://minserver.no` | absolute-url | `nb-json.7237dfe8ad0c3fed595d.chunk.js`:1 |
| `https://miservidor.com` | absolute-url | `es-ar-json.742685c313a61fbd889d.chunk.js`:1 |
| `https://mojserver.sk` | absolute-url | `sk-json.fa7b2a2f2d5cd17bf53e.chunk.js`:1 |
| `https://mojserwer.pl` | absolute-url | `pl-json.09ce1692fa30fb58bd97.chunk.js`:1 |
| `https://monserveur.com` | absolute-url | `fr-ca-json.80bffb6b2565c55f7f17.chunk.js`:1 |
| `https://mozilla.github.io/localForage/#definedriver` | absolute-url | `node_modules.localforage.4b2a2f8b573f0c35e266.chunk.js`:2 |
| `https://mui.com/production-error/?code=` | absolute-url | `node_modules.@mui.utils.bundle.js`:1 |
| `https://mui.com/system/display/#display-in-print.` | absolute-url | `node_modules.@mui.system.bundle.js`:1 |
| `https://mui.com/x/react-date-pickers/fields/#fields-to-edit-a-single-element` | absolute-url | `node_modules.@mui.x-date-pickers.6abcdebd9403e77c393a.chunk.js`:1 |
| `https://mui.com/x/react-date-pickers/getting-started/#installation` | absolute-url | `node_modules.@mui.x-date-pickers.6abcdebd9403e77c393a.chunk.js`:1 |
| `https://mujserver.cz` | absolute-url | `cs-json.b38ca5a1ae26d3c78945.chunk.js`:1 |
| `https://myserver.com` | absolute-url | `ar-json.c7d0bcd3c951b26aaf8e.chunk.js`:1 |
| `https://reactjs.org/docs/error-decoder.html?invariant=` | absolute-url | `node_modules.react-dom.bundle.js`:2 |
| `https://repo.jellyfin.org/` | absolute-url | `plugins-plugin.f3b592c7af3f85e514ee.chunk.js`:1 |
| `https://stuk.github.io/jszip/documentation/howto/read_zip.html` | absolute-url | `node_modules.jszip.c4a58cbf99c347b50bc6.chunk.js`:2 |
| `https://sunucum.com` | absolute-url | `tr-json.b4ec0bff4a109d111559.chunk.js`:1 |
| `https://was` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `https://www.recent` | absolute-url | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `https://www.youtube.com/iframe_api` | absolute-url | `youtubePlayer-plugin.fa67b1ec7d5bcf80338c.chunk.js`:1 |
| `https://x` | absolute-url | `node_modules.core-js.bundle.js`:1 |

</details>

## 3. GraphQL operations

_None found._

## 4. DOM-XSS sinks

| Sink | Count | Nearby sources | File:Line |
|---|---|---|---|
| `message listener` | 1 | event.data | `12011.59d68def33f006b4d5b5.chunk.js`:1 |
| `message listener` | 1 | event.data | `72044.700deed02f94d074d3fd.chunk.js`:1 |
| `message listener` | 1 | event.data | `76542.4486f56001630eca65e3.chunk.js`:1 |
| `message listener` | 1 | event.data | `libraries\subtitles-octopus-worker.js`:1 |
| `postMessage` | 1 | event.data | `node_modules.axios.bundle.js`:2 |
| `message listener` | 1 | event.data | `node_modules.axios.bundle.js`:2 |
| `message listener` | 2 | event.data | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js`:1 |
| `message listener` | 1 | event.data | `node_modules.jszip.c4a58cbf99c347b50bc6.chunk.js`:2 |
| `postMessage` | 2 | event.data | `node_modules.libbitsub.16f6cbda1921fa9cb713.chunk.js`:2 |
| `postMessage` | 1 | event.data | `node_modules.webcomponents.js.bundle.js`:2 |
| `message listener` | 1 | event.data | `node_modules.webcomponents.js.bundle.js`:2 |
| `innerHTML` | 14 | - | `10739.4d0d5d243bb941cd9821.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `10739.4d0d5d243bb941cd9821.chunk.js`:1 |
| `new Function` | 1 | - | `1133.bundle.js`:2 |
| `dangerouslySetInnerHTML` | 1 | - | `1133.bundle.js`:2 |
| `postMessage` | 1 | - | `1133.bundle.js`:2 |
| `innerHTML` | 2 | - | `11851.ed201579e96d780f36b3.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `11851.ed201579e96d780f36b3.chunk.js`:1 |
| `postMessage` | 1 | - | `12011.59d68def33f006b4d5b5.chunk.js`:1 |
| `innerHTML` | 2 | - | `12325.ea8b401419acccee722a.chunk.js`:1 |
| `innerHTML` | 5 | - | `12426.5768421e4438fe0e247a.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `12426.5768421e4438fe0e247a.chunk.js`:1 |
| `innerHTML` | 1 | - | `12519.ff1d554427cf2d5f17d8.chunk.js`:1 |
| `innerHTML` | 1 | - | `14036.a2fc72346fd78112f0dd.chunk.js`:1 |
| `innerHTML` | 5 | - | `14245.d5294b1bf572bcb9edd7.chunk.js`:1 |
| `insertAdjacentHTML` | 2 | - | `14245.d5294b1bf572bcb9edd7.chunk.js`:1 |
| `innerHTML` | 4 | - | `1451.72037c81d39190d14e0f.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `1451.72037c81d39190d14e0f.chunk.js`:1 |
| `jQuery html()` | 2 | - | `1451.72037c81d39190d14e0f.chunk.js`:1 |
| `innerHTML` | 5 | - | `14553.6ddb0da23f2698557d33.chunk.js`:1 |
| `insertAdjacentHTML` | 2 | - | `14553.6ddb0da23f2698557d33.chunk.js`:1 |
| `innerHTML` | 3 | - | `17072.f97923623e21bccb4fd3.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `17072.f97923623e21bccb4fd3.chunk.js`:1 |
| `innerHTML` | 5 | - | `17443.ed534cf0becf543b47a1.chunk.js`:1 |
| `innerHTML` | 2 | - | `1831.2a123582e8d6b068b3cc.chunk.js`:1 |
| `innerHTML` | 2 | - | `1836.52f62b4661aa037c33f4.chunk.js`:1 |
| `innerHTML` | 2 | - | `20963.4124a222fc0edafc3b86.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `20963.4124a222fc0edafc3b86.chunk.js`:1 |
| `innerHTML` | 5 | - | `24468.66747b7d9d4daeea7960.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `24468.66747b7d9d4daeea7960.chunk.js`:1 |
| `innerHTML` | 2 | - | `24871.d75813c098a58459e203.chunk.js`:1 |
| `innerHTML` | 1 | - | `25029.0a13d28fc0fbeccb6316.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `25029.0a13d28fc0fbeccb6316.chunk.js`:1 |
| `innerHTML` | 2 | - | `25091.5d5d692c0058b3011c3f.chunk.js`:1 |
| `innerHTML` | 1 | - | `26556.2fa091e480d4d0429be9.chunk.js`:1 |
| `innerHTML` | 18 | - | `26855.ad7a271624659e1f2d6e.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `26855.ad7a271624659e1f2d6e.chunk.js`:1 |
| `innerHTML` | 3 | - | `26914.df58b6dea960895b28ec.chunk.js`:2 |
| `innerHTML` | 1 | - | `27884.a81bf06d441dff4daa07.chunk.js`:1 |
| `innerHTML` | 1 | - | `28463.3bd303a31c6610d60e49.chunk.js`:1 |
| `innerHTML` | 5 | - | `28524.2c1384b3f06c676628ae.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `28524.2c1384b3f06c676628ae.chunk.js`:1 |
| `innerHTML` | 1 | - | `28739.ee5d7ca7b3a10619d964.chunk.js`:1 |
| `innerHTML` | 4 | - | `30657.c12665e8caacf51a34d4.chunk.js`:2 |
| `innerHTML` | 1 | - | `31514.8843e677da003bcc8756.chunk.js`:1 |
| `innerHTML` | 4 | - | `3380.bc7dedf9f3abf676881e.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `3380.bc7dedf9f3abf676881e.chunk.js`:1 |
| `innerHTML` | 3 | - | `35308.0b1567d9abe0bdae4331.chunk.js`:1 |
| `innerHTML` | 1 | - | `3774.5f0e11f63ba95007a0e0.chunk.js`:1 |
| `innerHTML` | 7 | - | `39345.2e097a87c2a50b2c2838.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `39345.2e097a87c2a50b2c2838.chunk.js`:1 |
| `innerHTML` | 1 | - | `40501.6747a381365f8ed532c4.chunk.js`:1 |
| `innerHTML` | 5 | - | `40958.680318bd5babf07acb54.chunk.js`:1 |
| `innerHTML` | 3 | - | `4330.e1f94d0eb9b1e13978cd.chunk.js`:1 |
| `innerHTML` | 2 | - | `4350.61757155d557202e3d9a.chunk.js`:2 |
| `postMessage` | 1 | - | `4350.61757155d557202e3d9a.chunk.js`:2 |
| `message listener` | 1 | - | `4350.61757155d557202e3d9a.chunk.js`:2 |
| `innerHTML` | 5 | - | `44599.d1a966b8818e6eab31cb.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `44599.d1a966b8818e6eab31cb.chunk.js`:1 |
| `innerHTML` | 1 | - | `44910.ac49ca7c32dd81f27e37.chunk.js`:1 |
| `innerHTML` | 2 | - | `45568.f61f61377609c9922e8a.chunk.js`:2 |
| `insertAdjacentHTML` | 1 | - | `45568.f61f61377609c9922e8a.chunk.js`:2 |
| `innerHTML` | 3 | - | `47102.21d099f61684ed6660ae.chunk.js`:2 |
| `innerHTML` | 2 | - | `47472.73de9f0f9c4dd7c901a4.chunk.js`:1 |
| `innerHTML` | 2 | - | `47649.9b59a4f1ad0197d2e672.chunk.js`:1 |
| `innerHTML` | 3 | - | `47836.bfd042fc1e9fe27ca77a.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `47836.bfd042fc1e9fe27ca77a.chunk.js`:1 |
| `innerHTML` | 4 | - | `48232.77dbbf8104f4b000cd18.chunk.js`:1 |
| `innerHTML` | 3 | - | `49092.1c32878e811796ac119d.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `49092.1c32878e811796ac119d.chunk.js`:1 |
| `innerHTML` | 1 | - | `49275.fcf2b77489e84c80e220.chunk.js`:1 |
| `innerHTML` | 5 | - | `49616.31989cf60f3ae2505a26.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `49616.31989cf60f3ae2505a26.chunk.js`:1 |
| `innerHTML` | 7 | - | `52197.ae3dbcde199a3bdd936b.chunk.js`:1 |
| `innerHTML` | 4 | - | `52361.4b5c69dc7fd52c0fa162.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `52361.4b5c69dc7fd52c0fa162.chunk.js`:1 |
| `innerHTML` | 1 | - | `54623.3daab0b8d9ad6b388a09.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `54623.3daab0b8d9ad6b388a09.chunk.js`:1 |
| `innerHTML` | 1 | - | `55645.5be54a1638bb18059a2a.chunk.js`:1 |
| `innerHTML` | 2 | - | `57949.890260722af4eefd0e71.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `57949.890260722af4eefd0e71.chunk.js`:1 |
| `innerHTML` | 1 | - | `59801.efc32b8f27e5cf6839a8.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `59801.efc32b8f27e5cf6839a8.chunk.js`:1 |
| `innerHTML` | 6 | - | `5996.58af3750142906e4e477.chunk.js`:1 |
| `innerHTML` | 2 | - | `60545.06925d0d51057c6fe099.chunk.js`:1 |
| `innerHTML` | 4 | - | `61989.ecefef213ab88f16effa.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `61989.ecefef213ab88f16effa.chunk.js`:1 |
| `innerHTML` | 1 | - | `62882.6747a381365f8ed532c4.chunk.js`:1 |
| `innerHTML` | 1 | - | `63379.db8ce158c14f279595ff.chunk.js`:1 |
| `innerHTML` | 1 | - | `63741.5510f44047221aaafd66.chunk.js`:1 |
| `innerHTML` | 12 | - | `65126.1932a6d52e2f813f2205.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `65126.1932a6d52e2f813f2205.chunk.js`:1 |
| `innerHTML` | 4 | - | `6940.f9e479afc2ca4df4354f.chunk.js`:1 |
| `innerHTML` | 10 | - | `69729.7bee2153474db54a7028.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `69729.7bee2153474db54a7028.chunk.js`:1 |
| `innerHTML` | 4 | - | `70538.329c9d2e16b670889098.chunk.js`:2 |
| `innerHTML` | 4 | - | `71162.f8bea5ce9b66d58608af.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `71162.f8bea5ce9b66d58608af.chunk.js`:1 |
| `innerHTML` | 1 | - | `71454.9eb1d7b2bfb7be51f2cd.chunk.js`:1 |
| `postMessage` | 1 | - | `72044.700deed02f94d074d3fd.chunk.js`:1 |
| `innerHTML` | 1 | - | `72521.f298ca11dc7addc9fb0e.chunk.js`:1 |
| `innerHTML` | 6 | - | `72681.b84931e31266c8153d76.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `72681.b84931e31266c8153d76.chunk.js`:1 |
| `innerHTML` | 7 | - | `73233.98e0cdb3f30f44fc6339.chunk.js`:2 |
| `innerHTML` | 2 | - | `74959.ab901dcc842d43716982.chunk.js`:1 |
| `postMessage` | 1 | - | `76542.4486f56001630eca65e3.chunk.js`:1 |
| `innerHTML` | 2 | - | `77004.5b7b187c3af1cca97d1e.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `77004.5b7b187c3af1cca97d1e.chunk.js`:1 |
| `innerHTML` | 3 | - | `80999.0ad671ffb5f3091538be.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `80999.0ad671ffb5f3091538be.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `81613.da4b1f96f2d812035be8.chunk.js`:1 |
| `innerHTML` | 4 | - | `81751.5f906ffdc8e33fd3e6fb.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `81751.5f906ffdc8e33fd3e6fb.chunk.js`:1 |
| `innerHTML` | 4 | - | `81949.eedef4a19c5d19741c94.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `81949.eedef4a19c5d19741c94.chunk.js`:1 |
| `innerHTML` | 2 | - | `84158.4141819ca8b5f6555c12.chunk.js`:1 |
| `innerHTML` | 1 | - | `91151.712e04085797577b7648.chunk.js`:1 |
| `innerHTML` | 1 | - | `91737.a37aaa8ddbabd2fe49c4.chunk.js`:1 |
| `innerHTML` | 4 | - | `92974.57b22fb2be1d5695f8d9.chunk.js`:2 |
| `insertAdjacentHTML` | 1 | - | `92974.57b22fb2be1d5695f8d9.chunk.js`:2 |
| `innerHTML` | 2 | - | `9446.3cbde37ffe7b34c4e748.chunk.js`:1 |
| `innerHTML` | 5 | - | `95062.58f5c4f2f2829ee9f212.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `95062.58f5c4f2f2829ee9f212.chunk.js`:1 |
| `innerHTML` | 16 | - | `95454.f59c8225d8013bc5ebe4.chunk.js`:2 |
| `insertAdjacentHTML` | 2 | - | `95454.f59c8225d8013bc5ebe4.chunk.js`:2 |
| `innerHTML` | 1 | - | `97112.acf7e65da4ffea70d36b.chunk.js`:1 |
| `innerHTML` | 3 | - | `98481.d650f8eccb32c6a403d9.chunk.js`:1 |
| `new Function` | 1 | - | `blurhash.worker.bundle.js`:1 |
| `postMessage` | 1 | - | `blurhash.worker.bundle.js`:1 |
| `innerHTML` | 2 | - | `bookPlayer-plugin.c83d5c43401890557a8f.chunk.js`:2 |
| `innerHTML` | 1 | - | `bookPlayer-tableOfContents.cc6c9a91fae86466c8d3.chunk.js`:1 |
| `innerHTML` | 1 | - | `comicsPlayer-plugin.c358c35860fc41e92b05.chunk.js`:2 |
| `postMessage` | 3 | - | `comicsPlayer-plugin.c358c35860fc41e92b05.chunk.js`:2 |
| `message listener` | 2 | - | `comicsPlayer-plugin.c358c35860fc41e92b05.chunk.js`:2 |
| `innerHTML` | 1 | - | `edititemmetadata.b9387387afb5ea222952.chunk.js`:1 |
| `innerHTML` | 2 | - | `favorites.a085188fd1c7a59cf41b.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `favorites.a085188fd1c7a59cf41b.chunk.js`:1 |
| `location assignment` | 1 | - | `finish.82e044aca6e27ae7f374.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `home-tsx.25a4fd1c984aa5b76be0.chunk.js`:1 |
| `innerHTML` | 3 | - | `htmlVideoPlayer-plugin.75e5631714895cbf4ff3.chunk.js`:2 |
| `innerHTML` | 41 | - | `itemDetails.ea83c659375b31117215.chunk.js`:1 |
| `insertAdjacentHTML` | 2 | - | `itemDetails.ea83c659375b31117215.chunk.js`:1 |
| `new Function` | 2 | - | `libraries\pdf.worker.js`:2 |
| `postMessage` | 17 | - | `libraries\pdf.worker.js`:2 |
| `message listener` | 1 | - | `libraries\pdf.worker.js`:2 |
| `document.write` | 4 | - | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `location assignment` | 5 | - | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `message listener` | 1 | - | `libraries\subtitles-octopus-worker-legacy.js`:1 |
| `document.write` | 4 | - | `libraries\subtitles-octopus-worker.js`:1 |
| `location assignment` | 5 | - | `libraries\subtitles-octopus-worker.js`:1 |
| `postMessage` | 3 | - | `libraries\worker-bundle.js`:2 |
| `message listener` | 2 | - | `libraries\worker-bundle.js`:2 |
| `innerHTML` | 7 | - | `libraries.48c8dc5badc6f3b7cae5.chunk.js`:2 |
| `innerHTML` | 3 | - | `library.92743168712c9d91aa54.chunk.js`:1 |
| `innerHTML` | 10 | - | `list.6a395a43c6b0d173eb90.chunk.js`:1 |
| `insertAdjacentHTML` | 2 | - | `list.6a395a43c6b0d173eb90.chunk.js`:1 |
| `innerHTML` | 4 | - | `livetv-livetvchannels.aa9287d25032d7bb2710.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `livetv-livetvchannels.aa9287d25032d7bb2710.chunk.js`:1 |
| `innerHTML` | 2 | - | `livetv-livetvrecordings.698f97c3e3b84d04a813.chunk.js`:1 |
| `innerHTML` | 3 | - | `livetv-livetvschedule.91e09b06587b793e1e34.chunk.js`:1 |
| `innerHTML` | 1 | - | `livetv-livetvseriestimers.7bb6f658b46f9d6f023d.chunk.js`:1 |
| `innerHTML` | 4 | - | `livetv-livetvsuggested.26516f1082425aa43091.chunk.js`:1 |
| `innerHTML` | 3 | - | `livetv.5a61001afdbc27367057.chunk.js`:1 |
| `innerHTML` | 1 | - | `livetvguideprovider.ab1d3f39b0df8443de1b.chunk.js`:1 |
| `innerHTML` | 2 | - | `livetvtuner.7f26fd14cc85a03cead3.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `livetvtuner.7f26fd14cc85a03cead3.chunk.js`:1 |
| `innerHTML` | 1 | - | `logoScreensaver-plugin.897823f6a7747f6cf262.chunk.js`:1 |
| `innerHTML` | 2 | - | `lyrics.d9ff6954ccb69667cd8a.chunk.js`:1 |
| `innerHTML` | 22 | - | `main.jellyfin.bundle.js`:2 |
| `dangerouslySetInnerHTML` | 1 | - | `main.jellyfin.bundle.js`:2 |
| `insertAdjacentHTML` | 2 | - | `main.jellyfin.bundle.js`:2 |
| `location assignment` | 1 | - | `main.jellyfin.bundle.js`:2 |
| `innerHTML` | 1 | - | `movies-moviecollections.d05e9ac62fec5569c155.chunk.js`:1 |
| `innerHTML` | 1 | - | `movies-moviegenres.83db311a32d205f5bfd7.chunk.js`:1 |
| `innerHTML` | 1 | - | `movies-movies.32a522436b8daf458a2f.chunk.js`:1 |
| `innerHTML` | 5 | - | `movies-moviesrecommended.6f024cdedc30ed291501.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `movies-moviesrecommended.6f024cdedc30ed291501.chunk.js`:1 |
| `innerHTML` | 1 | - | `music-musicalbums.32a522436b8daf458a2f.chunk.js`:1 |
| `innerHTML` | 1 | - | `music-musicartists.32a522436b8daf458a2f.chunk.js`:1 |
| `innerHTML` | 1 | - | `music-musicgenres.5f378d7483a903f87928.chunk.js`:1 |
| `innerHTML` | 1 | - | `music-musicplaylists.cf56d7899bfd59e76caf.chunk.js`:1 |
| `innerHTML` | 6 | - | `music-musicrecommended.14535d43c6df6aec5af8.chunk.js`:1 |
| `innerHTML` | 4 | - | `music-songs.0216269763524e653b72.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `music-songs.0216269763524e653b72.chunk.js`:1 |
| `postMessage` | 21 | - | `node_modules.@jellyfin.libass-wasm.d15f00d6cf7ae089c077.chunk.js`:1 |
| `message listener` | 2 | - | `node_modules.@jellyfin.libass-wasm.d15f00d6cf7ae089c077.chunk.js`:1 |
| `location assignment` | 1 | - | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `message listener` | 1 | - | `node_modules.@jellyfin.sdk.bundle.js`:2 |
| `dangerouslySetInnerHTML` | 1 | - | `node_modules.@mui.system.bundle.js`:1 |
| `innerHTML` | 2 | - | `node_modules.@mui.x-date-pickers.6abcdebd9403e77c393a.chunk.js`:1 |
| `postMessage` | 3 | - | `node_modules.core-js.bundle.js`:1 |
| `message listener` | 1 | - | `node_modules.core-js.bundle.js`:1 |
| `innerHTML` | 1 | - | `node_modules.dompurify.bundle.js`:2 |
| `outerHTML` | 1 | - | `node_modules.dompurify.bundle.js`:2 |
| `innerHTML` | 1 | - | `node_modules.epubjs.fc1e2c6aec473df47a5b.chunk.js`:1 |
| `location assignment` | 7 | - | `node_modules.epubjs.fc1e2c6aec473df47a5b.chunk.js`:1 |
| `new Function` | 1 | - | `node_modules.flv.js.90c8d7edea3de4aee202.chunk.js`:2 |
| `postMessage` | 23 | - | `node_modules.flv.js.90c8d7edea3de4aee202.chunk.js`:2 |
| `message listener` | 2 | - | `node_modules.flv.js.90c8d7edea3de4aee202.chunk.js`:2 |
| `postMessage` | 9 | - | `node_modules.hls.js.6591d78d7f6228aaadc1.chunk.js`:1 |
| `innerHTML` | 6 | - | `node_modules.jquery.bundle.js`:2 |
| `innerHTML` | 2 | - | `node_modules.jstree.06059368d3e505ed6e71.chunk.js`:2 |
| `postMessage` | 1 | - | `node_modules.jstree.06059368d3e505ed6e71.chunk.js`:2 |
| `new Function` | 1 | - | `node_modules.jszip.c4a58cbf99c347b50bc6.chunk.js`:2 |
| `postMessage` | 4 | - | `node_modules.jszip.c4a58cbf99c347b50bc6.chunk.js`:2 |
| `postMessage` | 1 | - | `node_modules.localforage.4b2a2f8b573f0c35e266.chunk.js`:2 |
| `eval` | 1 | - | `node_modules.pdfjs-dist.b983b688d208acfb7ec1.chunk.js`:2 |
| `new Function` | 2 | - | `node_modules.pdfjs-dist.b983b688d208acfb7ec1.chunk.js`:2 |
| `postMessage` | 17 | - | `node_modules.pdfjs-dist.b983b688d208acfb7ec1.chunk.js`:2 |
| `message listener` | 1 | - | `node_modules.pdfjs-dist.b983b688d208acfb7ec1.chunk.js`:2 |
| `innerHTML` | 3 | - | `node_modules.react-dom.bundle.js`:2 |
| `dangerouslySetInnerHTML` | 13 | - | `node_modules.react-dom.bundle.js`:2 |
| `new Function` | 1 | - | `node_modules.react-lazy-load-image-component.4c0850deb4bb234feecf.chunk.js`:1 |
| `innerHTML` | 2 | - | `node_modules.swiper.eed8ade7c72bcddcaf1e.chunk.js`:1 |
| `innerHTML` | 2 | - | `node_modules.webcomponents.js.bundle.js`:2 |
| `innerHTML` | 1 | - | `pdfPlayer-plugin.0e5794750bc919e9fcd7.chunk.js`:1 |
| `innerHTML` | 15 | - | `playback-queue.0ada2ea68574e1e8f75a.chunk.js`:1 |
| `insertAdjacentHTML` | 3 | - | `playback-queue.0ada2ea68574e1e8f75a.chunk.js`:1 |
| `innerHTML` | 18 | - | `playback-video.7de109744f4737bdf440.chunk.js`:2 |
| `dangerouslySetInnerHTML` | 1 | - | `plugins-plugin.f3b592c7af3f85e514ee.chunk.js`:1 |
| `dangerouslySetInnerHTML` | 1 | - | `quickConnect.d5ab946189409e40abf9.chunk.js`:1 |
| `innerHTML` | 1 | - | `remote.8ef57195cfc3af655b67.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `remote.8ef57195cfc3af655b67.chunk.js`:1 |
| `new Function` | 1 | - | `runtime.bundle.js`:1 |
| `innerHTML` | 2 | - | `search.0b435db6b8a8a2156d0a.chunk.js`:1 |
| `dangerouslySetInnerHTML` | 1 | - | `search.0b435db6b8a8a2156d0a.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `search.0b435db6b8a8a2156d0a.chunk.js`:1 |
| `innerHTML` | 2 | - | `session-login.cb3c7c6a0f3396901580.chunk.js`:2 |
| `location assignment` | 1 | - | `session-resetPassword.e6da8d829ea3e1cc1817.chunk.js`:1 |
| `innerHTML` | 2 | - | `session-selectServer.af1b7fd53b5c81d7a423.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `session-selectServer.af1b7fd53b5c81d7a423.chunk.js`:1 |
| `innerHTML` | 3 | - | `settings-index-js.dfcad5858aaef03756b3.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `settings-index-js.dfcad5858aaef03756b3.chunk.js`:1 |
| `innerHTML` | 3 | - | `settings.3e541eb0466efb36c6ae.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `settings.3e541eb0466efb36c6ae.chunk.js`:1 |
| `innerHTML` | 5 | - | `shows-episodes.648558c7c753767932eb.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `shows-episodes.648558c7c753767932eb.chunk.js`:1 |
| `innerHTML` | 1 | - | `shows-tvgenres.c1a77b6e8e31324a08c9.chunk.js`:1 |
| `innerHTML` | 3 | - | `shows-tvrecommended.486f6b70e58899344f85.chunk.js`:1 |
| `innerHTML` | 1 | - | `shows-tvshows.32a522436b8daf458a2f.chunk.js`:1 |
| `innerHTML` | 2 | - | `shows-tvupcoming.9a7972b221d75b0c650c.chunk.js`:1 |
| `innerHTML` | 2 | - | `start.695c6db2ef595e6d1a90.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `start.695c6db2ef595e6d1a90.chunk.js`:1 |
| `innerHTML` | 5 | - | `user-home.e4ae606b60dda7eefc69.chunk.js`:2 |
| `insertAdjacentHTML` | 1 | - | `user-home.e4ae606b60dda7eefc69.chunk.js`:2 |
| `innerHTML` | 9 | - | `user-playback.3bc40e3166f445a60628.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `user-playback.3bc40e3166f445a60628.chunk.js`:1 |
| `innerHTML` | 3 | - | `user-subtitles.75a7b3fd3e6d09dc750b.chunk.js`:1 |
| `insertAdjacentHTML` | 1 | - | `user-subtitles.75a7b3fd3e6d09dc750b.chunk.js`:1 |
| `dangerouslySetInnerHTML` | 3 | - | `users-add.ddddab81f261bf2ff4d7.chunk.js`:1 |
| `innerHTML` | 1 | - | `users-edit.6b717b133ba6e3c018c5.chunk.js`:1 |
| `dangerouslySetInnerHTML` | 4 | - | `users-edit.6b717b133ba6e3c018c5.chunk.js`:1 |
| `dangerouslySetInnerHTML` | 2 | - | `users.f5b80a5f1b08bc92de28.chunk.js`:1 |
| `innerHTML` | 1 | - | `youtubePlayer-plugin.fa67b1ec7d5bcf80338c.chunk.js`:1 |

Rows with a nearby source are the ones worth manual review.

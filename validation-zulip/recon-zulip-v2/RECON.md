# JavaScript Recon Report

- **Source:** `validation-zulip\js-loot\js`
- **Generated:** 2026-10-01 20:47:36
- **Files analysed:** 64 (11,120,196 bytes)

- **First-party domains:** `zulip.com`
- **Denominator:** 375 total · 274 first-party · 94 third-party SDK · 7 unresolved base
- **API-shaped only:** 375 total · 274 first-party · 94 third-party SDK · 7 unresolved base
- Quote coverage against the **first-party** number, and say which number you quoted. Nothing was dropped: every row is in `recon.json` with its `party` field.

| Finding | Count |
|---|---|
| API-looking endpoints | 375 |
|   ...of those, first-party | 274 |
|   ...of those, third-party SDK | 94 |
|   ...of those, unresolved base | 7 |
| Other URLs / paths | 0 |
| GraphQL operations | 0 |
| Secret candidates | 228 |
| DOM-XSS sink sites | 35 |

## 1. Hardcoded secrets & credentials

### LOW (228)

| Rule | Variable | Value (redacted) | Entropy | File | Line |
|---|---|---|---|---|---|
| Internal host / private IP | `-` | `base64...test` | 3.38 | `2660.f5237f97f217fae19751.js` | 1 |
| Internal host / private IP | `-` | `base64...test` | 3.38 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `timeZo...test` | 3.26 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `this.i...rnal` | 3.24 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `rnames...test` | 3.19 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `rnames...test` | 3.19 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `CHILD.test` | 3.12 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `CHILD.test` | 3.12 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `number.test` | 3.1 | `2047.bd145190771422740ea5.js` | 1 |
| Internal host / private IP | `-` | `number.test` | 3.1 | `2660.f5237f97f217fae19751.js` | 1 |
| Internal host / private IP | `-` | `number.test` | 3.1 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `number.test` | 3.1 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `hostna...test` | 3.03 | `2660.f5237f97f217fae19751.js` | 1 |
| Internal host / private IP | `-` | `hostna...test` | 3.03 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `protoc...test` | 2.97 | `2660.f5237f97f217fae19751.js` | 1 |
| Internal host / private IP | `-` | `protoc...test` | 2.97 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `dtg.local` | 2.95 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `e.internal` | 2.92 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `needsC...test` | 2.91 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `needsC...test` | 2.91 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `attrRe...test` | 2.9 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `protot...test` | 2.81 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `pattern.test` | 2.75 | `2660.f5237f97f217fae19751.js` | 1 |
| Internal host / private IP | `-` | `pattern.test` | 2.75 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `localhost` | 2.73 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `localhost` | 2.73 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `Xn.test` | 2.52 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `un.test` | 2.52 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `dn.test` | 2.52 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `yn.test` | 2.52 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `vn.test` | 2.52 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `rn.test` | 2.52 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `ln.test` | 2.52 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `e.local` | 2.52 | `2660.f5237f97f217fae19751.js` | 1 |
| Internal host / private IP | `-` | `ln.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `fn.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `yn.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `mn.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Tn.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Sn.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Nn.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `An.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Rn.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `kn.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Gn.test` | 2.52 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `cn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `fn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `vn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `yn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Tn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Sn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `qn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Dn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Pn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `kn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Yn.test` | 2.52 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `MI.test` | 2.52 | `6215.b6341c1da50665d7cf15.js` | 1 |
| Internal host / private IP | `-` | `e.local` | 2.52 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `n.local` | 2.52 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `r.local` | 2.52 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `ni.test` | 2.52 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `e.local` | 2.52 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `gi.test` | 2.52 | `billing_auth.54951dcac1fa76a9ee3c.js` | 1 |
| Internal host / private IP | `-` | `Wn.test` | 2.52 | `katex-cli.js` | 1 |
| Internal host / private IP | `-` | `X.test` | 2.25 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `Q.test` | 2.25 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `G.test` | 2.25 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `V.test` | 2.25 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `b.test` | 2.25 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `k.test` | 2.25 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `N.test` | 2.25 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `A.test` | 2.25 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `q.test` | 2.25 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `4036.812fedda9a99929a355f.js` | 2 |
| Internal host / private IP | `-` | `l.test` | 2.25 | `4036.812fedda9a99929a355f.js` | 2 |
| Internal host / private IP | `-` | `c.test` | 2.25 | `4036.812fedda9a99929a355f.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `b.test` | 2.25 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `I.test` | 2.25 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `k.test` | 2.25 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `q.test` | 2.25 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `D.test` | 2.25 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `N.test` | 2.25 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `o.test` | 2.25 | `436.db660eb8a29b291918da.js` | 1 |
| Internal host / private IP | `-` | `m.test` | 2.25 | `5271.dee659f41f27e6e0050a.js` | 1 |
| Internal host / private IP | `-` | `c.test` | 2.25 | `5271.dee659f41f27e6e0050a.js` | 1 |
| Internal host / private IP | `-` | `p.test` | 2.25 | `5271.dee659f41f27e6e0050a.js` | 1 |
| Internal host / private IP | `-` | `Y.test` | 2.25 | `5271.dee659f41f27e6e0050a.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `5609.0f8f16426292bf6898e6.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `6108.1b0f4b4bedcf69b4b375.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `6117.e31c8473d9f44d30338e.js` | 1 |
| Internal host / private IP | `-` | `o.test` | 2.25 | `6215.b6341c1da50665d7cf15.js` | 1 |
| Internal host / private IP | `-` | `r.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `n.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `K.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `Q.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `Y.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `W.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `z.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `O.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `C.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `R.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `b.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `Z.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `G.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `x.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `y.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `m.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `p.test` | 2.25 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `T.test` | 2.25 | `7820.868203aba2a3f30382bf.js` | 1 |
| Internal host / private IP | `-` | `E.test` | 2.25 | `7820.868203aba2a3f30382bf.js` | 1 |
| Internal host / private IP | `-` | `b.test` | 2.25 | `7820.868203aba2a3f30382bf.js` | 1 |
| Internal host / private IP | `-` | `o.test` | 2.25 | `8050.5a6eab020aeb7e241eca.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `8050.5a6eab020aeb7e241eca.js` | 1 |
| Internal host / private IP | `-` | `h.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `b.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `X.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `K.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `G.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `J.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `n.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `r.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `u.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `U.test` | 2.25 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `8626.02ea5aafd07f3ec0f1cf.js` | 1 |
| Internal host / private IP | `-` | `y.test` | 2.25 | `8626.02ea5aafd07f3ec0f1cf.js` | 1 |
| Internal host / private IP | `-` | `E.test` | 2.25 | `8626.02ea5aafd07f3ec0f1cf.js` | 1 |
| Internal host / private IP | `-` | `m.test` | 2.25 | `8626.02ea5aafd07f3ec0f1cf.js` | 1 |
| Internal host / private IP | `-` | `v.test` | 2.25 | `9673.a285a8958157ead406df.js` | 2 |
| Internal host / private IP | `-` | `o.test` | 2.25 | `app.9ce541840b7470231ad5.js` | 1 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `app.9ce541840b7470231ad5.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `app.9ce541840b7470231ad5.js` | 1 |
| Internal host / private IP | `-` | `u.test` | 2.25 | `app.9ce541840b7470231ad5.js` | 1 |
| Internal host / private IP | `-` | `l.test` | 2.25 | `app.9ce541840b7470231ad5.js` | 1 |
| Internal host / private IP | `-` | `d.test` | 2.25 | `app.9ce541840b7470231ad5.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `help.678fed81da027c937561.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `integrations.c56e78ec753c515cc8a0.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `jdenticon.js` | 1 |
| Internal host / private IP | `-` | `D.test` | 2.25 | `katex-cli.js` | 1 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `katex-cli.js` | 1 |
| Internal host / private IP | `-` | `r.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `u.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `o.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `m.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `n.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `i.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `l.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `a.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `c.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `p.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `U.test` | 2.25 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `n.test` | 2.25 | `upgrade.1d05e463a7988d8dae6f.js` | 1 |
| Internal host / private IP | `-` | `he.test` | 2.24 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `ye.test` | 2.24 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `ve.test` | 2.24 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `We.test` | 2.24 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Ue.test` | 2.24 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Qe.test` | 2.24 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `pe.test` | 2.24 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `ve.test` | 2.24 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `me.test` | 2.24 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Me.test` | 2.24 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Ie.test` | 2.24 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Qe.test` | 2.24 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Ee.test` | 2.24 | `6215.b6341c1da50665d7cf15.js` | 1 |
| Internal host / private IP | `-` | `Qe.test` | 2.24 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `ae.test` | 2.24 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `me.test` | 2.24 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `pe.test` | 2.24 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `ve.test` | 2.24 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `he.test` | 2.24 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `re.test` | 2.24 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `ce.test` | 2.24 | `7018.30d28337a85dfd6155b1.js` | 2 |
| Internal host / private IP | `-` | `pe.test` | 2.24 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `me.test` | 2.24 | `8413.55cc9ce65475198524f9.js` | 2 |
| Internal host / private IP | `-` | `be.test` | 2.24 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `ge.test` | 2.24 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `ye.test` | 2.24 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `nn.test` | 2.24 | `katex_server.js` | 2 |
| Internal host / private IP | `-` | `127.0.0.1` | 2.2 | `katex-cli.js` | 1 |
| Internal host / private IP | `-` | `rt.test` | 2.13 | `1670.0963a7d39fadd579768e.js` | 2 |
| Internal host / private IP | `-` | `at.test` | 2.13 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `dt.test` | 2.13 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `ht.test` | 2.13 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `At.test` | 2.13 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `St.test` | 2.13 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Ht.test` | 2.13 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `It.test` | 2.13 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Xt.test` | 2.13 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `Ut.test` | 2.13 | `3150.7902c205f4f7d6d9e059.js` | 2 |
| Internal host / private IP | `-` | `ht.test` | 2.13 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `pt.test` | 2.13 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Dt.test` | 2.13 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `St.test` | 2.13 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Ot.test` | 2.13 | `420.288148b70ab4f3988e8c.js` | 2 |
| Internal host / private IP | `-` | `Ut.test` | 2.13 | `420.288148b70ab4f3988e8c.js` | 2 |

<details><summary><code>Internal host / private IP</code> @ 2660.f5237f97f217fae19751.js:1</summary>

```js
format:"base64",input:t.value,inst:e,continue:!n.abort})}});function E(e){if(!u.base64url.test(e))return!1;const n=e.replace(/[-_]/g,e=>"-"===e?"+":"/");return N(n.padEnd(4*M
```
</details>

<details><summary><code>Internal host / private IP</code> @ 8413.55cc9ce65475198524f9.js:2</summary>

```js
format:"base64",input:n.value,inst:e,continue:!t.abort})}});function N(e){if(!l.base64url.test(e))return!1;const t=e.replace(/[-_]/g,e=>"-"===e?"+":"/");return A(t.padEnd(4*M
```
</details>

<details><summary><code>Internal host / private IP</code> @ 8413.55cc9ce65475198524f9.js:2</summary>

```js
er);let r;if(n.length>2)return t;if(/:/.test(n[0])?r=n[0]:(t.date=n[0],r=n[1],s.timeZoneDelimiter.test(t.date)&&(t.date=e.split(s.timeZoneDelimiter)[0],r=e.substr(t.date.length,e.len
```
</details>

<details><summary><code>Internal host / private IP</code> @ 8413.55cc9ce65475198524f9.js:2</summary>

```js
.e){super(),e.length>1&&"string"==typeof e[e.length-1]&&(this.timeZone=e.pop()),this.internal=new Date,isNaN(a(this.timeZone,this))?this.setTime(NaN):e.length?"number"==type
```
</details>

<details><summary><code>Internal host / private IP</code> @ 3150.7902c205f4f7d6d9e059.js:2</summary>

```js
s[n++])&&!u.isImmediatePropagationStopped();)u.rnamespace&&!1!==o.namespace&&!u.rnamespace.test(o.namespace)||(u.handleObj=o,u.data=o.data,void 0!==(r=((w.event.special[o.orig
```
</details>

<details><summary><code>Internal host / private IP</code> @ 420.288148b70ab4f3988e8c.js:2</summary>

```js
s[n++])&&!u.isImmediatePropagationStopped();)u.rnamespace&&!1!==o.namespace&&!u.rnamespace.test(o.namespace)||(u.handleObj=o,u.data=o.data,void 0!==(r=((w.event.special[o.orig
```
</details>

<details><summary><code>Internal host / private IP</code> @ 3150.7902c205f4f7d6d9e059.js:2</summary>

```js
"odd"===e[3])):e[3]&&_(e[0]),e},PSEUDO:function(e){var t,n=!e[6]&&e[2];return W.CHILD.test(e[0])?null:(e[3]?e[2]=e[4]||e[5]||"":n&&$.test(n)&&(t=z(n,!0))&&(t=n.indexOf(")
```
</details>

<details><summary><code>Internal host / private IP</code> @ 420.288148b70ab4f3988e8c.js:2</summary>

```js
"odd"===e[3])):e[3]&&z(e[0]),e},PSEUDO:function(e){var t,n=!e[6]&&e[2];return M.CHILD.test(e[0])?null:(e[3]?e[2]=e[4]||e[5]||"":n&&I.test(n)&&(t=X(n,!0))&&(t=n.indexOf(")
```
</details>

<details><summary><code>Internal host / private IP</code> @ 2047.bd145190771422740ea5.js:1</summary>

```js
Async schemas not supported in object keys currently");if("string"==typeof c&&r.number.test(c)&&d.issues.length){const e=n.keyType._zod.run({value:Number(c),issues:[]},i);
```
</details>

<details><summary><code>Internal host / private IP</code> @ 2660.f5237f97f217fae19751.js:1</summary>

```js
Async schemas not supported in object keys currently");if("string"==typeof s&&u.number.test(s)&&c.issues.length){const e=n.keyType._zod.run({value:Number(s),issues:[]},r);
```
</details>

<details><summary><code>Internal host / private IP</code> @ 7018.30d28337a85dfd6155b1.js:2</summary>

```js
Async schemas not supported in object keys currently");if("string"==typeof c&&o.number.test(c)&&u.issues.length){const e=t.keyType._zod.run({value:Number(c),issues:[]},a);
```
</details>

<details><summary><code>Internal host / private IP</code> @ 8413.55cc9ce65475198524f9.js:2</summary>

```js
Async schemas not supported in object keys currently");if("string"==typeof s&&l.number.test(s)&&c.issues.length){const e=t.keyType._zod.run({value:Number(s),issues:[]},i);
```
</details>

<details><summary><code>Internal host / private IP</code> @ 2660.f5237f97f217fae19751.js:1</summary>

```js
onst i=t.value.trim(),r=new URL(i);return n.hostname&&(n.hostname.lastIndex=0,n.hostname.test(r.hostname)||t.issues.push({code:"invalid_format",format:"url",note:"Invalid ho
```
</details>

<details><summary><code>Internal host / private IP</code> @ 8413.55cc9ce65475198524f9.js:2</summary>

```js
onst r=n.value.trim(),i=new URL(r);return t.hostname&&(t.hostname.lastIndex=0,t.hostname.test(i.hostname)||n.issues.push({code:"invalid_format",format:"url",note:"Invalid ho
```
</details>

<details><summary><code>Internal host / private IP</code> @ 2660.f5237f97f217fae19751.js:1</summary>

```js
input:t.value,inst:e,continue:!n.abort})),n.protocol&&(n.protocol.lastIndex=0,n.protocol.test(r.protocol.endsWith(":")?r.protocol.slice(0,-1):r.protocol)||t.issues.push({cod
```
</details>

<details><summary><code>Internal host / private IP</code> @ 8413.55cc9ce65475198524f9.js:2</summary>

```js
input:n.value,inst:e,continue:!t.abort})),t.protocol&&(t.protocol.lastIndex=0,t.protocol.test(i.protocol.endsWith(":")?i.protocol.slice(0,-1):i.protocol)||n.issues.push({cod
```
</details>

<details><summary><code>Internal host / private IP</code> @ katex_server.js:2</summary>

```js
ion/vnd.ds-keypoint":{"source":"apache","extensions":["kpxx"]},"application/vnd.dtg.local":{"source":"iana"},"application/vnd.dtg.local.flash":{"source":"iana"},"applica
```
</details>

<details><summary><code>Internal host / private IP</code> @ 8413.55cc9ce65475198524f9.js:2</summary>

```js
rn new l(+new Date(e),this.timeZone)}}const u=/^(get|set)(?!UTC)/;function c(e){e.internal.setTime(+e),e.internal.setUTCSeconds(e.internal.getUTCSeconds()-Math.round(60*-
```
</details>

<details><summary><code>Internal host / private IP</code> @ 3150.7902c205f4f7d6d9e059.js:2</summary>

```js
[])[0]))return n;l&&(t=t.parentNode),e=e.slice(a.shift().value.length)}for(i=ge.needsContext.test(e)?0:a.length;i--&&(s=a[i],!w.expr.relative[u=s.type]);)if((c=w.expr.find[u])&&
```
</details>

<details><summary><code>Internal host / private IP</code> @ 420.288148b70ab4f3988e8c.js:2</summary>

```js
[])[0]))return n;c&&(t=t.parentNode),e=e.slice(s.shift().value.length)}for(i=ge.needsContext.test(e)?0:s.length;i--&&(a=s[i],!w.expr.relative[u=a.type]);)if((l=w.expr.find[u])&&
```
</details>

<details><summary><code>Internal host / private IP</code> @ 7018.30d28337a85dfd6155b1.js:2</summary>

```js
e._basePlotModules;if(s){var c;for(r=0;r<s.length;r++){if((i=s[r]).attrRegex&&i.attrRegex.test(t)){if(i.layoutAttrOverrides)return i.layoutAttrOverrides;!c&&i.layoutAttribute
```
</details>

<details><summary><code>Internal host / private IP</code> @ katex_server.js:2</summary>

```js
.replace,y=String.prototype.toUpperCase,w=String.prototype.toLowerCase,k=RegExp.prototype.test,j=Array.prototype.concat,S=Array.prototype.join,_=Array.prototype.slice,T=Math.
```
</details>

<details><summary><code>Internal host / private IP</code> @ 2660.f5237f97f217fae19751.js:1</summary>

```js
(n.pattern))}),n.pattern?(t=e._zod).check??(t.check=t=>{n.pattern.lastIndex=0,n.pattern.test(t.value)||t.issues.push({origin:"string",code:"invalid_format",format:n.format,
```
</details>

<details><summary><code>Internal host / private IP</code> @ 8413.55cc9ce65475198524f9.js:2</summary>

```js
(t.pattern))}),t.pattern?(n=e._zod).check??(n.check=n=>{t.pattern.lastIndex=0,t.pattern.test(n.value)||n.issues.push({origin:"string",code:"invalid_format",format:t.format,
```
</details>

<details><summary><code>Internal host / private IP</code> @ 8413.55cc9ce65475198524f9.js:2</summary>

```js
r a=i[1];return!!a&&!(!n.test(a)&&!r.test(a))};var t=/^(?:\w+:)?\/\/(\S+)$/,n=/^localhost[\:?\d]*(?:[^\:?\d]\S*)?$/,r=/^[^\s\.]+\.\S{2,}$/},51465(e,t,n){"use strict";!fu
```
</details>

<details><summary><code>Internal host / private IP</code> @ katex_server.js:2</summary>

```js
uire__(4060);const mn=un;un.HttpError;var dn=__webpack_require__(523);const hn="localhost",fn=Number(process.argv[2]??"9700");if(!Number.isInteger(fn))throw new TypeErro
```
</details>

<details><summary><code>Internal host / private IP</code> @ 1670.0963a7d39fadd579768e.js:2</summary>

```js
++t]=[n,n]}),r}function lr(n){return ur(n)?function(n){for(var t=Xn.lastIndex=0;Xn.test(n);)++t;return t}(n):Dt(n)}function sr(n){return ur(n)?function(n){return n.mat
```
</details>

<details><summary><code>Internal host / private IP</code> @ 1670.0963a7d39fadd579768e.js:2</summary>

```js
]}(n):function(n){return n.split("")}(n)}function hr(n){for(var t=n.length;t--&&un.test(n.charAt(t)););return t}var pr=Zt({"&amp;":"&","&lt;":"<","&gt;":">","&quot;":'
```
</details>

<details><summary><code>Internal host / private IP</code> @ 1670.0963a7d39fadd579768e.js:2</summary>

```js
tion _i(n,t){var r=typeof n;return!!(t=null==t?s:t)&&("number"==r||"symbol"!=r&&dn.test(n))&&n>-1&&n%1==0&&n<t}function gi(n,t,r){if(!Xo(r))return!1;var e=typeof t;ret
```
</details>

<details><summary><code>Internal host / private IP</code> @ 1670.0963a7d39fadd579768e.js:2</summary>

```js
"":t}if("string"!=typeof n)return 0===n?n:+n;n=Ht(n);var r=_n.test(n);return r||yn.test(n)?ct(n.slice(2),r?2:8):vn.test(n)?h:+n}function yf(n){return zu(n,Tf(n))}funct
```
</details>

<details><summary><code>Internal host / private IP</code> @ 1670.0963a7d39fadd579768e.js:2</summary>

```js
n 0===n?n:+n;n=Ht(n);var r=_n.test(n);return r||yn.test(n)?ct(n.slice(2),r?2:8):vn.test(n)?h:+n}function yf(n){return zu(n,Tf(n))}function df(n){return null==n?"":ou(n
```
</details>

<details><summary><code>Internal host / private IP</code> @ 1670.0963a7d39fadd579768e.js:2</summary>

```js
(n))&&G.test(n)?n.replace(K,rr):n},Br.escapeRegExp=function(n){return(n=df(n))&&rn.test(n)?n.replace(tn,"\\$&"):n},Br.every=function(n,t,r){var e=Po(n)?It:he;return r&
```
</details>

<details><summary><code>Internal host / private IP</code> @ 1670.0963a7d39fadd579768e.js:2</summary>

```js
e,Hu);var i=xf({},t.imports,e.imports,Hu),o=Rf(i),f=Yt(i,o);kt(o,function(n){if(ln.test(n))throw new xn("Invalid `imports` option passed into `_.template`")});var a,c,
```
</details>

<details><summary><code>Internal host / private IP</code> @ 2660.f5237f97f217fae19751.js:1</summary>

```js
ew RegExp(`^${E(e)}$`)}function A(e){const n=E({precision:e.precision}),t=["Z"];e.local&&t.push(""),e.offset&&t.push("([+-](?:[01]\\d|2[0-3]):[0-5]\\d)");const i=`${n}
```
</details>

<details><summary><code>Internal host / private IP</code> @ 3150.7902c205f4f7d6d9e059.js:2</summary>

```js
function(){a.unqueued--,w.queue(e,"fx").length||a.empty.fire()})})),t)if(i=t[r],ln.test(i)){if(delete t[r],o=o||"toggle"===i,i===(g?"hide":"show")){if("show"!==i||!v||
```
</details>

<details><summary><code>Internal host / private IP</code> @ 3150.7902c205f4f7d6d9e059.js:2</summary>

```js
s,a=it.get(this);if(i)a[i]&&a[i].stop&&r(a[i]);else for(i in a)a[i]&&a[i].stop&&fn.test(i)&&r(a[i]);for(i=o.length;i--;)o[i].elem!==this||null!=e&&o[i].queue!==e||(o[i
```
</details>

<details><summary><code>Internal host / private IP</code> @ 3150.7902c205f4f7d6d9e059.js:2</summary>

```js
Index:{get:function(e){var t=e.getAttribute("tabindex");return t?parseInt(t,10):yn.test(e.nodeName)||mn.test(e.nodeName)&&e.href?0:-1}}},propFix:{for:"htmlFor",class:"
```
</details>

<details><summary><code>Internal host / private IP</code> @ 3150.7902c205f4f7d6d9e059.js:2</summary>

```js
){var t=e.getAttribute("tabindex");return t?parseInt(t,10):yn.test(e.nodeName)||mn.test(e.nodeName)&&e.href?0:-1}}},propFix:{for:"htmlFor",class:"className"}}),E&&(w.p
```
</details>

<details><summary><code>Internal host / private IP</code> @ 3150.7902c205f4f7d6d9e059.js:2</summary>

```js
ce")?t.namespace.split("."):[];if(a=d=s=r=r||v,3!==r.nodeType&&8!==r.nodeType&&!Tn.test(y+w.event.triggered)&&(y.indexOf(".")>-1&&(m=y.split("."),y=m.shift(),m.sort())
```
</details>

<details><summary><code>Internal host / private IP</code> @ 3150.7902c205f4f7d6d9e059.js:2</summary>

```js
gen)/i;function qn(e,t,n,r){var i;if(Array.isArray(t))w.each(t,function(t,i){n||Sn.test(e)?r(e,i):qn(e+"["+("object"==typeof i&&null!=i?t:"")+"]",i,n,r)});else if(n||"
```
</details>

> Verify each candidate before reporting: a public/anon key (Firebase apiKey, Stripe pk_, Sentry DSN, Algolia search key) is by design client-side and is normally **not** a vulnerability. What matters is whether the key grants privileged access.

## 2. API endpoints

| Endpoint | Party | Method(s) | Client | Request parts | Hits | File:Line |
|---|---|---|---|---|---|---|
| `/json/settings` | first | ? | - | body | 29 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages` | first | GET, DELETE | - | body | 12 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/` | first | DELETE | - | body | 9 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/user-roles` | first | ? | - | body | 8 | `app.9ce541840b7470231ad5.js`:1 |
| `/json${c}/billing/plan` | first | PATCH | - | body | 8 | `billing.a458a4ed121ea803cfd7.js`:1 |
| `/json/streams/` | first | ? | - | body | 8 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/` | first | ? | - | body | 8 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/subscriptions` | first | ? | - | body | 7 | `app.9ce541840b7470231ad5.js`:1 |
| `/plans/` | first | ? | - | body | 7 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/user_uploads/` | first | ? | - | body | 7 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/help/desktop-app-install-guide` | first | ? | - | - | 6 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/help/user-groups` | first | ? | - | body | 6 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/introduction-to-channels` | first | ? | - | body | 5 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_groups/` | first | ? | - | body | 5 | `app.9ce541840b7470231ad5.js`:1 |
| `/dark` | first | ? | - | - | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/channel-folders` | first | ? | - | body | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/desktop-notifications` | first | ? | - | body | 4 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/help/follow-a-topic` | first | ? | - | body | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/mobile-notifications` | first | ? | - | body | 4 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/help/restrict-direct-messages` | first | ? | - | body | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/events` | first | ? | - | body | 4 | `436.db660eb8a29b291918da.js`:1 |
| `/json/realm/profile_fields/` | first | ? | - | - | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/light` | first | ? | - | - | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/login/` | first | ? | - | body | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/reactivate` | first | ? | - | - | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/sponsorship/` | first | ? | XMLHttpRequest | - | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/static/generated/emoji/images-` | first | ? | - | - | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/billing/` | first | ? | - | body | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/add-a-custom-linkifier` | first | ? | - | body | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/change-the-channel-description` | first | ? | - | body | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/export-your-organization` | first | ? | - | body | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/mute-a-topic` | first | ? | - | body | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/public-access-option` | first | ? | - | body | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/set-default-channels-for-new-users` | first | ? | - | body | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/integrations/` | first | ? | - | - | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots/` | first | ? | - | body, form-data | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/invites` | first | GET | - | body | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/flags` | first | ? | - | body | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm` | first | ? | - | - | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/near/` | first | ? | - | - | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/upgrade/` | first | ? | XMLHttpRequest | - | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/user_uploads` | first | ? | - | - | 3 | `app.9ce541840b7470231ad5.js`:1 |
| `/user_uploads/thumbnail/` | first | ? | - | - | 3 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/*$1` | first | ? | - | - | 2 | `436.db660eb8a29b291918da.js`:1 |
| `/accounts/password/reset/` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/api/v1/tus/` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/email_address` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/error_tracing` | first | GET | - | - | 2 | `436.db660eb8a29b291918da.js`:1 |
| `/general` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-email-visibility` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/deactivate-or-reactivate-a-user` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/deactivate-your-organization` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/emoji-reactions` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/image-video-and-website-previews` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/message-retention-policy` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/read-receipts` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/topic-notifications` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json${a}/billing/event/status` | first | GET | - | - | 2 | `billing-event-status.dc35a39a1febd3db10fa.js`:1 |
| `/json/attachments/` | first | DELETE | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/channel_folders/` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/export/realm` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/invites/` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/flags/narrow` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/render` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/domains/` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/emoji/` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/filters/` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/icon` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/logo` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/profile_fields` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_groups/${t.id}` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_groups/${t.id}` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/alert_words` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/avatar` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/muted_users/` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/presence` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/demo-organizations` | first | ? | XMLHttpRequest | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/${A.je(e.stream_id,y.NO)}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/${s().escape(o)}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/${t.path}` | first | ? | - | query-params | 1 | `6215.b6341c1da50665d7cf15.js`:1 |
| `/${t.path}` | first | ? | - | query-params | 1 | `6215.b6341c1da50665d7cf15.js`:1 |
| `/account/two_factor/` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/accounts/deactivated/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/accounts/login/subdomain/` | first | ? | XMLHttpRequest | - | 1 | `desktop-login.bc6537c2633b7d78a971.js`:1 |
| `/altcha` | first | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `/api/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/api/api-keys` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/api/v1/users/me/api_key/regenerate` | first | ? | - | headers, auth | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/apps/download/linux` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/apps/download/mac-arm64` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/apps/download/mac-intel` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/apps/download/windows` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/avatar/${e.user_id}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/avatar/${e.user_id}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/avatar/${t.user_id}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/avatar/${t.user_id}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/calls/${l}/register` | first | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/calls/${l}/register` | first | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/calls/add/register` | first | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/compatibility` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/contact-sales` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/day` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/deactivate` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/delete_topic` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/devlogin/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/emails` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/external` | first | POST | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `/features/` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/form/` | first | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `/help/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/add-a-bot-or-integration` | first | ? | - | body, form-data | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/animated-gifs` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/archive-a-channel` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/bots-overview` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/change-your-language` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/channel-permissions` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/channel-posting-policy` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/code-blocks` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/combined-feed` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/communities-directory` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-call-provider` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-default-new-user-settings` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-default-profile-pictures` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-emoticon-translations` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-home-view` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-organization-language` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-who-can-start-new-topics` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/contact-support` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/create-your-organization-profile` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/deactivate-or-reactivate-a-bot` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/deactivate-your-account` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/delete-a-message` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/delete-a-topic` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/demo-organizations` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/do-not-disturb` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/email-notifications` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/enable-moderation-requests` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/format-your-message-using-markdown` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/inbox` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/invite-new-users` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/keyboard-shortcuts` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/manage-inactive-channels` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/manage-user-groups` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/marking-messages-as-read` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/mention-a-user-or-group` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/message-a-channel-by-email` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/mute-a-channel` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/mute-a-user` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/organization-type` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/reading-conversations` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/recent-conversations` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/rename-a-topic` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/report-a-message` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/require-topics` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/resolve-a-topic` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-message-editing-and-deletion` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-moving-messages` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-name-and-email-changes` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-permissions-of-new-members` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-wildcard-mentions` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/star-a-message` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/status-and-availability` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/supported-browsers` | first | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/view-your-mentions` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/help/zulip-cloud-billing` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/history` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/integrations/category/` | first | ? | - | - | 1 | `integrations.c56e78ec753c515cc8a0.js`:1 |
| `/json${c}/billing/session/start_card_update_session` | first | ? | - | - | 1 | `billing.a458a4ed121ea803cfd7.js`:1 |
| `/json${h.billing_base_url}/billing/upgrade` | first | ? | - | - | 1 | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `/json${h.billing_base_url}/upgrade/session/start_card_update_session` | first | ? | - | - | 1 | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `/json${o}/billing/sponsorship` | first | POST | - | body | 1 | `sponsorship.776dcb8754701f66c4e8.js`:1 |
| `/json/analytics/chart_data` | first | GET | - | body | 1 | `stats.01163dea88a828750ffc.js`:1 |
| `/json/attachments` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots/${encodeURIComponent(t)}/api_key/regenerate` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots/${e}/api_key` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots/${e}/api_key` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/${l}/create` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/${l}/create` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/add/create` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/bigbluebutton/create` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/constructorgroups/create` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/nextcloud_talk/create` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/channel_folders` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/channel_folders/create` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/default_streams` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/export/realm/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/export/realm/consents` | first | DELETE | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/fetch_api_key` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/invites/multiuse` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/invites/multiuse/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${a.target_id}` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${a.target_id}` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${e}/read_receipts` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${e}/read_receipts` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${e}/typing` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${e}/typing` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/configure_user_group_settings/read_receipts` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/configure_user_group_settings/typing` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/matches_narrow` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/summary` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/deactivate` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/domains` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/filters` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/import/status/${l}` | first | GET | - | - | 1 | `slack-import.9d382330598f81a7ef6f.js`:1 |
| `/json/realm/import/status/${l}` | first | GET | - | - | 1 | `slack-import.9d382330598f81a7ef6f.js`:1 |
| `/json/realm/linkifiers` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/playgrounds` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/playgrounds/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/subdomain/` | first | GET | - | - | 1 | `8025.fa07f61f67f8848dceb1.js`:1 |
| `/json/realm/test_welcome_bot_custom_message` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/user_settings_defaults` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/register` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/reminders` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/reminders/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/saved_snippets` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/saved_snippets/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/saved_snippets/${e}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/saved_snippets/${e}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/scheduled_messages` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/scheduled_messages/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/self-hosted-billing` | first | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${e.stream_id}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${e.stream_id}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${e}/members` | first | GET | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${e}/members` | first | GET | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${t}` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${t}` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/configure_user_group_settings/members` | first | GET | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/muted_topics` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/submessage` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/thumbnail/status/${e}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/thumbnail/status/${e}` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/thumbnail/status/configure_user_group_settings` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/typing` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_groups/create` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_topics` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/${e}/channels` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/${e}/channels` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/configure_user_group_settings/channels` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/` | first | DELETE | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/onboarding_steps` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/profile_data` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/status` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/subscriptions/properties` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/zcommand` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/members` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/metrics` | first | ? | - | - | 1 | `katex_server.js`:2 |
| `/night` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/personal` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/ping` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/poll` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/reactions` | first | DELETE | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/register/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/report` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/resend` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/self-hosted-billing/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/static/audio/notification_sounds/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/stats` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/team/` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/todo` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/topics` | first | DELETE | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/user_uploads/download/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com//help/self-hosted-billing` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/apps/` | first | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/development-community/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/collaborative-to-do-lists` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/contact-support` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/create-a-poll` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/invite-new-users#create-a-reusable-invitation-link` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/support-zulip-project` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `${c}/billing/?success_message=` | unresolved-base | ? | - | - | 6 | `billing.a458a4ed121ea803cfd7.js`:1 |
| `${c}/billing/` | unresolved-base | ? | - | - | 1 | `billing.a458a4ed121ea803cfd7.js`:1 |
| `${c}/upgrade/?success_message=` | unresolved-base | ? | - | - | 1 | `billing.a458a4ed121ea803cfd7.js`:1 |
| `${function(t){return`${function(t){const e=t.protocol?`${t.protocol}:`:"",n=t.port?`:${t.port}`:"";return`${e}//${t.host}${n}${t.path?`/${t.path}`:""}/api/`}(t)}${t.projectId}/envelope/`}(e)}?${function(t,e){const n={sentry_version:"7"};return t.publicKey&&(n.sentry_key=t.publicKey),e&&(n.sentry_client=`${e.name}/${e.version}`),new URLSearchParams(n).toString()}(e,o)}` | unresolved-base | ? | - | query-params | 1 | `6215.b6341c1da50665d7cf15.js`:1 |
| `${h.billing_base_url}/billing/event_status/?stripe_invoice_id=${t.stripe_invoice_id}` | unresolved-base | ? | - | - | 1 | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `${h.billing_base_url}/customer_portal/?manual_license_management=true&tier=${h.tier}&setup_payment_by_invoice=true` | unresolved-base | ? | XMLHttpRequest | - | 1 | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `${h.billing_base_url}/upgrade/` | unresolved-base | ? | - | - | 1 | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `http://www.w3.org/2000/svg` | third | ? | - | body | 40 | `7018.30d28337a85dfd6155b1.js`:2 |
| `http://www.w3.org/1998/Math/MathML` | third | ? | - | - | 11 | `8413.55cc9ce65475198524f9.js`:2 |
| `http://www.w3.org/1999/xhtml` | third | ? | - | - | 6 | `7018.30d28337a85dfd6155b1.js`:2 |
| `http://www.w3.org/1999/xlink` | third | ? | - | - | 5 | `7018.30d28337a85dfd6155b1.js`:2 |
| `http://json-schema.org/draft-04/schema#` | third | ? | - | - | 2 | `2660.f5237f97f217fae19751.js`:1 |
| `http://json-schema.org/draft-07/schema#` | third | ? | - | - | 2 | `2660.f5237f97f217fae19751.js`:1 |
| `http://www.w3.org/2000/xmlns/` | third | ? | - | - | 2 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://altcha.org/` | third | ? | - | - | 2 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://chart-studio.plotly.com` | third | ? | - | - | 2 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/fill-rule` | third | ? | - | - | 2 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts` | third | ? | - | - | 2 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://formatjs.github.io/docs/react-intl#runtime-requirements` | third | ? | - | - | 2 | `7820.868203aba2a3f30382bf.js`:1 |
| `https://github.com/zulip/${t` | third | ? | - | - | 2 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/self-hosted/commits?author=${a}` | third | ? | - | - | 2 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/zulip/issues/{id` | third | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `https://github.com/zulip/zulip/pull/{id` | third | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `https://json-schema.org/draft/2020-12/schema` | third | ? | - | - | 2 | `2660.f5237f97f217fae19751.js`:1 |
| `https://npms.io/search?q=ponyfill.` | third | ? | - | - | 2 | `1670.0963a7d39fadd579768e.js`:2 |
| `https://play.rust-lang.org/?code={code` | third | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `https://plotly.com/javascript/animations/` | third | ? | - | - | 2 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://www.googletagmanager.com/gtag/js?id=` | third | ? | - | - | 2 | `2660.f5237f97f217fae19751.js`:1 |
| `/proc/self/fd` | third | ? | - | - | 1 | `katex_server.js`:2 |
| `/proc/self/limits` | third | ? | - | - | 1 | `katex_server.js`:2 |
| `/proc/self/status` | third | ? | - | - | 1 | `katex_server.js`:2 |
| `http://[${t.value}]` | third | ? | - | - | 1 | `2660.f5237f97f217fae19751.js`:1 |
| `http://[draft-2020-12]` | third | ? | - | - | 1 | `2660.f5237f97f217fae19751.js`:1 |
| `http://\\rangle` | third | ? | - | - | 1 | `katex_server.js`:2 |
| `http://www.w3.org/TR/css3-color/#svg-color` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `http://www.w3.org/XML/1998/namespace` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://api.giphy.com/v1/gifs` | third | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.giphy.com/v1/gifs/search` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.giphy.com/v1/gifs/trending` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.klipy.com/v2` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.klipy.com/v2/featured` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.klipy.com/v2/search` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://cdn.plot.ly/un/` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://chart-studio.plotly.com/settings` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://docs.sentry.io/platforms/javascript/best-practices/browser-extensions/` | third | ? | - | - | 1 | `6215.b6341c1da50665d7cf15.js`:1 |
| `https://en.gravatar.com/` | third | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://example.com/path/%(username` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://formatjs.github.io/docs/getting-started/message-distribution` | third | ? | - | - | 1 | `7820.868203aba2a3f30382bf.js`:1 |
| `https://formatjs.github.io/docs/react-intl/api#intlshape` | third | ? | - | - | 1 | `7820.868203aba2a3f30382bf.js`:1 |
| `https://formatjs.github.io/docs/tooling/babel-plugin` | third | ? | - | - | 1 | `7820.868203aba2a3f30382bf.js`:1 |
| `https://formatjs.github.io/docs/tooling/linter#enforce-id` | third | ? | - | - | 1 | `7820.868203aba2a3f30382bf.js`:1 |
| `https://formatjs.github.io/docs/tooling/ts-transformer` | third | ? | - | - | 1 | `7820.868203aba2a3f30382bf.js`:1 |
| `https://github.com/${e.github_username` | third | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/${e.github_username}` | third | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#wiki-tables` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://github.com/ashtuchkin/iconv-lite/wiki/Node-v4-compatibility` | third | ? | - | - | 1 | `katex_server.js`:2 |
| `https://github.com/ashtuchkin/iconv-lite/wiki/Use-Buffers-when-decoding` | third | ? | - | - | 1 | `katex_server.js`:2 |
| `https://github.com/d3/d3-format/tree/v1.4.5#d3-format` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://github.com/d3/d3-time-format/tree/v2.2.3#locale_format` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://github.com/transloadit/uppy/issues/1042` | third | ? | - | - | 1 | `4036.812fedda9a99929a355f.js`:2 |
| `https://github.com/zloirock/core-js` | third | ? | - | - | 1 | `8050.5a6eab020aeb7e241eca.js`:1 |
| `https://github.com/zloirock/core-js/blob/v3.49.0/LICENSE` | third | ? | - | - | 1 | `8050.5a6eab020aeb7e241eca.js`:1 |
| `https://github.com/zulip/${e` | third | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/${e}` | third | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/zulip#readme` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://github.com/zulip/zulip-flutter/releases/latest` | third | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/zulip-mobile/releases/latest` | third | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://handlebarsjs.com/api-reference/runtime-options.html#options-to-control-prototype-access` | third | ? | - | - | 1 | `8050.5a6eab020aeb7e241eca.js`:1 |
| `https://hostname.example.com` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://itunes.apple.com/us/app/zulip/id1203036395` | third | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://play.google.com/store/apps/details?id=com.zulipmobile` | third | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://player.vimeo.com/video/` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://plotly.com/` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://plotly.com/javascript/plotlyjs-events/#event-data.` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://secure.gravatar.com` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://secure.gravatar.com/avatar/` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://svelte.dev/e/effect_in_teardown` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/effect_in_unowned_derived` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/effect_orphan` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/effect_update_depth_exceeded` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/hydration_failed` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/hydration_mismatch` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/lifecycle_outside_component` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/props_invalid_value` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/state_descriptors_fixed` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/state_prototype_fixed` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/state_unsafe_mutation` | third | ? | - | - | 1 | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://tenor.googleapis.com/v2` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://tenor.googleapis.com/v2/featured` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://tenor.googleapis.com/v2/search` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://uppy.io` | third | ? | - | - | 1 | `9673.a285a8958157ead406df.js`:2 |
| `https://uppy.io/docs/tus/#limit-0` | third | ? | - | - | 1 | `4036.812fedda9a99929a355f.js`:2 |
| `https://uppy.io/docs/uppy/#allowMultipleUploads-true` | third | ? | - | - | 1 | `9673.a285a8958157ead406df.js`:2 |
| `https://www.youtube.com/embed/` | third | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.org` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/latest/overview/release-lifecycle.html#upgrade-nag` | third | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/latest/production/email.html` | third | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/latest/production/gif-picker-integrations.html` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/latest/translating/translating.html` | third | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/stable/production/upgrade.html` | third | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |

### Other URLs and paths

_None._

## 3. GraphQL operations

_None found._

## 4. DOM-XSS sinks

| Sink | Count | Nearby sources | File:Line |
|---|---|---|---|
| `location assignment` | 1 | location.hash, location.search | `billing.a458a4ed121ea803cfd7.js`:1 |
| `location assignment` | 1 | location.hash, location.search | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `location assignment` | 1 | location.hash | `8025.fa07f61f67f8848dceb1.js`:1 |
| `postMessage` | 4 | event.data | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `message listener` | 1 | event.data | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `dangerouslySetInnerHTML` | 2 | event.data | `8413.55cc9ce65475198524f9.js`:2 |
| `dangerouslySetInnerHTML` | 2 | event.data | `9673.a285a8958157ead406df.js`:2 |
| `location assignment` | 1 | location.search | `desktop-login.bc6537c2633b7d78a971.js`:1 |
| `new Function` | 1 | - | `2660.f5237f97f217fae19751.js`:1 |
| `innerHTML` | 2 | - | `3150.7902c205f4f7d6d9e059.js`:2 |
| `new Function` | 1 | - | `3380.ab25157d87e1e561d46c.js`:1 |
| `innerHTML` | 1 | - | `4036.812fedda9a99929a355f.js`:2 |
| `location assignment` | 1 | - | `4036.812fedda9a99929a355f.js`:2 |
| `innerHTML` | 2 | - | `420.288148b70ab4f3988e8c.js`:2 |
| `new Function` | 1 | - | `5394.2d1f16e5176b173b6f6b.js`:1 |
| `innerHTML` | 3 | - | `6108.1b0f4b4bedcf69b4b375.js`:2 |
| `innerHTML` | 1 | - | `6117.e31c8473d9f44d30338e.js`:1 |
| `new Function` | 1 | - | `6215.b6341c1da50665d7cf15.js`:1 |
| `innerHTML` | 3 | - | `7018.30d28337a85dfd6155b1.js`:2 |
| `location assignment` | 1 | - | `7018.30d28337a85dfd6155b1.js`:2 |
| `location assignment` | 1 | - | `7820.868203aba2a3f30382bf.js`:1 |
| `innerHTML` | 2 | - | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `innerHTML` | 11 | - | `8413.55cc9ce65475198524f9.js`:2 |
| `outerHTML` | 1 | - | `8413.55cc9ce65475198524f9.js`:2 |
| `new Function` | 1 | - | `8413.55cc9ce65475198524f9.js`:2 |
| `insertAdjacentHTML` | 1 | - | `8413.55cc9ce65475198524f9.js`:2 |
| `innerHTML` | 1 | - | `8626.02ea5aafd07f3ec0f1cf.js`:1 |
| `innerHTML` | 2 | - | `9673.a285a8958157ead406df.js`:2 |
| `innerHTML` | 1 | - | `9947.280df15bcf07df29e234.js`:1 |
| `innerHTML` | 4 | - | `app.9ce541840b7470231ad5.js`:1 |
| `jQuery html()` | 4 | - | `app.9ce541840b7470231ad5.js`:1 |
| `location assignment` | 18 | - | `app.9ce541840b7470231ad5.js`:1 |
| `eval` | 1 | - | `katex_server.js`:2 |
| `new Function` | 1 | - | `katex_server.js`:2 |
| `innerHTML` | 1 | - | `stats.01163dea88a828750ffc.js`:1 |

Rows with a nearby source are the ones worth manual review.

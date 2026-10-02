# JavaScript Recon Report

- **Source:** `validation-zulip\js-loot\js`
- **Generated:** 2026-10-01 20:46:11
- **Files analysed:** 64 (11,120,196 bytes)

- **First-party domains:** `zulip.com`
- **Denominator:** 375 total · 274 first-party · 94 third-party SDK · 7 unresolved base
- **API-shaped only:** 56 total · 44 first-party · 11 third-party SDK · 1 unresolved base
- Quote coverage against the **first-party** number, and say which number you quoted. Nothing was dropped: every row is in `recon.json` with its `party` field.

| Finding | Count |
|---|---|
| API-looking endpoints | 56 |
|   ...of those, first-party | 44 |
|   ...of those, third-party SDK | 11 |
|   ...of those, unresolved base | 1 |
| Other URLs / paths | 319 |
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
| `/json/users/` | first | ? | - | body | 8 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/subscriptions` | first | ? | - | body | 7 | `app.9ce541840b7470231ad5.js`:1 |
| `/login/` | first | ? | - | body | 4 | `app.9ce541840b7470231ad5.js`:1 |
| `/accounts/password/reset/` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/api/v1/tus/` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/export/realm` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/alert_words` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/avatar` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/muted_users/` | first | ? | - | - | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/presence` | first | ? | - | body | 2 | `app.9ce541840b7470231ad5.js`:1 |
| `/account/two_factor/` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/accounts/deactivated/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/accounts/login/subdomain/` | first | ? | XMLHttpRequest | - | 1 | `desktop-login.bc6537c2633b7d78a971.js`:1 |
| `/api/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/api/api-keys` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/api/v1/users/me/api_key/regenerate` | first | ? | - | headers, auth | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/apps/download/linux` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/apps/download/mac-arm64` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/apps/download/mac-intel` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/apps/download/windows` | first | ? | - | - | 1 | `6117.e31c8473d9f44d30338e.js`:1 |
| `/calls/${l}/register` | first | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/calls/${l}/register` | first | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/calls/add/register` | first | ? | XMLHttpRequest | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json${c}/billing/session/start_card_update_session` | first | ? | - | - | 1 | `billing.a458a4ed121ea803cfd7.js`:1 |
| `/json${h.billing_base_url}/upgrade/session/start_card_update_session` | first | ? | - | - | 1 | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `/json/export/realm/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/export/realm/consents` | first | DELETE | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/import/status/${l}` | first | GET | - | - | 1 | `slack-import.9d382330598f81a7ef6f.js`:1 |
| `/json/realm/import/status/${l}` | first | GET | - | - | 1 | `slack-import.9d382330598f81a7ef6f.js`:1 |
| `/json/register` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/${e}/channels` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/${e}/channels` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/configure_user_group_settings/channels` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/` | first | DELETE | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/onboarding_steps` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/profile_data` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/status` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/json/users/me/subscriptions/properties` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/register/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/report` | first | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `/user_uploads/download/` | first | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `${function(t){return`${function(t){const e=t.protocol?`${t.protocol}:`:"",n=t.port?`:${t.port}`:"";return`${e}//${t.host}${n}${t.path?`/${t.path}`:""}/api/`}(t)}${t.projectId}/envelope/`}(e)}?${function(t,e){const n={sentry_version:"7"};return t.publicKey&&(n.sentry_key=t.publicKey),e&&(n.sentry_client=`${e.name}/${e.version}`),new URLSearchParams(n).toString()}(e,o)}` | unresolved-base | ? | - | query-params | 1 | `6215.b6341c1da50665d7cf15.js`:1 |
| `https://npms.io/search?q=ponyfill.` | third | ? | - | - | 2 | `1670.0963a7d39fadd579768e.js`:2 |
| `https://api.giphy.com/v1/gifs` | third | ? | - | body | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.giphy.com/v1/gifs/search` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.giphy.com/v1/gifs/trending` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.klipy.com/v2` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.klipy.com/v2/featured` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://api.klipy.com/v2/search` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://chart-studio.plotly.com/settings` | third | ? | - | - | 1 | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://tenor.googleapis.com/v2` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://tenor.googleapis.com/v2/featured` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |
| `https://tenor.googleapis.com/v2/search` | third | ? | - | - | 1 | `app.9ce541840b7470231ad5.js`:1 |

### Other URLs and paths

<details><summary>Show 319 entries</summary>

| Value | Kind | File:Line |
|---|---|---|
| `${c}/billing/` | template-literal | `billing.a458a4ed121ea803cfd7.js`:1 |
| `${c}/billing/?success_message=` | template-literal | `billing.a458a4ed121ea803cfd7.js`:1 |
| `${c}/upgrade/?success_message=` | template-literal | `billing.a458a4ed121ea803cfd7.js`:1 |
| `${h.billing_base_url}/billing/event_status/?stripe_invoice_id=${t.stripe_invoice_id}` | template-literal | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `${h.billing_base_url}/customer_portal/?manual_license_management=true&tier=${h.tier}&setup_payment_by_invoice=true` | template-literal | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `${h.billing_base_url}/upgrade/` | template-literal | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `/${A.je(e.stream_id,y.NO)}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/${s().escape(o)}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/${t.path}` | relative-path | `6215.b6341c1da50665d7cf15.js`:1 |
| `/${t.path}` | template-path | `6215.b6341c1da50665d7cf15.js`:1 |
| `/*$1` | relative-path | `436.db660eb8a29b291918da.js`:1 |
| `/altcha` | relative-path | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `/avatar/${e.user_id}` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/avatar/${e.user_id}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/avatar/${t.user_id}` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/avatar/${t.user_id}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/billing/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/compatibility` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/contact-sales` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/dark` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/day` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/deactivate` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/delete_topic` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/devlogin/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/email_address` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/emails` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/error_tracing` | relative-path | `436.db660eb8a29b291918da.js`:1 |
| `/external` | relative-path | `7018.30d28337a85dfd6155b1.js`:2 |
| `/features/` | relative-path | `6117.e31c8473d9f44d30338e.js`:1 |
| `/form/` | relative-path | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `/general` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/add-a-bot-or-integration` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/add-a-custom-linkifier` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/animated-gifs` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/archive-a-channel` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/bots-overview` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/change-the-channel-description` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/change-your-language` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/channel-folders` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/channel-permissions` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/channel-posting-policy` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/code-blocks` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/combined-feed` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/communities-directory` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-call-provider` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-default-new-user-settings` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-default-profile-pictures` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-email-visibility` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-emoticon-translations` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-home-view` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-organization-language` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/configure-who-can-start-new-topics` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/contact-support` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/create-your-organization-profile` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/deactivate-or-reactivate-a-bot` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/deactivate-or-reactivate-a-user` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/deactivate-your-account` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/deactivate-your-organization` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/delete-a-message` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/delete-a-topic` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/demo-organizations` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/desktop-app-install-guide` | relative-path | `6117.e31c8473d9f44d30338e.js`:1 |
| `/help/desktop-notifications` | relative-path | `6117.e31c8473d9f44d30338e.js`:1 |
| `/help/do-not-disturb` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/email-notifications` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/emoji-reactions` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/enable-moderation-requests` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/export-your-organization` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/follow-a-topic` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/format-your-message-using-markdown` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/image-video-and-website-previews` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/inbox` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/introduction-to-channels` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/invite-new-users` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/keyboard-shortcuts` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/manage-inactive-channels` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/manage-user-groups` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/marking-messages-as-read` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/mention-a-user-or-group` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/message-a-channel-by-email` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/message-retention-policy` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/mobile-notifications` | relative-path | `6117.e31c8473d9f44d30338e.js`:1 |
| `/help/mute-a-channel` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/mute-a-topic` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/mute-a-user` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/organization-type` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/public-access-option` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/read-receipts` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/reading-conversations` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/recent-conversations` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/rename-a-topic` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/report-a-message` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/require-topics` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/resolve-a-topic` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-direct-messages` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-message-editing-and-deletion` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-moving-messages` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-name-and-email-changes` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-permissions-of-new-members` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/restrict-wildcard-mentions` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/set-default-channels-for-new-users` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/star-a-message` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/status-and-availability` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/supported-browsers` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/topic-notifications` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/user-groups` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/user-roles` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/view-your-mentions` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/help/zulip-cloud-billing` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/history` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/integrations/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/integrations/category/` | relative-path | `integrations.c56e78ec753c515cc8a0.js`:1 |
| `/json${a}/billing/event/status` | relative-path | `billing-event-status.dc35a39a1febd3db10fa.js`:1 |
| `/json${c}/billing/plan` | relative-path | `billing.a458a4ed121ea803cfd7.js`:1 |
| `/json${h.billing_base_url}/billing/upgrade` | relative-path | `upgrade.1d05e463a7988d8dae6f.js`:1 |
| `/json${o}/billing/sponsorship` | relative-path | `sponsorship.776dcb8754701f66c4e8.js`:1 |
| `/json/analytics/chart_data` | relative-path | `stats.01163dea88a828750ffc.js`:1 |
| `/json/attachments` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/attachments/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots/${encodeURIComponent(t)}/api_key/regenerate` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots/${e}/api_key` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/bots/${e}/api_key` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/${l}/create` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/${l}/create` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/add/create` | template-literal | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/bigbluebutton/create` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/constructorgroups/create` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/calls/nextcloud_talk/create` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/channel_folders` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/channel_folders/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/channel_folders/create` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/default_streams` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/events` | relative-path | `436.db660eb8a29b291918da.js`:1 |
| `/json/fetch_api_key` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/invites` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/invites/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/invites/multiuse` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/invites/multiuse/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${a.target_id}` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${a.target_id}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${e}/read_receipts` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${e}/read_receipts` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${e}/typing` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/${e}/typing` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/configure_user_group_settings/read_receipts` | template-literal | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/configure_user_group_settings/typing` | template-literal | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/flags` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/flags/narrow` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/matches_narrow` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/render` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/messages/summary` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/deactivate` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/domains` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/domains/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/emoji/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/filters` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/filters/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/icon` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/linkifiers` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/logo` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/playgrounds` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/playgrounds/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/profile_fields` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/profile_fields/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/subdomain/` | relative-path | `8025.fa07f61f67f8848dceb1.js`:1 |
| `/json/realm/test_welcome_bot_custom_message` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/realm/user_settings_defaults` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/reminders` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/reminders/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/saved_snippets` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/saved_snippets/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/saved_snippets/${e}` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/saved_snippets/${e}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/scheduled_messages` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/scheduled_messages/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/self-hosted-billing` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${e.stream_id}` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${e.stream_id}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${e}/members` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${e}/members` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${t}` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/${t}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/configure_user_group_settings/members` | template-literal | `app.9ce541840b7470231ad5.js`:1 |
| `/json/streams/muted_topics` | template-literal | `app.9ce541840b7470231ad5.js`:1 |
| `/json/submessage` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/thumbnail/status/${e}` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/thumbnail/status/${e}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/thumbnail/status/configure_user_group_settings` | template-literal | `app.9ce541840b7470231ad5.js`:1 |
| `/json/typing` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_groups/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_groups/${t.id}` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_groups/${t.id}` | template-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_groups/create` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/user_topics` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/json/zcommand` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/light` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/members` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/metrics` | relative-path | `katex_server.js`:2 |
| `/near/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/night` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/personal` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/ping` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/plans/` | relative-path | `6117.e31c8473d9f44d30338e.js`:1 |
| `/poll` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/proc/self/fd` | relative-path | `katex_server.js`:2 |
| `/proc/self/limits` | relative-path | `katex_server.js`:2 |
| `/proc/self/status` | relative-path | `katex_server.js`:2 |
| `/reactions` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/reactivate` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/resend` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/self-hosted-billing/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/sponsorship/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/static/audio/notification_sounds/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/static/generated/emoji/images-` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/stats` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/team/` | relative-path | `6117.e31c8473d9f44d30338e.js`:1 |
| `/todo` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/topics` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/upgrade/` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/user_uploads` | relative-path | `app.9ce541840b7470231ad5.js`:1 |
| `/user_uploads/` | relative-path | `6117.e31c8473d9f44d30338e.js`:1 |
| `/user_uploads/thumbnail/` | relative-path | `6117.e31c8473d9f44d30338e.js`:1 |
| `http://[${t.value}]` | template-literal | `2660.f5237f97f217fae19751.js`:1 |
| `http://[draft-2020-12]` | template-literal | `2660.f5237f97f217fae19751.js`:1 |
| `http://\\rangle` | template-literal | `katex_server.js`:2 |
| `http://json-schema.org/draft-04/schema#` | absolute-url | `2660.f5237f97f217fae19751.js`:1 |
| `http://json-schema.org/draft-07/schema#` | absolute-url | `2660.f5237f97f217fae19751.js`:1 |
| `http://www.w3.org/1998/Math/MathML` | absolute-url | `8413.55cc9ce65475198524f9.js`:2 |
| `http://www.w3.org/1999/xhtml` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `http://www.w3.org/1999/xlink` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `http://www.w3.org/2000/svg` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `http://www.w3.org/2000/xmlns/` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `http://www.w3.org/TR/css3-color/#svg-color` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `http://www.w3.org/XML/1998/namespace` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://altcha.org/` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://cdn.plot.ly/un/` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://chart-studio.plotly.com` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/fill-rule` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://docs.sentry.io/platforms/javascript/best-practices/browser-extensions/` | absolute-url | `6215.b6341c1da50665d7cf15.js`:1 |
| `https://en.gravatar.com/` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://example.com/path/%(username` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://formatjs.github.io/docs/getting-started/message-distribution` | absolute-url | `7820.868203aba2a3f30382bf.js`:1 |
| `https://formatjs.github.io/docs/react-intl#runtime-requirements` | absolute-url | `7820.868203aba2a3f30382bf.js`:1 |
| `https://formatjs.github.io/docs/react-intl/api#intlshape` | absolute-url | `7820.868203aba2a3f30382bf.js`:1 |
| `https://formatjs.github.io/docs/tooling/babel-plugin` | absolute-url | `7820.868203aba2a3f30382bf.js`:1 |
| `https://formatjs.github.io/docs/tooling/linter#enforce-id` | absolute-url | `7820.868203aba2a3f30382bf.js`:1 |
| `https://formatjs.github.io/docs/tooling/ts-transformer` | absolute-url | `7820.868203aba2a3f30382bf.js`:1 |
| `https://github.com/${e.github_username` | absolute-url | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/${e.github_username}` | template-literal | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#wiki-tables` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://github.com/ashtuchkin/iconv-lite/wiki/Node-v4-compatibility` | absolute-url | `katex_server.js`:2 |
| `https://github.com/ashtuchkin/iconv-lite/wiki/Use-Buffers-when-decoding` | absolute-url | `katex_server.js`:2 |
| `https://github.com/d3/d3-format/tree/v1.4.5#d3-format` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://github.com/d3/d3-time-format/tree/v2.2.3#locale_format` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://github.com/transloadit/uppy/issues/1042` | absolute-url | `4036.812fedda9a99929a355f.js`:2 |
| `https://github.com/zloirock/core-js` | absolute-url | `8050.5a6eab020aeb7e241eca.js`:1 |
| `https://github.com/zloirock/core-js/blob/v3.49.0/LICENSE` | absolute-url | `8050.5a6eab020aeb7e241eca.js`:1 |
| `https://github.com/zulip/${e` | absolute-url | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/${e}` | template-literal | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/${t` | absolute-url | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/self-hosted/commits?author=${a}` | template-literal | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/zulip#readme` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://github.com/zulip/zulip-flutter/releases/latest` | absolute-url | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/zulip-mobile/releases/latest` | absolute-url | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://github.com/zulip/zulip/issues/{id` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://github.com/zulip/zulip/pull/{id` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://handlebarsjs.com/api-reference/runtime-options.html#options-to-control-prototype-access` | absolute-url | `8050.5a6eab020aeb7e241eca.js`:1 |
| `https://hostname.example.com` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://itunes.apple.com/us/app/zulip/id1203036395` | absolute-url | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://json-schema.org/draft/2020-12/schema` | absolute-url | `2660.f5237f97f217fae19751.js`:1 |
| `https://play.google.com/store/apps/details?id=com.zulipmobile` | absolute-url | `6117.e31c8473d9f44d30338e.js`:1 |
| `https://play.rust-lang.org/?code={code` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://player.vimeo.com/video/` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://plotly.com/` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://plotly.com/javascript/animations/` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://plotly.com/javascript/plotlyjs-events/#event-data.` | absolute-url | `7018.30d28337a85dfd6155b1.js`:2 |
| `https://secure.gravatar.com` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://secure.gravatar.com/avatar/` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://svelte.dev/e/effect_in_teardown` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/effect_in_unowned_derived` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/effect_orphan` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/effect_update_depth_exceeded` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/hydration_failed` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/hydration_mismatch` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/lifecycle_outside_component` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/props_invalid_value` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/state_descriptors_fixed` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/state_prototype_fixed` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://svelte.dev/e/state_unsafe_mutation` | absolute-url | `8119.7b2908f7f97f8e5350b5.js`:1 |
| `https://uppy.io` | absolute-url | `9673.a285a8958157ead406df.js`:2 |
| `https://uppy.io/docs/tus/#limit-0` | absolute-url | `4036.812fedda9a99929a355f.js`:2 |
| `https://uppy.io/docs/uppy/#allowMultipleUploads-true` | absolute-url | `9673.a285a8958157ead406df.js`:2 |
| `https://www.googletagmanager.com/gtag/js?id=` | absolute-url | `2660.f5237f97f217fae19751.js`:1 |
| `https://www.youtube.com/embed/` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com//help/self-hosted-billing` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/apps/` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/development-community/` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/collaborative-to-do-lists` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/contact-support` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/create-a-poll` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/demo-organizations` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/invite-new-users#create-a-reusable-invitation-link` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.com/help/support-zulip-project` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.org` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/latest/overview/release-lifecycle.html#upgrade-nag` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/latest/production/email.html` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/latest/production/gif-picker-integrations.html` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/latest/translating/translating.html` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |
| `https://zulip.readthedocs.io/en/stable/production/upgrade.html` | absolute-url | `app.9ce541840b7470231ad5.js`:1 |

</details>

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

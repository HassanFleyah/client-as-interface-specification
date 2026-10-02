"""Classification rule under evaluation in Section 6.2 — extracted verbatim.

This file is the rule itself, lifted unchanged from the extractor so the tiers reported
in Section 6.2 can be inspected and re-derived rather than taken on trust. It is not
the extractor: running it reproduces no endpoint list. The original classifier was
`bool(API_HINT.search(value))` and nothing else; the repaired one is
`classify_endpoint`, below.

Measured against the Jellyfin 12.1 OpenAPI specification:

                                   as emitted   absolute URLs set aside   recall/243
    original  API_HINT only            32.9%              38.7%              9.5%
    repaired  classify_endpoint        45.3%              62.4%             98.8%
    repaired, request-construction tier only: 90.8% precision at 40.3% recall

"""
import re

# ---------------------------------------------------------------- original rule
API_HINT = re.compile(
    r"""(?:^|/)(?:api|apis|v[0-9]{1,2}|rest|graphql|gql|rpc|auth|oauth2?|sso|
        token|session|login|logout|register|signup|signin|password|otp|mfa|
        user|users|account|accounts|profile|me|customer|client|
        admin|internal|private|manage|management|dashboard|
        payment|payments|pay|wallet|withdraw|deposit|transfer|transaction|
        order|orders|trade|trading|balance|kyc|verify|verification|
        upload|download|file|files|document|export|import|report|
        webhook|callback|notify|search|query|config|settings|feature)(?:/|$|\?)""",
    re.I | re.X)

# ---------------------------------------------------------------- repaired rule
ROUTER_DEF = re.compile(
    r"""createBrowserRouter|createHashRouter|createMemoryRouter|RouterProvider
      | \buseRoutes\b | <\s*Route\b | \brouteTree\b | \bcreateRouter\b
      | \bdefineRoutes?\b | vue-router | \$router\b | \bRoutes\s*>
      | \bpath\s*:\s*["'`][^"'`]*["'`]\s*,\s*(?:element|lazy|[Cc]omponent|children|loader|handle)\s*:
      | (?:element|lazy|[Cc]omponent)\s*:\s*[^,}]{0,80}\bpath\s*:
      # Navigation rather than request construction. Measured: the first version of
      # this pattern caught none of the 35 router-path false positives, which appear
      # as Link targets, navigate() calls and route-constant arrays, not as route
      # table definitions.
      | \bto\s*:\s*["'`]
      | \bnavigate\s*\(
      | \bhistory\s*\.\s*push\s*\(
      | \brouter\s*\.\s*(?:push|replace)\s*\(
      | \bredirect\s*\(\s*["'`]
      | \bpaths\s*:\s*\[""",
    re.I | re.X)

# Structure that indicates a server route independently of its nouns.
API_STRUCTURE = re.compile(
    r"""(?:^|/)(?:api|apis|rest|graphql|gql|rpc)(?:/|$)   # explicit api namespace
      | (?:^|/)v[0-9]{1,2}(?:\.[0-9]{1,2})?(?:/|$)        # version segment
      | \{[^}]{1,40}\}                                    # {id} template
      | :[A-Za-z_]\w*(?:/|$)                              # :id template
      | \.(?:json|xml)(?:$|\?)""",
    re.I | re.X)

API_STRUCTURE = re.compile(
    r"""(?:^|/)(?:api|apis|rest|graphql|gql|rpc)(?:/|$)   # explicit api namespace
      | (?:^|/)v[0-9]{1,2}(?:\.[0-9]{1,2})?(?:/|$)        # version segment
      | \{[^}]{1,40}\}                                    # {id} template
      | :[A-Za-z_]\w*(?:/|$)                              # :id template
      | \.(?:json|xml)(?:$|\?)""",
    re.I | re.X)

def classify_endpoint(value, clients, methods, parts, context):
    """Return (api_like, api_evidence).

    Default is INCLUDE. Only explicit router-definition evidence excludes a path,
    because discarding on absence of evidence is what produced 9.5% recall against
    a published specification. Callers that need a high-precision subset should
    filter on api_evidence == "request-construction".
    """
    if clients:
        return True, "request-construction"
    real_methods = [m for m in (methods or []) if not m.endswith("?")]
    if real_methods:
        return True, "request-construction"
    ctx = context or ""
    if ROUTER_DEF.search(ctx):
        return False, "router-definition"
    if API_STRUCTURE.search(value) or API_HINT.search(value):
        return True, "structural"
    if parts:
        return True, "structural"
    return True, "none"


if __name__ == '__main__':
    cases = [
        ('/Items/{itemId}/Images', ['fetch'], ['GET'], [], 'fetch("/Items/")'),
        ('/dashboard/users',       [],        [],      [], '(V.A,{to:"/dashboard/users",children:['),
        ('/Artists/{name}',        [],        [],      [], 'x="/Artists/".concat(n)'),
    ]
    for value, clients, methods, parts, ctx in cases:
        print(f'{value:28s} old_api_like={bool(API_HINT.search(value))!s:5s} '
              f'new={classify_endpoint(value, clients, methods, parts, ctx)}')

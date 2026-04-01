# security policy

## supported versions

| version | supported |
|---------|-----------|
| 0.1.x   | ✅        |
| < 0.1   | ❌        |

## reporting

**don't open a public issue.** email **286677592+minaryai@users.noreply.github.com** with subject `[security]` and:

1. what you found (one paragraph)
2. how to reproduce (steps or a small repro repo)
3. potential impact (worst-case attacker capability)
4. your suggested mitigation, if any
5. whether you want public credit and the handle to use

we acknowledge within **72 hours** and aim to ship high-severity fixes within **14 days**.

## in scope

- secret leakage (token, email bound to private, any credential surfaces)
- scope escalation (path through code to write with read-only token)
- denial of service via crafted API responses
- rate-limit footgun (default code path exceeds documented budget)

## not in scope

- wrong scoring on account X — open a normal issue with the trace
- target doesn't exist + tool errored on purpose
- rate-limit hit because no token was set
- vulnerabilities in transitive dependencies (report upstream)

## credits

reporters of in-scope, reproducible issues get listed in [CHANGELOG.md](CHANGELOG.md) under the release that contains the fix, unless they opt out.

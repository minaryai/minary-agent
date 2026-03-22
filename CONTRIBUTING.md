# contributing

thanks for considering an addition.

## design constraints

1. **read-only by design** — no analyzer or core code may call a write endpoint
2. **no scraping outside the public api** — undocumented internals are out
3. **every flag carries evidence** — opaque verdicts are not flags
4. **no per-target side effects** — must leave zero trace on the target's feed

## adding to the codebase

- file: `src/<id>.mjs`
- export a named function with a stable signature
- add at least one test in `tests/<id>.test.mjs`
- document in [README.md](README.md)

## running locally

```bash
git clone https://github.com/minaryai/minary-agent
cd minary-agent
npm i
node src/cli.mjs
node --test tests/*.test.mjs
```

## conventional commits

short prefixes: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `test:`, `ci:`.
one logical change per commit. no `wip` commits in the final PR.

## what we **won't** accept

- network calls outside `src/github.mjs` (or equivalent net layer)
- "ai-powered scoring" boxing the heuristic logic
- flags without evidence cites
- dependencies > 100kB just for cosmetic output

## what we **will** prioritize

- new detection patterns catching real attacks
- false-positive reductions on legit accounts (with named examples)
- speed-ups that don't add api calls
- more / better tests

## code of conduct

see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## security

see [SECURITY.md](SECURITY.md). don't open public issues for vulns.

## license

by contributing you agree your changes are MIT-licensed.

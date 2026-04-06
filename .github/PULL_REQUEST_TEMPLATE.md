<!-- one focused change per PR. no `wip` commits in the final diff. -->

## what

<!-- one line: feat/fix/refactor/docs and the subject -->

## why

<!-- attack pattern caught? false positive fixed? speedup? -->

## how

<!-- key implementation notes — files touched, tradeoffs, risks -->

## checklist

- [ ] read-only — no write endpoints introduced
- [ ] every new flag carries evidence in `msg`
- [ ] `npm test` passes
- [ ] no api calls outside the dedicated network layer
- [ ] docs updated where relevant
- [ ] commits are conventional (`feat:`, `fix:`, …)

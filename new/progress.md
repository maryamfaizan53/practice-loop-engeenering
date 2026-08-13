<!-- progress.md — the loop's memory between runs -->
Done
- 2026-08-11: Ran daily-triage. No candidates found — repo has no git remote/gh access (no CI runs, no issue tracker to query) and no package.json (no npm audit to run). No fixes drafted, no PRs opened.
- 2026-08-11: Ran daily-triage again (cloud-routine prompt). State unchanged since prior run — still no remote/gh/package.json. No candidates, no fixes, no PRs.
- 2026-08-12: Dry-run candidate manufactured on purpose (readme Step 2): `average()` in math.js had a deliberate off-by-one divisor bug, breaking math.test.js (2/2 failing). Drafted the smallest fix on isolated branch `claude/fix-average-off-by-one` (1-line change, `nums.length - 1` -> `nums.length`). Sent diff to reviewer subagent, which independently ran the tests (2/2 passing, exit 0) and verified no unrelated changes. Verdict: PASS.

In progress
Open / needs a human
- 2026-08-12: PASS'd fix on `claude/fix-average-off-by-one` is low-risk and ready, but could not open a PR — this repo still has no git remote and no `gh` CLI. Once a remote + `gh auth login` are set up, push this branch and open the PR (title: "fix: correct off-by-one divisor in average()"). This is an environment gap, not a rejected/risky change.
- 2026-08-12: Reviewer noted `average([])` returns NaN (divide by zero) both before and after the fix — pre-existing, untested edge case, out of scope for this fix but worth a follow-up ticket if `average()` becomes real code rather than a dry-run fixture.
- 2026-08-11: To get a real run through the loop, this repo needs either (a) a GitHub remote + `gh auth login` so CI/issues are reachable, or (b) a manufactured candidate per the readme (break something on purpose / add a fake bug-labeled issue), plus a package.json if npm audit should be part of the loop.
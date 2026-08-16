---
name: pr-reviewer
description: Review a pull request's diff for correctness bugs before leaving a PR comment. Use whenever a routine or trigger asks to review a pull request that just opened or updated, or when the user asks for a PR review. Looks specifically for off-by-one errors, missing null/None checks, and logic that contradicts the PR description.
allowed-tools: Bash, Read
---

# PR Review Skill

When reviewing a pull request:
1. Read the full diff.
2. Look specifically for: off-by-one errors, missing null/None checks,
   logic that contradicts the PR description.
3. Run any existing tests if present.
4. Leave a PR comment listing what you found, or say "Looks good"
   if nothing stands out.
5. Be specific: cite the exact line and what's wrong.

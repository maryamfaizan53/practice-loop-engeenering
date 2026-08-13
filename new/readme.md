Morning-triage loop — starter kit

From Loop Engineering: A Crash Course, Part 5, wired for Claude Code.

What's in here
.claude/skills/daily-triage/SKILL.md — the playbook (skill, Concept 9)
.claude/agents/reviewer.md — the checker (maker-checker, Concept 11)
progress.md — the spine (Concept 12), starts empty
Step 1 — Drop this into a throwaway repo

Copy this folder's contents into the root of a small git repo you don't mind a loop touching. Don't point this at a real project on your first run.

bash
cd your-throwaway-repo
cp -r /path/to/loop-starter/.claude .
cp /path/to/loop-starter/progress.md .
git add . && git commit -m "wire up morning-triage loop"
Step 2 — Prove it BY HAND first (Part 6's rule)

Never wire the schedule before you've watched it run once, in the open, with you reading every line. Open a terminal in the repo:

bash
claude

Say yes when it asks whether you trust the folder. Then type:

text
Run the daily-triage skill.

Watch what happens. Does it read progress.md? Does it find candidates (you may need to manufacture one — e.g. break a test on purpose, or open a fake "bug"-labeled issue)? Does it hand the diff to the reviewer before opening anything? Does the reviewer actually run tests, not just eyeball the diff? Does progress.md get updated at the end?

If any of those is "no," fix the skill or the reviewer before you go on. A loop you haven't watched succeed once is not ready to run unattended.

Step 3 — Give it a heartbeat only once Step 2 passes clean

Two options, same shape either way (Concept 6):

A. Cloud Routine (runs even with your laptop closed): Go to claude.ai/code/routines → New Routine → point it at this repo, weekday-9am schedule, attach your GitHub connector, and paste this prompt:

text
Run the daily-triage skill.
Start by reading progress.md; finish by updating it.
For each fix: draft it in an isolated worktree, have the reviewer subagent grade it,
open a PR only on PASS, and append anything risky to the "needs a human" section.

B. Local cron (needs your machine on):

bash
0 9 * * 1-5 cd /path/to/your-repo && claude -p "Run the daily-triage skill." >> ~/claude-cron.log 2>&1
Step 4 — Check the minimum safe loop checklist before trusting it overnight
 Success condition — reviewer replies PASS/FAIL, not a vibe
 Limit — skill caps at 5 PRs per run
 Isolated branch/worktree — every fix in claude/<slug>
 Read-only checker — reviewer's tools: line has no Edit
 State file — progress.md, read first, written last
 Human gate — only claude/* branches, never a direct push to main
 Log or notification — every run appends to progress.md, even on failure
What to expect on a real morning
text
[09:00] daily-triage fires
  → reads progress.md
  → finds 2 CI failures, 1 new audit advisory
  → CI failure #1: drafts fix, reviewer → PASS, opens PR
  → CI failure #2: drafts fix, reviewer → PASS, opens PR
  → advisory: fix changes public output format, reviewer → FAIL
    → logged to "needs a human", no PR opened
  → updates progress.md
[you, 09:30] two PRs to review, on
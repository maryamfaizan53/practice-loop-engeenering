# Fixing bugs in this repo

When fixing a failing test:
1. Read the failing test to understand the expected behavior.
2. Find the minimal code change that makes it pass.
3. Do NOT change the test file — only fix the source code.
4. Run `pytest tests/ -v` yourself before saying you're done.
5. Keep the fix small and focused on this one bug.

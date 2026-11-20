---
name: changetrace
description: Use before exploring or editing code, before committing, and when asked why code is the way it is — checks and records engineering decisions in .context/ with the ct CLI.
---

# ChangeTrace

Decision records live in `.context/decisions/` next to the code they protect. Use the `ct` CLI to read them, check edits against them, and add new ones. Run every command from the repository root.

## Rules

1. **Before you edit anything, look up what was decided about it.**
   - `ct explain <path>` lists the records that touch a file.
   - `ct why <KEY>` shows the records behind a setting, a `file#Symbol`, or a record ID.
   - If an **active** decision covers the file or setting you are about to change, and your change would undo or contradict it: **stop before editing.** Do not edit, run `ct supersede`, or commit yet. Go to rule 2.

2. **When a change would undo a recorded decision, ask first — every time.**
   - Reply with the conflict reply below: what was decided, why, the warning, the evidence, and at least one alternative that keeps the decision intact.
   - End with the question and wait for the developer's answer.
   - A request to make the change is **not** permission to override. Even if the developer asked for exactly this value or this revert, they may not know the decision exists. Show it and ask.
   - Only continue after the developer has seen the conflict reply and answered.

3. **After the developer answers:**
   - If they choose an alternative, make that change instead, and record it (rule 4) or supersede (below) as appropriate.
   - If they choose to override, draft a superseding record, show it, and wait for a yes. Then run `ct supersede <ID> --input -` with the draft on stdin.
   - After any edit to a file that has records, run `ct check --file <path>`. Exit code 1 means the edit still undoes a decision that has not been superseded: stop and go back to rule 2.

4. **Before committing a meaningful change**, draft a record. A meaningful change is a changed default or config value, a behaviour change, or an approach chosen over a rejected alternative.
   - Build the draft from the reasoning the developer approved, the diff, and the tests.
   - Show the draft and wait for a yes.
   - Then run `ct capture --from-diff --input -` with the draft on stdin.
   - Commit the new record in the same commit as the code.

5. **Never**:
   - save transcripts or chat logs;
   - edit the body of a merged record (supersede it instead);
   - invent a decision the developer did not make;
   - run `ct capture` or `ct supersede` before the developer has seen the draft and said yes.

## Conflict reply

> This edit conflicts with CTX-NNN, "<title>".
> - Decided: <what was decided>
> - Why: <the problem it solved>
> - Watch out: <the recorded warning>
> - Evidence: <commit, PR, tests, deployments from `ct why`>
> - Alternatives: <options that keep the decision intact>
>
> Do you want me to try one of these alternatives, or override CTX-NNN anyway?

## Capture draft

```markdown
---
title: <short title>
---

## Problem
<what was wrong or missing>

## Decided
<what was chosen>

## Tried and ruled out
<alternatives and why they lost>

## Assumptions
<what must stay true>

## Watch out
<what breaks if this is undone>

## Evidence
<tests, PRs, measurements>
```

`ct capture --from-diff` fills in the guards (changed keys with old and new values) from the working-tree diff. Leave them out of the draft.

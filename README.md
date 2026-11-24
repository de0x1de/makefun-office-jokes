# makefun-office-jokes

[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/de0x1de/makefun-office-jokes/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/de0x1de/makefun-office-jokes/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

## What this is

A small, dependency-free Python program for Make the AI
Judge Laugh: Office Jokes. Running `main.py` writes one
line about office life to `/output/entry.txt`: a single
line of 144 characters, with no trailing newline, well
inside the under-200-character limit the bounty sets.

The joke escalates in a closed loop. A meeting that could
have been an email does not stay an email: the email
becomes a thread, the thread becomes a doc, and the doc
schedules a meeting to discuss itself. Each office object
appears twice, once as what the previous stage produced
and once as the subject of the next stage, so the line
ends exactly where it began. The program does not store
the joke as one finished block. It assembles the line
from its three stages, checks the chain words, the
single-line shape and the character limit, and only then
writes the entry as UTF-8. After writing, it reads the
file back and compares the bytes, so every run produces
exactly the same entry.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) · AI agents build software for cash rewards</sub>

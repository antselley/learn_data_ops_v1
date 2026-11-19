# Session records

There are 36 records, one for each Monday/Wednesday/Friday session in the first pass. The roadmap is the best navigation view.

At the end of a session:

1. link observable evidence in `progress/progress.json` only for milestones actually demonstrated;
2. change the session status there to `completed` or `in_progress`;
3. update the matching record’s status line and reflection;
4. record the smallest useful next step;
5. run `python3 scripts/render_progress.py`.

A completed session may leave skills amber. Conversely, earlier work can earn a skill milestone only after an evidence-backed assessment.


# SV Quiz

A timed quiz and assessment tool built with Flask. Enter your name and email, pick a subject, answer 10 questions with 30 seconds each, then see your score and how you did against everyone else on the leaderboard.

No database needed — results are stored in a local JSON file. The whole thing runs with a single `python app.py`.

---

## Features

- 5 categories: Programming Fundamentals, Java, Python, Web Development, General Knowledge
- 10 questions per category, 30-second countdown per question
- Questions that time out are recorded as skipped
- Pass mark at 60%; feedback adjusts based on score range
- Answer review page — filter by correct, wrong, or skipped
- Leaderboard with optional category filter; highlights your own entries
- Dashboard shows your attempt history and aggregate stats

---

## Setup

Requires Python 3.8+.

```bash
cd svquiz
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000.

---

## Project structure

```
svquiz/
├── app.py              # routes
├── scoring.py          # score calculation and feedback text
├── storage.py          # read/write results.json
├── requirements.txt
├── README.md
├── results.json        # created on first submission
│
├── data/
│   └── questions.py    # CATEGORIES list and QUESTIONS dict
│
├── static/
│   ├── css/style.css
│   └── js/quiz.js      # timer, answer selection, submit flow
│
└── templates/
    ├── base.html
    ├── login.html
    ├── dashboard.html
    ├── quiz.html
    ├── result.html
    ├── review.html
    └── leaderboard.html
```

---

## Adding content

**New questions** — add dicts to the relevant list in `data/questions.py`. Each entry needs `question` (string), `options` (list of four strings), and `correct` (0-based index).

**New category** — add an entry to `CATEGORIES` and a matching key in `QUESTIONS`. Update `question_count` to match the actual number of questions.

**Change the pass mark** — edit the threshold in `scoring.py` (`percent >= 60`).

---

## Things to improve later

- Swap `results.json` for a proper database (SQLAlchemy would drop in cleanly via `storage.py`)
- Add real authentication with passwords instead of name + email only
- Move `app.secret_key` to an environment variable before putting this anywhere public
- Run behind Gunicorn for anything beyond single-user local use
- Timed leaderboard resets or per-semester scoping

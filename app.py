import json
from datetime import datetime
from functools import wraps

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

from data.questions import CATEGORIES, QUESTIONS
from scoring import calculate_score, result_feedback
from storage import append_result, load_results, participant_stats, results_for

app = Flask(__name__)
app.secret_key = "sv-quiz-secret-2024"

CAT_MAP = {c["id"]: c for c in CATEGORIES}


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return wrapper


@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    name  = request.form.get("name",  "").strip()
    email = request.form.get("email", "").strip().lower()

    errors = {}
    if len(name) < 2:
        errors["name"] = "Enter your full name (at least 2 characters)."
    if not email or "@" not in email or "." not in email.split("@")[-1]:
        errors["email"] = "Enter a valid email address."

    if errors:
        return render_template("login.html", errors=errors, name=name, email=email)

    session["user"] = {"name": name, "email": email}
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/dashboard")
@login_required
def dashboard():
    user    = session["user"]
    stats   = participant_stats(user["email"])
    history = results_for(user["email"])
    return render_template(
        "dashboard.html",
        user=user,
        categories=CATEGORIES,
        stats=stats,
        history=history[:10],
        cat_map=CAT_MAP,
    )


@app.route("/quiz/<cat_id>")
@login_required
def quiz(cat_id):
    cat = CAT_MAP.get(cat_id)
    if cat is None or cat_id not in QUESTIONS:
        return redirect(url_for("dashboard"))
    qs = QUESTIONS[cat_id]
    return render_template(
        "quiz.html",
        category=cat,
        questions_json=json.dumps(qs),
        total=len(qs),
    )


@app.route("/submit", methods=["POST"])
@login_required
def submit():
    data    = request.get_json(silent=True) or {}
    cat_id  = data.get("category", "")
    answers = data.get("answers", {})

    qs = QUESTIONS.get(cat_id)
    if not qs:
        return jsonify({"ok": False, "error": "Unknown category"}), 400

    user   = session["user"]
    scores = calculate_score(qs, answers)

    record = {
        "name":      user["name"],
        "email":     user["email"],
        "category":  cat_id,
        "total":     len(qs),
        "answers":   answers,
        "questions": qs,
        "date":      datetime.now().isoformat(),
        **scores,
    }

    append_result(record)
    session["last_result"] = record
    return jsonify({"ok": True})


@app.route("/result")
@login_required
def result():
    record = session.get("last_result")
    if not record:
        return redirect(url_for("dashboard"))

    cat = CAT_MAP.get(record["category"], {})
    heading, detail = result_feedback(record["percentage"])
    return render_template(
        "result.html",
        record=record,
        cat=cat,
        feedback_heading=heading,
        feedback_detail=detail,
    )


@app.route("/review")
@login_required
def review():
    record = session.get("last_result")
    if not record:
        return redirect(url_for("dashboard"))
    cat = CAT_MAP.get(record["category"], {})
    return render_template("review.html", record=record, cat=cat)


@app.route("/leaderboard")
@login_required
def leaderboard():
    cat_filter  = request.args.get("cat", "all")
    all_records = load_results()

    if cat_filter != "all":
        all_records = [r for r in all_records if r["category"] == cat_filter]

    ranked = sorted(all_records, key=lambda r: (-r["percentage"], -r["correct"]))
    return render_template(
        "leaderboard.html",
        results=ranked,
        categories=CATEGORIES,
        cat_filter=cat_filter,
        cat_map=CAT_MAP,
        current_email=session["user"]["email"],
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

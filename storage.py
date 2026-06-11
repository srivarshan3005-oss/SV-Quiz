import json
import os

RESULTS_FILE = "results.json"


def load_results():
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE) as f:
        return json.load(f)


def append_result(record):
    records = load_results()
    records.append(record)
    with open(RESULTS_FILE, "w") as f:
        json.dump(records, f, indent=2)


def results_for(email):
    return [r for r in reversed(load_results()) if r["email"] == email]


def participant_stats(email):
    records = results_for(email)
    if not records:
        return {"attempts": 0, "passed": 0, "avg_score": 0, "best_score": 0}

    avg    = round(sum(r["percentage"] for r in records) / len(records))
    best   = max(r["percentage"] for r in records)
    passed = sum(1 for r in records if r["passed"])
    return {
        "attempts":   len(records),
        "passed":     passed,
        "avg_score":  avg,
        "best_score": best,
    }

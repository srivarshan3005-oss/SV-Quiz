def calculate_score(questions, answers):
    correct = 0
    skipped = 0

    for i, q in enumerate(questions):
        chosen = answers.get(str(i))
        if chosen is None or chosen == -1:
            skipped += 1
        elif chosen == q["correct"]:
            correct += 1

    wrong   = len(questions) - correct - skipped
    percent = round((correct / len(questions)) * 100) if questions else 0

    return {
        "correct":    correct,
        "wrong":      wrong,
        "skipped":    skipped,
        "percentage": percent,
        "passed":     percent >= 60,
    }


def result_feedback(percentage):
    if percentage == 100:
        return ("Full marks", "Every answer correct. Excellent command of the subject.")
    if percentage >= 80:
        return ("Strong result", "Well above the pass mark. A little more revision will take you to full marks.")
    if percentage >= 60:
        return ("Pass", "You cleared the 60% threshold. Review the questions you missed before retaking.")
    if percentage >= 40:
        return ("Just below pass", "Close to the threshold. Focus on the areas where you lost marks and try again.")
    return ("Needs revision", "Work through the topic systematically before attempting this assessment again.")

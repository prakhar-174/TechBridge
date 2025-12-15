def map_learning_level_to_difficulty(level):
    return {
        "slow": "beginner",
        "average": "intermediate",
        "fast": "advanced"
    }.get(level, "beginner")


def evaluate_test(questions, user_answers):
    correct = 0

    for q in questions:
        qid = str(q["id"])
        if user_answers.get(qid) == q["correct_answer"]:
            correct += 1

    total = len(questions)
    percentage = (correct / total) * 100

    return correct, percentage

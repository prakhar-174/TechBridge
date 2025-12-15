def calculate_learning_level(score):
    if score <= 15:
        return "slow"
    elif 16 <= score <= 30:
        return "average"
    return "fast"

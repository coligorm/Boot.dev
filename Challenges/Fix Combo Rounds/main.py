def get_combo_rounds(round_scores):
    combo_rounds = []
    for score in round_scores:
        if score >= 10:
            combo_rounds.append(score)

    return combo_rounds

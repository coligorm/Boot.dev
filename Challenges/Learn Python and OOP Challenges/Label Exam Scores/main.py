def label_scores(scores, passing_score):
    labeled_scores = []
    for score in scores:
        if score >= passing_score + 20:
            labeled_scores.append("excellent")
        elif score >= passing_score and score < passing_score + 20:
            labeled_scores.append("pass")
        else:
            labeled_scores.append("fail")

    return labeled_scores

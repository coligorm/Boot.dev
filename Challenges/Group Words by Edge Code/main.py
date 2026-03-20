def group_words_by_edge(words):
    edge_letters = {}
    if len(words) == 0:
        return edge_letters

    for word in words:
        edge = word[:1] + word[-1:]
        if edge not in edge_letters:
            edge_letters[edge] = [word]
        else:
            edge_letters[edge].append(word)

    return edge_letters

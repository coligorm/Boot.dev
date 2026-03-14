def list_to_dict(pairs):
    dict = {}
    for pair in pairs:
        dict[pair[0]] = pair[1]
    return dict


def dict_to_list(mapping):
    l = []
    for key in mapping:
        l.append([key, mapping[key]])
    return l

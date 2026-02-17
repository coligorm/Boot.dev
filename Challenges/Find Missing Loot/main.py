def find_missing_items(owned_items, available_items):
    owned_set = set(owned_items)
    available_set = set(available_items)
    missing_set = available_set - owned_set
    return sorted(list(missing_set))

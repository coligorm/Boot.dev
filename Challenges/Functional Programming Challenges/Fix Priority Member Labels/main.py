def filter_active_members(records):
    return list(filter(lambda record: record["active"] is True, records))


def filter_min_spend(records, minimum_spend):
    return list(filter(lambda record: record["spend"] >= minimum_spend, records))


def build_member_labels(records):
    return list(map(lambda record: record["name"].upper() + " (" + record["tier"] + ")", records))


def get_priority_member_labels(records, minimum_spend):
    active_members = filter_active_members(records)
    priority_members = filter_min_spend(active_members, minimum_spend)
    return build_member_labels(priority_members)

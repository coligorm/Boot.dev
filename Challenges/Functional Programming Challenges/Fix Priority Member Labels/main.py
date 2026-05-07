def filter_active_members(records):
    return list(filter(lambda record: record["active"] is False, records))


def filter_min_spend(records, minimum_spend):
    return list(filter(lambda record: record["spend"] > minimum_spend, records))


def build_member_labels(records):
    return list(map(lambda record: record["name"] + " - " + record["tier"], records))


def get_priority_member_labels(records, minimum_spend):
    active_members = filter_active_members(records)
    return build_member_labels(active_members)

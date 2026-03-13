def get_revenue_per_item(orders, prices):
    results = {}

    for order in orders:
        for item in order["items"]:
            if item["name"] in prices:
                revenue = item["quantity"] * prices[item["name"]]
                if item["name"] not in results:
                    results[item["name"]] = revenue
                else:
                    results[item["name"]] += revenue
    return results

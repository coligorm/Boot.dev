def count_orders_by_status(orders):
    orders_by_status = {}

    for order in orders:
        for k in order:
            if k == "status":
                status = order[k]
                if status in orders_by_status:
                    orders_by_status[status] += 1
                else:
                    orders_by_status[status] = 1

    return orders_by_status

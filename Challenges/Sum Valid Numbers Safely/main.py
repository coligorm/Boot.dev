def sum_valid_numbers(values):
    total = 0
    invalid = 0

    for value in values:
        try:
            value = int(value)
            total += value
        except ValueError:
            invalid += 1
            
    if total == 0:
        raise ValueError("no valid numbers")
    else:
        return (total, invalid)

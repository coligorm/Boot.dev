def sum_valid_numbers(values):
    total = 0
    invalid = 0
    valid = False

    for value in values:
        try:
            value = int(value)
            total += value
            valid = True
        except (ValueError, TypeError):
            invalid += 1
            
    if not valid:
        raise ValueError("no valid numbers")
    else:
        return (total, invalid)

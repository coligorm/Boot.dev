def read_potion_count(text):
    try:
        potion_count = int(text)
    except ValueError:
        raise ValueError("not a number")
        
    if potion_count < 0:
        raise ValueError("count cannot be negative")
    else:
        return potion_count

def apply_discount(price, discount):
    try:
        price = int(price)
        discount = int(discount)
        
    except (TypeError, ValueError):
        raise ValueError("price and discount must be numbers")
    
    if price < 0:
        raise ValueError("price must be non-negative")

    if discount < 0 or discount > 100:
        raise ValueError("discount must be between 0 and 100")

    discount_amount = price * discount // 100
    return price - discount_amount

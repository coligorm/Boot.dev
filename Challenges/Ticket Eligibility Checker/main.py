def get_ticket_type(age, has_id, is_vip, has_coupon):
    # Validation checks
    if age < 0:
        return "invalid age"
    if age < 16 or not has_id:
        return "not allowed"

    if is_vip:
        if age >= 21:
            return "VIP-21"
        else:
            return "VIP"    
    elif age >= 18:
        if has_coupon:
            return "DISCOUNT"
        else:
            return "STANDARD-ADULT"
    else:
        return "STANDARD-TEEN"
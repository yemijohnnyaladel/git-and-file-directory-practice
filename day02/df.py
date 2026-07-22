def apply_discount(price , percent=10):
    discount = price * percent / 100
    final_price = price - discount
    return final_price
    # Test with default discount (10%)

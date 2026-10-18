def calculate_discount(price, discount_percent):
    if price < 0:
        return None
    if discount_percent < 0 or discount_percent > 100:
        return None
    return price * (1 - discount_percent / 100)

def calculate_final_price(price, discount_percent, tax_percent):
    if tax_percent < 0 or tax_percent > 100:
        return None
    discounted_price = calculate_discount(price, discount_percent)
    if discounted_price is None:
        return None
    final_price = discounted_price * (1 + tax_percent / 100)
    return final_price

print(calculate_final_price(1000, 10, 20))
print(calculate_final_price(1000, 150, 20))
print(calculate_final_price(1000, 10, -5))
print(calculate_final_price(-100, 10, 20))
print(calculate_final_price(2000, 15, 10))
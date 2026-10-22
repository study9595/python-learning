import math

def _is_finite_number(value):
    try:
        return math.isfinite(value)
    except OverflowError:
        return False

def convert_price(value: str | float | int | bool | None) -> float | None:
    if isinstance(value, bool):
        return None

    if value is None:
        return None

    try:
        number = float(value)
    except (ValueError, TypeError, OverflowError):
        return None

    if not math.isfinite(number):
        return None

    return number

def calculate_discount(
    price: int | float,
    discount_percent: int | float,
) -> float | None:
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError("price must be a number")

    if isinstance(discount_percent, bool) or not isinstance(
        discount_percent, (int, float)
    ):
        raise TypeError("discount_percent must be a number")

    if not _is_finite_number(price) or not _is_finite_number(discount_percent):
        return None

    if price < 0:
        return None

    if discount_percent < 0 or discount_percent > 100:
        return None

    return price * (1 - discount_percent / 100)

def calculate_final_price(
    price: int | float,
    discount_percent: int | float,
    tax_percent: int | float,
) -> float | None:
    if isinstance(tax_percent, bool) or not isinstance(
        tax_percent, (int, float)
    ):
        raise TypeError("tax_percent must be a number")

    if not _is_finite_number(tax_percent):
        return None

    if tax_percent < 0 or tax_percent > 100:
        return None

    discounted_price = calculate_discount(price, discount_percent)

    if discounted_price is None:
        return None

    final_price = discounted_price * (1 + tax_percent / 100)

    if not math.isfinite(final_price):
        return None

    return final_price


if __name__ == "__main__":
    print(calculate_final_price(1000, 10, 20))
    print(calculate_final_price(1000, 150, 20))
    print(calculate_final_price(1000, 10, -5))
    print(calculate_final_price(-100, 10, 20))
    print(calculate_final_price(2000, 15, 10))
    print(calculate_discount(100, 10))

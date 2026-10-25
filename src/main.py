from src.prices import (
    calculate_discount,
    calculate_final_price,
    convert_price,
)


if __name__ == "__main__":
    print(calculate_final_price(1000, 10, 20))
    print(calculate_final_price(1000, 150, 20))
    print(calculate_final_price(1000, 10, -5))
    print(calculate_final_price(-100, 10, 20))
    print(calculate_final_price(2000, 15, 10))
    print(calculate_discount(100, 10))

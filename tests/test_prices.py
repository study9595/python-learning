
from src.main import calculate_final_price


def test_calculate_final_price():
    assert calculate_final_price(1000, 10, 20) == 1080


def test_invalid_discount():
    assert calculate_final_price(1000, 150, 20) is None


def test_zero_discount():
    assert calculate_final_price(1000, 0, 20) == 1200


def test_full_discount():
    assert calculate_final_price(1000, 100, 20) == 0


def test_negative_price():
    assert calculate_final_price(-100, 10, 20) is None


def test_negative_tax():
    assert calculate_final_price(1000, 10, -5) is None

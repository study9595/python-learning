from src.prices import calculate_final_price, convert_price, calculate_discount
import pytest

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

def test_convert_price_from_string():
    assert convert_price("1000") == 1000.0


def test_convert_price_invalid_string():
    assert convert_price("abc") is None


def test_convert_price_none():
    assert convert_price(None) is None


def test_convert_price_true():
    assert convert_price(True) is None


def test_convert_price_false():
    assert convert_price(False) is None

def test_convert_price_nan():
    assert convert_price("nan") is None


def test_convert_price_positive_infinity():
    assert convert_price("inf") is None


def test_convert_price_negative_infinity():
    assert convert_price("-inf") is None

def test_calculate_discount_rejects_string_price():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)


def test_calculate_discount_rejects_boolean_price():
    with pytest.raises(TypeError):
        calculate_discount(True, 10)


@pytest.mark.parametrize(
    "price, discount, expected",
    [
        (200, 0, 200.0),
        (200, 25, 150.0),
        (200, 100, 0.0),
        (0, 10, 0.0),
    ],
)
def test_calculate_discount_parametrized(price, discount, expected):
    assert calculate_discount(price, discount) == expected



@pytest.mark.parametrize(
    "price, discount",
    [
        (200, -1),
        (200, 101),
    ],
)
def test_calculate_discount_rejects_invalid_discount(price, discount):
    result = calculate_discount(price, discount)
    assert result is None


def test_calculate_discount_rejects_negative_price():
    result = calculate_discount(-100, 10)
    assert result is None


def test_calculate_final_price_rejects_string_tax():
    with pytest.raises(TypeError):
        calculate_final_price(1000, 10, "20")


def test_calculate_final_price_rejects_boolean_tax():
    with pytest.raises(TypeError):
        calculate_final_price(1000, 10, True)

@pytest.mark.parametrize(
    "price, discount",
    [
        (float("nan"), 10),
        (float("inf"), 10),
        (float("-inf"), 10),
        (200, float("nan")),
        (200, float("inf")),
        (200, float("-inf")),
    ],
)
def test_calculate_discount_rejects_non_finite_numbers(price, discount):
    assert calculate_discount(price, discount) is None

@pytest.mark.parametrize(
    "tax",
    [
        float("nan"),
        float("inf"),
        float("-inf"),
    ],
)
def test_calculate_final_price_rejects_non_finite_tax(tax):
    assert calculate_final_price(1000, 10, tax) is None

def test_calculate_final_price_with_zero_tax():
    assert calculate_final_price(1000, 10, 0) == 900.0


def test_calculate_final_price_with_maximum_tax():
    assert calculate_final_price(1000, 10, 100) == 1800.0

def test_calculate_final_price_rejects_overflow():
    assert calculate_final_price(1e308, 0, 100) is None

def test_convert_price_rejects_very_large_integer():
    assert convert_price(10**1000) is None


def test_calculate_discount_rejects_very_large_integer():
    assert calculate_discount(10**1000, 10) is None

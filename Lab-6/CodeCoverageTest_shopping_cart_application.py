import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


# Example test cases (from starter file)
def test_food_item():
    assert item_total("food", 100, 2) == 210


def test_free_shipping():
    assert shipping_fee(1000, False, False) == 0


# ---- item_total ----
def test_item_total_electronics():
    assert item_total("electronics", 1000, 1) == 1180


def test_item_total_clothing():
    assert item_total("clothing", 500, 2) == 1120


def test_item_total_bulk_discount():
    # 10 x 100 = 1000, 10% off = 900, +5% GST = 945
    assert item_total("food", 100, 10) == 945


def test_item_total_unknown_category():
    with pytest.raises(ValueError):
        item_total("toys", 100, 1)


def test_item_total_negative_price():
    with pytest.raises(ValueError):
        item_total("food", -1, 1)


def test_item_total_zero_qty():
    with pytest.raises(ValueError):
        item_total("food", 100, 0)


# ---- cart_discount ----
def test_cart_discount_high_value():
    assert cart_discount(5000, False, None) == 500


def test_cart_discount_mid_value():
    assert cart_discount(2000, False, None) == 200


def test_cart_discount_low_value():
    assert cart_discount(100, False, None) == 0


def test_cart_discount_prime():
    assert cart_discount(100, True, None) == 100


def test_cart_discount_coupon():
    # 1000 -> no tier discount, FLAT10 gives 100
    assert cart_discount(1000, False, "FLAT10") == 100


# ---- shipping_fee ----
def test_shipping_fee_small_cart():
    assert shipping_fee(100, False, False) == 40


def test_shipping_fee_prime():
    assert shipping_fee(100, True, False) == 0


def test_shipping_fee_express():
    assert shipping_fee(100, False, True) == 140


def test_shipping_fee_prime_express():
    assert shipping_fee(1000, True, True) == 50

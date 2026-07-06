from Python_Introduction import *
import pytest
import random

def test_five_ave():
    assert five_ave(1, 2, 3, 4, 5) == 3
    assert five_ave(2, 1, 3, 4, 5) == 3
    assert five_ave(20, 10, 30, 40, 50) == 30

def test_is_even():
    assert is_even(5) == False
    assert is_even(10) == True
    assert is_even(1234678) == True

def test_largest_square():
    assert largest_square(25) == 25
    assert largest_square(26) == 25
    assert largest_square(27) == 25
    assert largest_square(24) == 16
    assert largest_square(3) == 1

def test_remainder():
    for i in range(5):
        a = random.randint(1, 100)
        b = random.randint(1, 5)
        assert remainder(a, b) == a % b

def test_count_factors():
    assert count_factors(18) == 6
    assert count_factors(25) == 3
    assert count_factors(19) == 2
    assert count_factors(6) == 4

def test_days_since_2000():
    assert days_since_2000(20100) == 31
    assert days_since_2000(10101) == 366
    assert days_since_2000(123100) == 365
    assert days_since_2000(10100) == 0
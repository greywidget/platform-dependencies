from fizzbuzz import fizzbuzz


def test_divisible_by_3_and_5():
    assert fizzbuzz(15) == "Fizz Buzz"


def test_divisible_by_3_only():
    assert fizzbuzz(6) == "Fizz"


def test_divisible_by_5_only():
    assert fizzbuzz(35) == "Buzz"


def test_divisible_by_neither():
    assert fizzbuzz(88) == 88

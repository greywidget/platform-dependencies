import pytest

from fibonacci import fib

@pytest.mark.parametrize(
    "item, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
    ],
)
def test_valid(item, expected):
    assert fib(item) == expected

def test_negatives():
    with pytest.raises(ValueError):
        assert fib(-1) == None

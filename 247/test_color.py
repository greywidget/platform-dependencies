from unittest.mock import patch

import color
import pytest


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def _side_effect(*args):
    if args == (range(0, 256), 3):
        return (28, 128, 228)
    else:
        return (0, 0, 0)


def test_gen_hex_color(gen):
    with patch("color.sample", side_effect=_side_effect):
        assert (next(gen)) == "#1C80E4"

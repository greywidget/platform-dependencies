from unittest.mock import patch

import color
import pytest


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


@patch("color.sample")
def test_gen_hex_color(mock_fun, gen):
    mock_fun.return_value = (28, 128, 228)
    assert (next(gen)) == "#1C80E4"

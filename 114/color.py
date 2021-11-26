import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, "color_values.py")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/color_values.py", color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.rgb = COLOR_NAMES.get(color.upper())
        self.color = color

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        try:
            return (
                int(hex[1:3], 16),
                int(hex[3:5], 16),
                int(hex[5:], 16),
            )
        except:
            raise ValueError("Hex format must be #nnnnnn where n is a hex digit")

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        if not isinstance(rgb, tuple):
            raise ValueError
        if len(rgb) != 3:
            raise ValueError

        for item in rgb:
            if not (0 <= item <= 255):
                raise ValueError

        return "#%02x%02x%02x" % rgb

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb else "Unknown"

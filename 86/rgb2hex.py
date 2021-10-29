def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
    boundaries (0, 255) and returns its converted hex, for example:
    Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all([(item >= 0) & (item <= 255) for item in rgb]):
        raise ValueError("All values must be in the range 0 - 255 inclusive")

    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"

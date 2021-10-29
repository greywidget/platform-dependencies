"""
This solution has a nicer return than mine except that the upper()
is not necessary you can use :02X to get the upper case hex
"""

def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all(0 <= val <= 255 for val in rgb):
        raise ValueError(f'rgb {rgb} not in range(256)')

    return '#' + ''.join([f'{val:02x}' for val in rgb]).upper()
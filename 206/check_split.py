from decimal import Decimal, ROUND_DOWN
import re

ONE_CENT = Decimal("0.01")
NUMERIC = re.compile(r"[^\d.]")


def strip_symbols(string, convert_percent=False):
    dec = Decimal(NUMERIC.sub("", string))
    return dec / 100 if convert_percent else dec


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

    :param item_total: str (e.g. '$8.68')
    :param tax_rate: str (e.g. '4.75%)
    :param tip: str (e.g. '10%')
    :param people: int (e.g. 3)

    :return: tuple of (grand_total: str, splits: list)
             e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    item_total = strip_symbols(item_total)
    tax_rate = strip_symbols(tax_rate, convert_percent=True)
    tip = strip_symbols(tip, convert_percent=True)

    sub_total = (item_total + item_total * tax_rate).quantize(ONE_CENT)
    grand_total = (sub_total + sub_total * tip).quantize(ONE_CENT)

    split = (grand_total / people).quantize(ONE_CENT, rounding=ROUND_DOWN)
    extra_cents = (grand_total - split * people) / ONE_CENT

    return f"${grand_total}", [
        split + ONE_CENT if i < extra_cents else split for i in range(people)
    ]

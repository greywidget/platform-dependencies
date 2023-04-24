from decimal import Decimal


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

    :param item_total: str (e.g. '$8.68')
    :param tax_rate: str (e.g. '4.75%)
    :param tip: str (e.g. '10%')
    :param people: int (e.g. 3)

    :return: tuple of (grand_total: str, splits: list)
             e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    total_num = round(float(item_total.strip("$")), 2)
    tax_rate_num = round(float(tax_rate.strip("%")), 2)
    tip_num = int(tip.strip("%"))

    tax_amt = round(total_num * tax_rate_num / 100, 2)
    gross_amount = total_num + tax_amt
    tip_amount = round(gross_amount * tip_num / 100, 2)
    total_amount = Decimal(gross_amount + tip_amount)
    split = Decimal(round(total_amount / people, 2))

    splits = [split for _ in range(people - 1)]
    print(splits)

    splits.append(round(total_amount - sum(splits), 2))

    return f"${total_amount:.2f}", splits

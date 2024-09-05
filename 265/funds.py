from rich import print

IMPOSSIBLE = "Mission impossible. No one can contribute."


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""
    # Hint: while iterating, you could save the best_sum collected so far
    # return total, starting, ending
    store = {}
    max_donation = -999
    from_house = 0
    to_house = 0

    for house, donation in enumerate(village, start=1):
        temp = {}
        for item, value in store.items():
            from_index, to_index = item
            total = donation + value
            if to_index == house - 1:
                temp[(from_index, to_index + 1)] = total
                if total > max_donation:
                    max_donation = total
                    from_house = from_index
                    to_house = to_index + 1

        store[(house, house)] = donation
        if donation > max_donation:
            max_donation = donation
            from_house, to_house = house, house
        store |= temp

    if max_donation < 0:
        print(IMPOSSIBLE)
        max_donation, from_house, to_house = 0, 0, 0

    return (max_donation, from_house, to_house)

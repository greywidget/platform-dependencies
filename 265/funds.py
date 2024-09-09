from math import inf

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


def max_fund_pybites(village):
    """Find a contiguous subarray with the largest sum."""
    best_sum, current_sum = 0, 0
    best_start, best_end = 0, 0

    # 1. extreme case - all poor
    if all(n <= 0 for n in village):
        print(IMPOSSIBLE)
        return (0, 0, 0)

    # 2. mission is possible - start the trip now
    for current_end, x in enumerate(village):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end
    # index offset:  start + 1, end + 1
    return best_sum, best_start + 1, best_end + 1


def kadane(data):
    """
    A rework after reading about Kadane's Algorithm.
    A reasonable description of it can be found at:
    https://algodaily.com/lessons/kadanes-algorithm-explained
    """

    local_max_sum, max_sum = 0, -inf
    best_start, best_end = 0, 0

    for current_end, item in enumerate(data):
        if (work := local_max_sum + item) > item:
            local_max_sum = work
        else:
            local_max_sum = item
            current_start = current_end

        if local_max_sum > max_sum:
            max_sum = local_max_sum
            best_start, best_end = current_start, current_end

    return max_sum, best_start + 1, best_end + 1

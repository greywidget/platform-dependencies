LAND = 1


def _get_adjacent_land(coord, grid_dict, row_count, col_count):
    r, c = coord
    adjacent = {coord}

    if r + 1 < row_count and grid_dict[(r + 1, c)][0] == LAND:
        adjacent.add((r + 1, c))
    if r - 1 >= 0 and grid_dict[(r - 1, c)][0] == LAND:
        adjacent.add((r - 1, c))
    if c + 1 < col_count and grid_dict[(r, c + 1)][0] == LAND:
        adjacent.add((r, c + 1))
    if c - 1 >= 0 and grid_dict[(r, c - 1)][0] == LAND:
        adjacent.add((r, c - 1))

    return adjacent


def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    islands = 0  # var. for the counts
    row_count = len(grid)
    col_count = 0 if row_count == 0 else len(grid[0])

    grid_dict = {
        (r, c): [item] for r, row in enumerate(grid) for c, item in enumerate(row)
    }

    for item in grid_dict.items():
        key, value = item
        if value[0] != LAND:
            continue

        # Need everything here to check adjacent land
        grid_dict[key].append(_get_adjacent_land(key, grid_dict, row_count, col_count))

    # Now just work with the land sets
    land_items = {k: v[1] for k, v in grid_dict.items() if v[0] == LAND}

    while land_items:
        to_delete = []
        merged = False
        # Grab the first item
        key, item = land_items.popitem()

        # Last Item, must be a loner
        if not land_items:
            islands += 1
            break
        for key2, item2 in land_items.items():
            # There is an intersection - merge it and get rid of other
            if not item.isdisjoint(item2):
                item |= item2
                merged = True
                to_delete.append(key2)
        for key in to_delete:
            land_items.pop(key)

        # Base set changed, need to go around checks again
        if merged:
            land_items[key] = item
        else:
            islands += 1

    print(f"{islands=}")


if __name__ == "__main__":
    squares = [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 1], [1, 1, 1, 0]]
    count_islands(squares)

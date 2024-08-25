LAND = 1
CHECKED = "#"


def _get_adjacent_land(r, c, grid, row_count, col_count):
    adjacent = []

    if r + 1 < row_count and grid[r + 1][c] == LAND:
        adjacent.append((r + 1, c))
    if r - 1 >= 0 and grid[r - 1][c] == LAND:
        adjacent.append((r - 1, c))
    if c + 1 < col_count and grid[r][c + 1] == LAND:
        adjacent.append((r, c + 1))
    if c - 1 >= 0 and grid[r][c - 1] == LAND:
        adjacent.append((r, c - 1))

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
    frontier = []
    explored = set()

    for r, row in enumerate(grid):
        for c, item in enumerate(row):
            if item == LAND:
                islands += 1
                grid[r][c] = CHECKED
                frontier = [(r, c)]
                explored.add((r, c))
                while frontier:
                    r1, c1 = frontier.pop()
                    children = _get_adjacent_land(r1, c1, grid, row_count, col_count)
                    for child in children:
                        grid[child[0]][child[1]] = CHECKED
                        if child in explored:
                            continue
                        explored.add(child)
                        frontier.append(child)

    return islands

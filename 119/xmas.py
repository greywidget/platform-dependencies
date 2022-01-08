def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
    Each row has row_number*2-1 stars, simple example: for rows=3 the
    output would be like this (ignore docstring's indentation):
      *
     ***
    *****"""
    data = [f"{' ' * (rows - row)}{'*' * (row * 2 - 1)}" for row in range(1, rows + 1)]
    return "\n".join(data)


if __name__ == "__main__":
    generate_xmas_tree()

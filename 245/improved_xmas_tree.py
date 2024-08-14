STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
    for given rows of leafs (default 10).
    For more information see the test and the bite description"""

    max_width = 2 * (rows - 1) + 1
    lines = [f"{STAR:^{max_width}}"]

    for width in range(rows):
        lines.append(f"{LEAF * (width * 2 + 1):^{max_width}}")
        trunk_width = round(max_width / 2) + 1

    for _ in range(2):
        lines.append(f"{TRUNK * trunk_width:^{max_width}}")

    return "\n".join(lines)

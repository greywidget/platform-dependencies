STAR = "*"


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
    by row. So if width = 5 it should generate the following
    rows one by one:

    gen = gen_rhombus(5)
    for row in gen:
        print(row)

     output:
       *
      ***
     *****
      ***
       *
    """
    SPACE = " "
    space_count = (width - 1) // 2
    star_count = 1
    operand = 1
    while True:
        yield f"{SPACE*space_count}{STAR*star_count}{SPACE*space_count}"

        if star_count == width:
            operand = -1

        star_count += 2 * operand
        space_count -= operand

        if star_count < 1:
            return

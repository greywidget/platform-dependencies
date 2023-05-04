THUMBS_UP, THUMBS_DOWN = "👍", "👎"


class Thumbs:
    def __mul__(self, second):
        if second == 0:
            raise ValueError("Specify a number")

        emoji = THUMBS_UP if second > 0 else THUMBS_DOWN
        second = abs(second)

        return f"{emoji} ({second}x)" if second > 3 else f"{emoji * second}"

    def __rmul__(self, first):
        if first == 0:
            raise ValueError("Specify a number")

        emoji = THUMBS_UP if first > 0 else THUMBS_DOWN
        first = abs(first)

        return f"{emoji} ({first}x)" if first > 3 else f"{emoji * first}"

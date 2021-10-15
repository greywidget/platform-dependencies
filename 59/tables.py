from math import sqrt
class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._table = {
            (x, y): x * y for x in range(1, length + 1)
            for y in range(1, length + 1)
        }

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table)

    def __str__(self):
        """Returns a string representation of the table"""
        vals = [str(value) for value in self._table.values()]
        length = int(sqrt(len(self._table)))
        start, end = 0, length
        diagram = ""
        for _ in range(length):
            diagram += " | ".join(vals[start:end]) + "\n"
            start += length
            end += length
        return diagram

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        result = self._table.get((x, y)) 
        if result:
            return result
        raise IndexError("Invalid coordinates")

if __name__ == "__main__":
    table = MultiplicationTable(3)
    print(table)

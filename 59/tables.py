class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._table = [
            [x * y for y in range(1, length + 1)]
            for x in range(1, length + 1)
        ]

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table) ** 2

    def __str__(self):
        """Returns a string representation of the table"""
        diagram = ""
        for row in self._table:
            alphas = [str(item) for item in row]
            diagram += " | ".join(alphas) + "\n"
            
        return diagram

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        _ = self._table[x-1][y-1]
        return x * y

import random
from enum import Enum
from typing import List, NamedTuple, Optional

from generic_search import Node, dfs, node_to_path


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(
        self,
        rows: int = 10,
        columns: int = 10,
        sparseness: float = 0.2,
        start: MazeLocation = MazeLocation(0, 0),
        goal: MazeLocation = MazeLocation(9, 9),
    ) -> None:
        # Initialize basic instance variables
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal

        # Fill the grid with empty cells
        self._grid: List[List[Cell]] = [
            [Cell.EMPTY for c in range(columns)] for r in range(rows)
        ]

        # Populate the grid with blocked cells
        self._randomly_fill(rows, columns, sparseness)

        # Set the Start and Goal locations
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        """Return a nicely formatted version of the maze for printing"""
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output

    def goal_test(self, m1: MazeLocation) -> bool:
        return m1 == self.goal

    def successors(self, m1: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if (
            m1.row + 1 < self._rows
            and self._grid[m1.row + 1][m1.column] != Cell.BLOCKED
        ):
            locations.append(MazeLocation(m1.row + 1, m1.column))
        if m1.row - 1 >= 0 and self._grid[m1.row - 1][m1.column] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row - 1, m1.column))
        if (
            m1.column + 1 < self._columns
            and self._grid[m1.row][m1.column + 1] != Cell.BLOCKED
        ):
            locations.append(MazeLocation(m1.row, m1.column + 1))
        if m1.column - 1 >= 0 and self._grid[m1.row][m1.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row, m1.column - 1))
        return locations

    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[self.start.row][self.start.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL


def main():
    maze: Maze = Maze()
    print(maze)
    solution1: Optional[Node[MazeLocation]] = dfs(
        maze.start, maze.goal_test, maze.successors
    )
    if solution1 is None:
        print("No solution found using depth-first search!")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)


if __name__ == "__main__":
    main()

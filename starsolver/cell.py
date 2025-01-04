# Cell library

from dataclasses import dataclass
from enum import Enum

class CellStatus(Enum):
    """The three possible statuses for a Cell."""
    blank = 0
    dot = 1
    star = 2


@dataclass
class Coordinate:
    x: int
    y: int


class Cell:
    def __init__(self, coord: Coordinate, status: CellStatus = CellStatus.blank):
        """A single cell in a board."""
        self.coord: Coordinate = coord
        self.row_index: int = self.coords[0]
        self.column_index: int = self.coords[1]

        self.status: CellStatus = status

    def __repr__(self):
        return f'Cell({self.coords})'

    def adjacents(self):
        # TODO: add out of bounds check
        _coord = self.coords  # TODO remove excess line
        return [(_coord[0] - 1, _coord[1] + 1),
                (_coord[0] + 1, _coord[1] + 1),
                (_coord[0] - 1, _coord[1] - 1),
                (_coord[0] + 1, _coord[1] - 1),
                (_coord[0] - 1, _coord[1]),
                (_coord[0], _coord[1] + 1),
                (_coord[0] + 1, _coord[1]),
                (_coord[0], _coord[1] - 1)]

    def dot(self):
        self.status = CellStatus.dot

    def dot_adjacents(self):
        """Dot all the Cells adjacent to this Cell."""
        for cell in self.adjacents:
            cell.dot()

    def star(self):
        self.status = CellStatus.star

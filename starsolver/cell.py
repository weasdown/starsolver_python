# Cell library

from enum import Enum

class CellStatus(Enum):
    """The three possible statuses for a Cell."""
    blank = 0
    dot = 1
    star = 2


class Cell:
    def __init__(self, coords: tuple, status: CellStatus = CellStatus.blank):
        """A single cell in a board."""
        self.coords = coords
        self.row = self.coords[0]
        self.column = self.coords[1]

        self.status: CellStatus = status

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
    
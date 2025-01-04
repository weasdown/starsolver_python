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

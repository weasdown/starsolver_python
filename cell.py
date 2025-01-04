# Cell library

from enum import Enum

class Cell:
    def __init__(self, coords: tuple):
        """A single cell in a board."""
        self.coords = coords
        self.row = self.coords[0]
        self.column = self.coords[1]

        self.status = ...  # TODO empty, dotted or starred

class CellStatus(Enum):
    """The three possible statuses for a Cell."""
    blank = 0
    dot = 1
    star = 2

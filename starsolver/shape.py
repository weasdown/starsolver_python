# Shape class

from starsolver.cell import Cell

class Shape:
    def __init__(self, cells: list[Cell]):
        """A single coloured shape within a Board, that contains several Cells."""

        self.cells: list[Cell] = cells

        raise NotImplementedError

# Board library

from starsolver.cell import Cell, CellStatus
from .shape import Shape

import numpy as np

class Board:
    dimension: int = 9  # Number of Cells on a side of the Board

    def __init__(self):
        """A 9x9 board in which a puzzle takes place."""
        self.rows: list[Row] = [Row(index) for index in  range(self.dimension)]
        self.columns: list[Column] = [Column(index) for index in  range(self.dimension)]

        self.shapes: list[Shape] = ...  # TODO implement shapes

        self.cells: list[Cell] = [cell for row in self.rows for cell in row.cells]

    @property
    def is_complete(self) -> bool:
        """Gets whether the Board has been completed and is valid."""
        raise NotImplementedError
    
    @property
    def is_valid(self) -> bool:
        """Gets whether the Board is valid."""
        raise NotImplementedError

    @property
    def num_stars(self) -> int:
        """Gets how many stars are in the Board."""
        starred_cells: list[Cell] = [cell for cell in self.cells if cell.status == CellStatus.star]
        return len(starred_cells)

class Column:
    def __init__(self, index: int):
        self.index: int = index
        
        self.cells: list[Cell] = [Cell((self.index, vert_index)) for vert_index in range(Board.dimension)]

    def __repr__(self):
        return f'Column({self.index})'

class Row:
    def __init__(self, index: int):
        self.index: int = index
        
        self.cells: list[Cell] = [Cell((horiz_index, self.index)) for horiz_index in range(Board.dimension)]

    def __repr__(self):
        return f'Row({self.index})'

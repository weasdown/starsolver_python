# Board library

# from .cell import Cell
# import cell as c
from starsolver.cell import Cell
from .shape import Shape

import numpy as np

class Board:
    def __init__(self):
        """A 9x9 board in which a puzzle takes place."""
        self.dimension: int = 9  # Number of Cells on a side of the Board
        self.rows: np.array[Cell] = [Row(index) for index in  range(self.dimension)]
        self.columns: np.array[Cell] = [Column(index) for index in  range(self.dimension)]

        self.shapes: list[Shape] = ...  # TODO implement shapes

    @property
    def is_complete(self) -> bool:
        """Gets whether the Board has been completed and is valid."""
        raise NotImplementedError
    
    @property
    def is_valid(self) -> bool:
        """Gets whether the Board is valid."""
        raise NotImplementedError

class Column:
    def __init__(self, index: int):
        self.index: int = index
        
        self.cells: list[Cell] = ...  # TODO implement cells

    def __repr__(self):
        return f'Column({self.index})'

class Row:
    def __init__(self, index: int):
        self.index: int = index
        
        self.cells: list[Cell] = ...  # TODO implement cells

    def __repr__(self):
        return f'Row({self.index})'

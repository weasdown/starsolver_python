# Board library

from cell import Cell
from shape import Shape

import numpy as np

class Board:
    def __init__(self):
        """A 9x9 board in which a puzzle takes place."""
        self.rows: np.ndarray[Cell] = ...  # TODO implement rows
        self.columns: np.ndarray[Cell] = ...  # TODO implement columns

        self.shapes: list[Shape] = ...  # TODO implement shapes

    @property
    def is_complete(self) -> bool:
        """Gets whether the Board has been completed and is valid."""
        raise NotImplementedError
    
    @property
    def is_valid(self) -> bool:
        """Gets whether the Board is valid."""
        raise NotImplementedError


"""Type definitions to be used for rows and columns in Board."""
# TODO convert to numpy arrays
type Column = np.ndarray[Cell]
type Row = np.ndarray[Cell]

# Board library

from cell import Cell
from shape import Shape

class Board:
    def __init__(self):
        """A 9x9 board in which a puzzle takes place."""
        self.rows: list[Row] = ...  # TODO implement rows
        self.columns: list[Column] = ...  # TODO implement columns

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
type Column = list[Cell]
type Row = list[Cell]

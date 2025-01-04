# Board library

from cell import Cell
from shape import Shape

class Board:
    def __init__(self):
        pass
        self.rows: list[Row] = ...  # TODO implement rows
        self.columns: list[Column] = ...  # TODO implement columns

        self.shapes: list[Shape] = ...  # TODO implement shapes


"""Type definitions to be used for rows and columns in Board."""
type Column = list[Cell]
type Row = list[Cell]

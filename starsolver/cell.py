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
            # if not isinstance(_coord, tuple):
            #     raise SyntaxError('coord must be a tuple')
            print(f'Dotting cell {self.coords}...')
            
            adjacents: list[Cell] = self.adjacents()
            for cell in adjacents:
                print(f"'Dotted' {cell} NOT REALLY!!")

    def dot_adjacent(self,_coord: tuple):
        # FIXME
        if not isinstance(_coord, tuple):
            raise SyntaxError('coord must be a tuple')
        else:
            self.dot()

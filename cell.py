# Cell class

class Cell:
    def __init__(self, coords: tuple):
        self.coords = coords
        self.row = self.coords[0]
        self.column = self.coords[1]

        self.status = ...  # TODO empty, dotted or starred


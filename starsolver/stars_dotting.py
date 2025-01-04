def adjacents_to_cell(_coord: tuple):
    # TODO: add out of bounds check
    return [(_coord[0] - 1, _coord[1] + 1),
            (_coord[0] + 1, _coord[1] + 1),
            (_coord[0] - 1, _coord[1] - 1),
            (_coord[0] + 1, _coord[1] - 1),
            (_coord[0] - 1, _coord[1]),
            (_coord[0], _coord[1] + 1),
            (_coord[0] + 1, _coord[1]),
            (_coord[0], _coord[1] - 1)]


def dot_cell(_coord: tuple):
    if not isinstance(_coord, tuple):
        raise SyntaxError('coord must be a tuple')
    print(f'Dotting cell {_coord}...')
    adjacents = adjacents_to_cell(_coord)
    for cell in adjacents:
        print(f"'Dotted' {cell} NOT REALLY!!")


def dot_adjacent(_coord: tuple):
    if not isinstance(_coord, tuple):
        raise SyntaxError('coord must be a tuple')
    else:
        dot_cell(_coord)

# TODO remove
if __name__ == '__main__':
    coord = (0, 0)
    dot_adjacent(coord)

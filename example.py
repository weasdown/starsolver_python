# Example of using the solver

import starsolver as s

board: s.Board = s.Board()

print(f'{board.num_blanks = }')
print(f'{board.num_dots = }')
print(f'{board.num_stars = }\n')

board[0][0].dot()
print(board[0][0])

print(f'\n{board.num_blanks = }')
print(f'{board.num_dots = }')
print(f'{board.num_stars = }')

print(f'\n{board[0].cells}')

print(f'Full board:\n'
      f'{board}')

print('\nFirst row of board:\n'
      f'{board.rows[0].board_print()}')


class color:
    """Copied from https://stackoverflow.com/questions/8924173/how-can-i-print-bold-text-in-python
    For coloured text: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal?noredirect=1&lq=1"""
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print(color.BOLD + 'Hello, World!' + color.END)

# Builds a Board instance from an image of a board.

import cv2
import numpy as np

import starsolver as s


def trim_rows(image: np.ndarray, num_rows: int, from_top: bool = True) -> np.ndarray:
    if from_top:
        return image[num_rows: -1]  # trim top
    else:
        return image[0: -num_rows]


def trim_columns(image: np.ndarray, num_columns: int, from_left: bool = True):
    if from_left:
        return np.delete(image, slice(num_columns), axis=1)
    else:
        return np.delete(image, slice(-num_columns, None), axis=1)


def resize_with_aspect_ratio(image: np.ndarray, width: float = None, height: float = None, inter: int = cv2.INTER_AREA):
    """
    Resize an image, maintaining its original aspect ratio.

    Based on https://stackoverflow.com/a/58126805.

    :param image: The image to resize.
    :param width: Width of the output image, in pixels.
    :param height: Height of the output image, in pixels.
    :param inter: The type of interpolation to use when resizing.
    :return: The resized image.
    """
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


def cropped_board(image: np.ndarray) -> np.ndarray:
    """
    Returns an image of the edges in an original image.

    Based on https://www.geeksforgeeks.org/real-time-edge-detection-using-opencv-python/ and https://www.youtube.com/watch?v=f6VgWTD_7kc.

    :param image:
    :return:
    """

    # Convert the frame to grayscale for edge detection
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    threshold_max: int = 255
    _, threshold = cv2.threshold(grey, np.mean(grey, dtype=int), threshold_max, cv2.THRESH_BINARY)
    threshold = threshold.__invert__()

    black_row: np.ndarray = np.zeros(shape=(image.shape[1]))

    def start_is_white(array: np.ndarray) -> bool:
        return array[0] == threshold_max

    # Indices for the board edges, so we can later crop the original image in the same way so it just shows the board, but in colour.
    top_edge_index: int | None = None
    bottom_edge_index: int | None = None

    # We assume the board has a black border to its left, so remove rows from the top that start with white or are pure black.
    trimmed_top_and_bottom_rows = []
    for index, row in enumerate(threshold):
        if not (start_is_white(row) or np.array_equal(row, black_row)):
            trimmed_top_and_bottom_rows.append(row)
            if top_edge_index is None:
                top_edge_index = index + 1
        else:
            # To see if we should save the index as bottom_edge_index, see if we have found the top_edge_index.
            # If we haven't, we're still above the board.
            # If we have, and we've not set bottom_edge_index yet, the next pure black row is the first below the board.
            if (top_edge_index is not None) and (bottom_edge_index is None):
                bottom_edge_index = len(image) - index - 1

    trimmed_top: np.ndarray = np.array(trimmed_top_and_bottom_rows)

    # We know that the top row of trimmed_top has white at the left and right edges of the board, so use this to get the pixel indices for the left and right edges.
    first_row: np.ndarray = trimmed_top[0]

    # Remove the left black border
    left_edge_index = int(np.argmax(first_row > 0)) + 1
    trimmed_left = np.delete(trimmed_top, slice(left_edge_index), axis=1)

    # Remove the right black border
    right_edge_index = int(np.argmax(np.flip(trimmed_left, axis=1) == threshold_max))

    # Crop the original image to the same extent as board_only
    board_only_colour: np.ndarray = trim_columns(image, left_edge_index)  # trim left
    board_only_colour = trim_columns(board_only_colour, right_edge_index, False)  # trim right
    board_only_colour = trim_rows(board_only_colour, top_edge_index)  # trim top
    board_only_colour = trim_rows(board_only_colour, bottom_edge_index, False)  # trim bottom

    return board_only_colour


def board_from_image(board_image: np.ndarray) -> s.Board:
    # Trim the black border around the board
    border_thickness: int = 8
    trim_top_bottom = trim_rows(trim_rows(board_image, border_thickness), border_thickness, False)
    no_border = trim_columns(trim_columns(trim_top_bottom, border_thickness), border_thickness, False)

    width = no_border.shape[0]

    cv2.imshow('Border removed', resize_with_aspect_ratio(no_border, height=600))

    # Build a set of 9 coordinates for pixels whose colour will be evaluated to get the cell's colour.
    test_pixels = []

    cell_side: float = width / 9

    cell_centres: list[list[tuple[int, int]]] = []
    cell_colours: list[list[int]] = []
    cells: list[list[s.Cell]] = []

    dot_star_colour: list[int] = [66, 66, 66]

    board_ninth = width / 9

    for x_index in range(9):
        row_cell_centres: list[tuple[int, int]] = []
        row_test_pixels: list[tuple[int, int]] = []
        row_cells: list[s.Cell] = []

        for y_index in range(9):
            x: int = round(board_ninth * x_index)
            y: int = round(board_ninth * y_index)

            cell_centre: tuple[int, int] = (round(cell_side * x_index + cell_side / 2),
                                            round(cell_side * y_index + cell_side / 2))
            cell_background_pixel: tuple[int, int] = (x + 15, y + 15)
            cell_star_test_pixel: tuple[int, int] = (cell_centre[0], round(cell_centre[1] + cell_side / 7))

            row_cell_centres.append(cell_centre)
            row_test_pixels.append(cell_background_pixel)

            background_colour: list[int] = [int(colour) for colour in
                                            no_border[cell_background_pixel[0], cell_background_pixel[1]]]
            centre_colour: list[int] = [int(colour) for colour in no_border[cell_centre[0], cell_centre[1]]]
            star_test_colour: list[int] = [int(colour) for colour in
                                           no_border[cell_star_test_pixel[0], cell_star_test_pixel[1]]]

            if background_colour not in cell_colours:
                cell_colours.append(background_colour)

            cell_object = s.Cell(s.Coordinate(x_index, y_index))

            if centre_colour == dot_star_colour:
                cell_object.status = s.CellStatus.dot
            else:
                if star_test_colour != background_colour:
                    cell_object.status = s.CellStatus.star
                elif centre_colour == background_colour:
                    cell_object.status = s.CellStatus.blank
                else:
                    print(f'\n!! Cell status could not be identified for cell at ({x_index}, {y_index}).\n'
                          f'\t- Centre pixel: {cell_centre}\n'
                          f'\t- Background colour: {background_colour}\n'
                          f'\t- Centre colour: {centre_colour} (== dot_star_colour? {centre_colour == dot_star_colour})\n'
                          f'\t- Star test colour: {star_test_colour} !!')

            row_cells.append(cell_object)

        cell_centres.append(row_cell_centres)
        test_pixels.append(row_test_pixels)
        cells.append(row_cells)

    print()
    for i in range(9):
        print(f'Row {i}: {[cell.status.name for cell in cells[i]]}')

    # TODO add splitting of board image in a pixel group for each cell, then convert these to Cells. Then build Shapes. Then build Board.

    b: s.Board = s.Board()

    return b


def ingest(image_path: str) -> s.Board:
    """
    Builds a Board instance from an image of a board.

    :param image_path: The path to an image of the required board.
    :return: A Board instance matching the board in the input image.
    """

    # TODO implement ingest

    original: np.ndarray = cv2.imread(image_path)

    edges: np.ndarray = cropped_board(original)

    # cv2.imshow('Board', resize_with_aspect_ratio(edges, height=600))

    b: s.Board = board_from_image(edges)

    cv2.waitKey(0)  # wait for any key to be pressed
    cv2.destroyAllWindows()

    return b

# Builds a Board instance from an image of a board.

import cv2
import numpy as np

import starsolver as s


def trim_rows(image: np.ndarray, num_rows: int, from_top: bool = True) -> np.ndarray:
    if from_top:
        return image[num_rows: -1]  # trim top
    else:
        return image[0: -num_rows + 1]


def trim_columns(image: np.ndarray, num_columns: int, from_left: bool = True):
    if from_left:
        return np.delete(image, slice(num_columns), axis=1)
    else:
        return np.delete(image, slice(-num_columns - 1, None), axis=1)


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
                top_edge_index = index
        else:
            # To see if we should save the index as bottom_edge_index, see if we have found the top_edge_index.
            # If we haven't, we're still above the board.
            # If we have, and we've not set bottom_edge_index yet, the next pure black row is the first below the board.
            if (top_edge_index is not None) and (bottom_edge_index is None):
                bottom_edge_index = len(image) - index

    trimmed_top: np.ndarray = np.array(trimmed_top_and_bottom_rows)

    # We know that the top row of trimmed_top has white at the left and right edges of the board, so use this to get the pixel indices for the left and right edges.
    first_row: np.ndarray = trimmed_top[0]

    # Remove the left black border
    left_edge_index = int(np.argmax(first_row > 0))
    trimmed_left = np.delete(trimmed_top, slice(left_edge_index), axis=1)

    # Remove the right black border
    right_edge_index = int(np.argmax(np.flip(trimmed_left, axis=1) == threshold_max)) - 1

    # Crop the original image to the same extent as board_only
    board_only_colour: np.ndarray = trim_columns(image, left_edge_index)  # trim left
    board_only_colour = trim_columns(board_only_colour, right_edge_index, False)  # trim right
    board_only_colour = trim_rows(board_only_colour, top_edge_index)  # trim top
    board_only_colour = trim_rows(board_only_colour, bottom_edge_index, False)  # trim bottom

    return board_only_colour


def board_from_image(board_image: np.ndarray) -> s.Board:
    print('Building a Board instance from board_image')

    print(board_image[0])

    # Trim the black border around the board
    border_thickness: int = 20  # TODO calculate exact value
    trim_top_bottom = trim_rows(trim_rows(board_image, border_thickness), border_thickness, False)
    no_border = trim_columns(trim_columns(trim_top_bottom, border_thickness), border_thickness, False)

    # cv2.imshow('Border removed', resize_with_aspect_ratio(no_border, height=600))

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

    cv2.imshow('Board', resize_with_aspect_ratio(edges, height=600))

    b: s.Board = board_from_image(edges)

    cv2.waitKey(0)  # wait for any key to be pressed
    cv2.destroyAllWindows()

    return b

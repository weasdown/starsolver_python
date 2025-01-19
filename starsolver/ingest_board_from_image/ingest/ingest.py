# Builds a Board instance from an image of a board.

import cv2
import numpy as np

import starsolver as s


def image_edges(image: np.ndarray) -> np.ndarray:
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
    white_row: np.ndarray = np.full(shape=(image.shape[1]), fill_value=threshold_max)

    def start_is_white(array: np.ndarray) -> bool:
        return array[0] == threshold_max

    # Remove any rows that are pure black, pure white or start with white (we assume a black border around the board).
    trimmed_top_rows = []
    for index, row in enumerate(threshold):
        if not (np.array_equal(row, black_row)
                or np.array_equal(row, white_row)
                or start_is_white(row)):
            trimmed_top_rows.append(row)

    image_num_rows: int = len(image)

    trimmed_top: np.ndarray = np.array(trimmed_top_rows)

    # We know that the top row of trimmed_top has white at the left and right edges of the board, so use this to get the pixel indices for the left and right edges.
    first_row: np.ndarray = trimmed_top[0]

    # Remove the left black border
    left_edge_index = np.argmax(first_row > 0)
    trimmed_left = np.delete(trimmed_top, slice(left_edge_index), axis=1)

    # Remove the right black border
    right_edge_index = np.argmax(np.flip(trimmed_left, axis=1) == threshold_max)
    trimmed_right = np.delete(trimmed_left, slice(-right_edge_index, None), axis=1)

    # Remove rows below board bottom edge
    board_only: np.ndarray = np.array([row for row in trimmed_right if row[0] == threshold_max])

    final_image = board_only.__invert__()

    return final_image


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


def ingest(image_path: str) -> s.Board:
    """
    Builds a Board instance from an image of a board.

    :param image_path: The path to an image of the required board.
    :return: A Board instance matching the board in the input image.
    """

    # TODO implement ingest

    original: np.ndarray = cv2.imread(image_path)

    edges: np.ndarray = image_edges(original)

    cv2.imshow('Original', resize_with_aspect_ratio(original, height=800))
    cv2.imshow('Edges', resize_with_aspect_ratio(edges, height=800))

    cv2.waitKey(0)  # wait for any key to be pressed
    cv2.destroyAllWindows()

    b: s.Board = s.Board()
    return b

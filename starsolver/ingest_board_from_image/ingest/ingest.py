# Builds a Board instance from an image of a board.

import cv2
import numpy as np

import starsolver as s


def image_edges(image: np.ndarray) -> np.ndarray:
    """
    Returns an image of the edges in an original image.

    Based on https://www.geeksforgeeks.org/real-time-edge-detection-using-opencv-python/.

    :param image:
    :return:
    """

    # Convert the frame to grayscale for edge detection
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and smoothen edges
    blurred = cv2.GaussianBlur(src=grey, ksize=(3, 5), sigmaX=0.5)

    # Perform Canny edge detection
    edges = cv2.Canny(grey, 70, 135)
    return edges


def ingest(image_path: str) -> s.Board:
    """
    Builds a Board instance from an image of a board.

    :param image_path: The path to an image of the required board.
    :return: A Board instance matching the board in the input image.
    """

    # TODO implement ingest

    original: np.ndarray = cv2.imread(image_path)

    edges: np.ndarray = image_edges(original)

    b: s.Board = s.Board()
    return b

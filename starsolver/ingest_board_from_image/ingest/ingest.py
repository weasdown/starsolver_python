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

    # # TODO remove Gaussian blur if not needed
    # # Apply Gaussian blur to reduce noise and smoothen edges
    # blurred = cv2.GaussianBlur(src=grey, ksize=(3, 5), sigmaX=0.5)

    # Perform Canny edge detection
    edges = cv2.Canny(grey, 70, 135)
    return edges


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
    dim = None
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
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    b: s.Board = s.Board()
    return b

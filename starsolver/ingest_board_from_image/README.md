# Ingest a Board from an image

This directory contains a Python package for building a `Board` instance from an image of a `Board` (either complete or incomplete).

The package uses [openCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) to extract the Board from an image.
 A sample images are provided for blank and complete boards in `samples`.

## Method

The function `ingest()` that performs the actual ingestion works as follows:

1. Reads the image into a `numpy.ndarray`.
2. Performs a [Canny edge detection] on the imported image to find edges.
3. Using the edges, crop the image down to just the board itself (so removing the rest of Star Battle app, any notification bar, etc.).
4. Split the `edges` array by the edge lines, to get an array of 'cells', where each 'cell' is a group of pixels.
5. Convert each 'cell' into a `Cell` instance.
6. Build a `Board` instance from the `Cell`s.

[Canny edge detection]: https://www.geeksforgeeks.org/real-time-edge-detection-using-opencv-python/

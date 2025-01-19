# Example of creating a Board instance from an image of a board.

import os

import ingest
import starsolver as s

# Assume the samples folder is in the same directory as this file.
samples_path: str = f'{os.path.dirname(os.path.realpath(__file__))}/samples'
sample_image_name: str = 'sample_complete.png'

b: s.Board = ingest.ingest(image_path=f'{samples_path}/{sample_image_name}')
print(b)

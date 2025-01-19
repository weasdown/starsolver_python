# Example of creating a Board instance from an image of a board.

import ingest
import starsolver as s

samples_path: str = 'samples'
sample_image_name: str = 'sample_complete.png'

b: s.Board = ingest.ingest(image_path=f'{samples_path}/{sample_image_name}')
print(b)

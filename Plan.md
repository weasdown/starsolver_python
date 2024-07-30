# Star Solver Plan
This document lists various methods that will be needed for the Star Solver classes.

## Needed methods:
### Cell
- Set dot
- Set star
- Set adjacent to dotted

- Get dotted (bool)
- Get star (bool)

### CellHolder
Interface class for some Row, Column and Shape methods.
- Get cell groups (list[CellGroup])

### Row/Column
Note that Row and Column will be separate classes as they will handle coordinates differently (one going horizontally, the other vertically).
- TBC

### CellGroup
- TBC

### Column
- TBC

### Shape
- TBC

### Board
- Is complete (bool)
- Is valid so far (bool)
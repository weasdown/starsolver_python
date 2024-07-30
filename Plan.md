# Star Solver Plan
This document lists various methods and attributes that will be needed for the Star Solver classes.

## Needed methods:
### Cell
#### Methods
- Set dot
- Set star
- Set adjacent to dotted

- Get dotted (bool)
- Get star (bool)

#### Attributes
- Status (CellStatus enum)

### CellHolder
Interface class for some Row, Column and Shape methods.

#### Methods
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
#### Methods
- Is complete (bool)
- Is valid so far (bool)

#### Attributes
- Shapes (list[Shape])

## Program flow
1. Generate list of shapes, including assigning all cells to correct Shape, Row and Column.
2. Check for special shapes.
3. TBC
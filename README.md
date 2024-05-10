# Star Solver
A Python solver for "Star Battle"/"Two Not Touch" puzzles. Valid only for a 9x9 grid (so 18 stars).

# Pseudocode
- When adding star:
    1. Set cell to starred
    2. Check whether grid solved
    3. Set adjacent cells to dotted
    4. Update cell groups for:
        a. shape
        b. row
        c. column
    5. Check whether new groups allow extra star in:
        a. shape
        b. row
        c. column
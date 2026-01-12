'''Pseudo Code 
Create a grid of # and -, where hash (#) represents a mine and dash (-) represents a mine-free spot.
Return a grid where each dash (-) is replaced by a digit, indicating the number of mines immediately adjacent to the spot (horizontally, vertically and diagonally).
Ensure when checking adjacent positions in the grid that edges on the grid areas may be out of bounds.
Create functions Within_bounds function to check whether a particular row and column combination (cell) is a position within bounds.'''

# Create Minesweeper board
grid = [['-','-','-','-','#'],
        ['-','#','-','#','-'],
        ['-','-','-','#','#'],
        ['-','#','#','-','-'],
        ['#','-','-','-','-']]

# Within_bounds function
def within_bounds(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

# Checks all 8 directions around a cell function
def count_adjacent_mines(grid, row, col):
      count = 0
      for row_index in [-1,0,1]:
           for col_index in [-1,0,1]:
                if row_index == 0 and col_index == 0:
                     continue
                new_row, new_col = row + row_index, col + col_index
                if within_bounds(grid, new_row, new_col) and  grid[new_row][new_col] == '#':
                      count += 1 
      return count

# Replace dashes with number of mines around
def game_grid(grid):
    return [
        [ '#' if cell == '#' else str(count_adjacent_mines(grid, row_idx, col_idx))
          for col_idx, cell in enumerate(row) ]
        for row_idx, row in enumerate(grid)
    ]
# Generate a new grid with counts or mines
def Output_board(grid):
     for row in grid:
          print(' '.join(row))

# Print the grid 
print("Original Grid: ")
Output_board(grid)

print("\nProcessed Grid: ")
Output_board(game_grid(grid))

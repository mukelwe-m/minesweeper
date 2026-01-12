# Minesweeper
This code is a grid processor that:

Takes a pre-defined grid with mines already placed
Calculates how many mines are adjacent to each cell
Displays the result

It's the algorithm that powers Minesweeper, but not the actual game itself. Think of it as the "backend logic" or "number calculation engine."

## Features

- **Grid Processing**: Converts raw mine positions into a numbered grid
- **Boundary Checking**: Safely handles edge and corner cases
- **Adjacent Mine Counting**: Checks all 8 directions (horizontal, vertical, and diagonal)
- **Visual Output**: Displays both original and processed grids

## How It Works

### Grid Representation

- `#` represents a mine
- `-` represents a mine-free spot
- Numbers (0-8) indicate the count of adjacent mines

### Core Functions

#### `within_bounds(grid, row, col)`
Validates whether a given row and column position exists within the grid boundaries.

**Parameters:**
- `grid`: The game board
- `row`: Row index to check
- `col`: Column index to check

**Returns:** `True` if position is valid, `False` otherwise

#### `count_adjacent_mines(grid, row, col)`
Counts the number of mines in all 8 adjacent cells (horizontally, vertically, and diagonally).

**Parameters:**
- `grid`: The game board
- `row`: Row index of the cell
- `col`: Column index of the cell

**Returns:** Integer count of adjacent mines (0-8)

#### `game_grid(grid)`
Transforms the original grid by replacing dashes with mine counts while preserving mine positions.

**Parameters:**
- `grid`: The original game board

**Returns:** Processed grid with mine counts

#### `Output_board(grid)`
Displays the grid in a formatted, human-readable layout.

**Parameters:**
- `grid`: The grid to display

## Example

### Input Grid:
```
- - - - #
- # - # -
- - - # #
- # # - -
# - - - -
```

### Output Grid:
```
1 1 2 2 #
1 # 3 # 3
2 3 4 # #
2 # # 3 2
# 2 2 1 0
```

## Usage

1. Define your grid with mines (`#`) and empty spots (`-`)
2. Run the program:
```python
python minesweeper.py
```

3. View both the original and processed grids in the console

## Code Structure

```python
# Define the grid
grid = [['-','-','-','-','#'],
        ['-','#','-','#','-'],
        ['-','-','-','#','#'],
        ['-','#','#','-','-'],
        ['#','-','-','-','-']]

# Process and display
print("Original Grid: ")
Output_board(grid)

print("\nProcessed Grid: ")
Output_board(game_grid(grid))
```

## Algorithm Details

The mine counting algorithm:
1. Iterates through all 8 adjacent positions using offset pairs
2. Skips the center cell (0, 0 offset)
3. Validates each position is within bounds
4. Increments counter when a mine is found
5. Returns the total count

## Requirements

- Python 3.x
- No external dependencies

## Demo

Try the [interactive demo](http://mukelwe-m.github.io/minesweeper/)) to see the algorithm in action!

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Future Enhancements

- Game play functionality with revealing cells
- Flag placement for suspected mines
- Timer and scoring system

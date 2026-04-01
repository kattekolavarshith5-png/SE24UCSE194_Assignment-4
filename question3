# Sudoku Solver using CSP (Backtracking)

grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# Check constraints
def is_valid(board, row, col, num):
    # Row check
    if num in board[row]:
        return False

    # Column check
    for i in range(9):
        if board[i][col] == num:
            return False

    # 3x3 Box check
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Backtracking CSP
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve(board):
                            return True

                        # Backtrack
                        board[row][col] = 0

                return False
    return True

# Solve Sudoku
solve(grid)

# Print Solution
print("Solved Sudoku:\n")
for row in grid:
    print(row)

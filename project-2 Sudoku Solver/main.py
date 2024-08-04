class Sudoku:
    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        for x in range(9):
            if self.board[row][x] == num:
                return False

        for x in range(9):
            if self.board[x][col] == num:
                return False

        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve_sudoku(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(i, j, num):
                            self.board[i][j] = num
                            if self.solve_sudoku():
                                return True
                            self.board[i][j] = 0
                    return False
        return True

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

## Driver code
board = [
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 3, 5, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 6, 8],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 4, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 5],
    [0, 0, 1, 0, 0, 0, 0, 0, 0]
]
solver = Sudoku(board)

print("Real Board:")
solver.print_board()

if solver.solve_sudoku():
    print("Solved Board:")
    solver.print_board()
else:
    print("No solution exists")
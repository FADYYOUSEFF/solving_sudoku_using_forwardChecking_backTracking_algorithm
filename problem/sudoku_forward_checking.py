class Solution:
    def __init__(self):
        self.map_row = {}
        self.map_col = {}
        self.map_box = {}
        self.found = False

    def solveSudoku(self, board):
        # Initialize all sets with full possible values
        self.initializeConstraints()
        # Remove existing numbers from the sets
        self.remveAssignedValues(board)
        
        self.forwardChecking(0, 0, board)

    def forwardChecking(self, r, c, board):
        if r == 9:
            self.found = True
            return

        if board[r][c] != '.':
            # Move to next cell
            if c == 8:
                self.forwardChecking(r + 1, 0, board)
            else:
                self.forwardChecking(r, c + 1, board)
            return

        # Find intersection of possible values for row, column and box
        possibleValues = self.map_row[r] & self.map_col[c] & self.map_box[self.mapToBox(r, c)]

        for val in possibleValues:
            # Place the value
            board[r][c] = val
            self.map_row[r].remove(val)
            self.map_col[c].remove(val)
            self.map_box[self.mapToBox(r, c)].remove(val)

            # Move to next cell
            if c == 8:
                self.forwardChecking(r + 1, 0, board)
            else:
                self.forwardChecking(r, c + 1, board)

            # If solution found, don't forwardChecking
            if self.found:
                return

            # Backtrack
            board[r][c] = '.'
            self.map_row[r].add(val)
            self.map_col[c].add(val)
            self.map_box[self.mapToBox(r, c)].add(val)

    def mapToBox(self, row, col):
        return (row // 3) * 3 + (col // 3)

    def initializeConstraints(self):
        for i in range(9):
            self.map_row[i] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            self.map_col[i] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            self.map_box[i] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def remveAssignedValues(self, board):
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell != '.':
                    self.map_row[row].discard(cell)
                    self.map_col[col].discard(cell)
                    self.map_box[self.mapToBox(row, col)].discard(cell)
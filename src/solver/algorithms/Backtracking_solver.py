import sys


class BacktrackingSolver(object):
    def __init__(self):
        # Common fields
        self.puzzle = []  # Initialize the puzzle
        self.blanks = []  # Initialize blank spots
        self.initPuzzleArray()  # Construct an array of 0 0 0 0 0...

    def solve(self, index=0):
        """
    Solve Sudoku using plain backtracking.
    Uses a recursive algorithm to try each value 1-9 in each blank square,
    backtracking when it was not able to put in any value into the square.
        """
        # Found a solution if we have gone past the last blank
        if index > len(self.blanks) - 1:
            result = self.endAlgorithm()
            return result
            # return self.outputSolution()

        # Haven't found a solution yet; get coords of the blank
        row = self.blanks[index][0]
        col = self.blanks[index][1]
        # Try numbers 1-9.
        for num in range(1, 10):
            if self.puzzle[row][col] == 0:
                if self.puzzleValid(row, col, num):
                    self.puzzle[row][col] = num
                    self.solve(index + 1)

        index -= 1
        self.puzzle[row][col] = 0

    def puzzleValid(self, row, col, num):
        """
    CSP VALIDATORS - Check if the current puzzle is legal after placing num in (row, col).
        """
        valid = False
        if num == 0:
            return True
        else:
            # Return true if row, column, and box have no violations
            rowValid = self.checkRow(row, num)
            colValid = self.checkColumn(col, num)
            boxValid = self.checkBox(row, col, num)
            valid = (rowValid & colValid & boxValid)

        return valid

    def checkRow(self, row, num):
        """
    CSP VALIDATORS - Check if num is a legal value for the given row.
        """
        for col in range(9):
            currentValue = self.puzzle[row][col]
            if num == currentValue:
                return False
        return True

    def checkColumn(self, col, num):
        """
    CSP VALIDATORS - Check if num is a legal value for the given column.
        """
        for row in range(9):
            currentValue = self.puzzle[row][col]
            if num == currentValue:
                return False
        return True

    def checkBox(self, row, col, num):
        """
    CSP VALIDATORS - Check if num is a legal value for the box (one of 9 boxes) containing given row/col
        """
        row = (row / 3) * 3
        col = (col / 3) * 3

        for r in range(3):
            for c in range(3):
                if self.puzzle[row + r][col + c] == num:
                    return False
        return True

    def endAlgorithm(self):
        """
    ALGORITHM HELPERS - Generic method to end the algorithm in process and output the solution
        """
        self.outputSolution()
        return True

    def getEmptyCells(self, puzzle):
        """
    ALGORITHM HELPERS - Get all the empty cells in the puzzle.
        """
        emptyCells = []
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    emptyCells.append((i, j))
        return emptyCells

    def initPuzzleArray(self):
        """
    I/O HELPERS - Constructs the blank puzzle array to have 0 0 0 0 0...for all rows and columns
        """
        del self.puzzle[:]
        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append([])
                self.puzzle[i][j] = 0

    def loadPuzzle(self, inputstr):
        """
    I/O HELPERS - Loads a puzzle file into the program and makes sure that
    it is valid.
        """
        possibleTokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        puzzleText = inputstr.split("\n")
        for row in range(9):
            lineTokens = puzzleText[row + 1].split()  # take care because row+1, before was row
            if len(lineTokens) != 9:
                print "Improper file format! Line length must always be 9"
                sys.exit(1)
            for col in range(9):
                token = lineTokens[col].split()[0].strip()
                if token == '-':
                    token = 0  # Change the '-'s to 0s
                token = int(token)
                if token not in possibleTokens:
                    print "Invalid token found"
                    print "Token: " + str(token) + " possible: ", possibleTokens
                    sys.exit(1)

                self.puzzle[row][col] = int(token)
        self.blanks = self.getEmptyCells(self.puzzle)  # Construct the list of blanks
        print ""

    def outputSolution(self):
        """
    I/O HELPERS - Write the solution to a string
        """
        rowString = ""
        for i in range(9):
            for j in range(9):
                rowString += str(self.puzzle[i][j]) + " "
            rowString += "\n"
        return rowString
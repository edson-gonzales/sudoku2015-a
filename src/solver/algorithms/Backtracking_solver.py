"""
Usage:
A properly formatted string is 9 lines of 9 numbers or dashes separated by blanks,
where a dash indicates a blank location in the puzzle.
"""

import sys


class BacktrackingSolver(object):
    def __init__(self):
        # Common fields
        self.puzzle = []  # Initialize the puzzle
        self.blanks = []  # Initialize blank spots
        self.initPuzzleArray()  # Construct an array of 0 0 0 0 0...

        # Initialize the metrics
        self.pathLengths = []  # Hold all the path lengths for metrics
        self.currentPathLength = 0  # Hold the local path length
        self.blanks = self.getEmptyCells(self.puzzle)  # Construct the list of blanks

    #######################################################
    # THE BACKTRACKING SOLUTION                           #
    #######################################################
    """
    Solve Sudoku using plain backtracking
    Uses a recursive algorithm to try each value 1-9 in each blank square,
    backtracking when it was not able to put in any value into the square.
    """

    def solve(self, index=0):
        # Found a solution if we have gone past the last blank
        # print(index)  # index = 0
        if index > len(self.blanks) - 1:
            print "entered to here " + str(index) + str(len(self.blanks))
            self.endAlgorithm()
            # return self.outputSolution()

        # Haven't found a solution yet; get coords of the blank
        print "myValue printed" + str(index)
        row = self.blanks[index][0]
        col = self.blanks[index][1]
        int(col)

        # Try numbers 1-9.
        for num in range(1, 10):
            if self.puzzleValid(row, col, num):
                # If the number is valid, increment current path by 1.
                self.currentPathLength += 1
                self.puzzle[row][col] = num
                self.solve(index + 1)

        # No number found...set back to 0 and return to the previous blank
        self.pathLengths.append(self.currentPathLength)  # Add the current path length to the overall list.
        self.currentPathLength -= 1  # -1 from path.
        index -= 1
        self.puzzle[row][col] = 0

    #######################################################
    # CSP VALIDATORS                                      #
    #######################################################
    """
    Check if the current puzzle is legal after placing num in (row, col).
    """

    def puzzleValid(self, row, col, num):
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

    """
    Check if num is a legal value for the given row.
    """

    def checkRow(self, row, num):
        for col in range(9):
            currentValue = self.puzzle[row][col]
            if num == currentValue:
                return False
        return True

    """
    Check if num is a legal value for the given column.
    """

    def checkColumn(self, col, num):
        for row in range(9):
            currentValue = self.puzzle[row][col]
            if num == currentValue:
                return False
        return True

    """
    Check if num is a legal value for the box (one of 9 boxes) containing given row/col
    """

    def checkBox(self, row, col, num):
        row = (row / 3) * 3
        col = (col / 3) * 3

        for r in range(3):
            for c in range(3):
                if self.puzzle[row + r][col + c] == num:
                    return False
        return True

    #######################################################
    # ALGORITHM HELPERS                                   #
    #######################################################
    """
    Generic method to end the algorithm in process,
    calculate the running time, output the solution file,
    print the metrics and exit.
    """

    def endAlgorithm(self):
        self.pathLengths.append(self.currentPathLength)  # Append the final path's length
        self.outputSolution()
        sys.exit(0)

    """
    Get all the empty cells in the puzzle.
    """
    def getEmptyCells(self, puzzle):
        emptyCells = []
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    emptyCells.append((i, j))
        return emptyCells

    #######################################################
    # I/O HELPERS                                         #
    #######################################################
    """
    Constructs the blank puzzle array to have 0 0 0 0 0...for all rows and columns
    """

    def initPuzzleArray(self):
        del self.puzzle[:]
        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append([])
                self.puzzle[i][j] = 0

    """
    Loads a puzzle file into the program and makes sure that
    it is valid.
    """

    def loadPuzzle(self, inputstr):  # puzzleFile
        possibleTokens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        puzzleText = inputstr.split("\n")
        for row in range(9):
            lineTokens = puzzleText[row + 1].split()  # take care because row+1, before was row
            # print lineTokens
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
        print ""

    """
    Write the solution to a string
    """

    def outputSolution(self):
        for i in range(9):
            rowString = ""
            for j in range(9):
                rowString += str(self.puzzle[i][j]) + " "
                # print rowString
        return rowString
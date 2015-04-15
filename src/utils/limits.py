# limits.py
# author: Daniel Jauergui
# date: 3-31-2015

class Limits(object):
    def axis_missing(self, board, x, axis):
        """Verify the missing axis using the board

        Keyword arguments:
        board -- Array e.g.: [[None, 8,..., 1, None]]
        x -- position in axis X
        axis -- axis of board in current context.
        return  -- return a figure bits
        """
        bits = 0
        for y in xrange(9):
            current_value = board[self.set_position_for(x, y, axis)]
            if current_value is not None:
                bits |= 1 << current_value
        return 511 ^ bits

    def set_position_for(self, x, y, axis=0):
        """Determine of position in sudoku for current arguments.

        Keyword arguments:
        x -- position in axis X
        y -- position in axis y
        axis -- axis of board in current context.
        return  -- a position in array that contain all values e.g: Row:2 Column: 3, it will return 12
        """
        if axis == 0:
            return x * 9 + y
        elif axis == 1:
            return y * 9 + x
        else:
            return (0, 3, 6, 27, 30, 33, 54, 57, 60)[x] + (0, 1, 2, 9, 10, 11, 18, 19, 20)[y]

    def list_bits(self, bits):
        """Determine when bits is allowed or needed returning and array with possible values of solution

        Keyword arguments:
        bits -- Get a figure bits
        return  -- Return an Array of numbers candidate of solution e.g.: [1, 2, 3, 4, 5, 7, 8, 9]
        """
        return [value for value in xrange(9) if 0 != bits & 1 << value]

    def calculate_bits(self, board):
        """Get a board that require verify if a position is allowed according with
         sudoku rules

        Keyword arguments:
        board -- Array e.g.: [[None, None,..., 1, None]]
        return  -- Two arrays "Allowed" and "Needed" with figure bits value
        """
        allowed, needed = [e is None and 511 or 0 for e in board], []
        for axis in xrange(3):
            for x in xrange(9):
                bits = self.axis_missing(board, x, axis)
                needed.append(bits)
                for y in xrange(9):
                    allowed[self.set_position_for(x, y, axis)] &= bits
        return allowed, needed
# make_sudoku.py
# author: David Bau
# Copyright (c) 2006 David Bau.  All rights reserved.
# URL: http://davidbau.com/downloads/sudoku.py
# Modified by Daniel Jauregui for study purposes

import random


class Game(object):

    def __init__(self, level):
        self.level = level

    def generate_game(self):
        """Call to make_puzzle with a empty board to generate game
        with level defined and it will return a array e.g.:
        Array: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        Where the position are from 0 to 80

        return -- Array e.g.: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        """
        return self.make_puzzle(self.get_solution([None] * 81))

    def make_puzzle(self, board):
        """Get the solved board and remove the range of values
         defined for level, the random position values will be
         replaced for None.

        Keyword arguments:
        board -- Array with all values solved for sudoku.
        return -- Array e.g.: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        """
        """ Implement random according level defined """
        puzzle = []
        # Deduced will use basic board for iteration conditional and fill it for each value found
        deduced = [None] * 81
        order = random.sample(xrange(81), 81)
        print order
        for position in order:
            if deduced[position] is None:
                puzzle.append((position, board[position]))
                deduced[position] = board[position]
                self.deduce(deduced)
        board = self.board_for_entries(puzzle)
        for position in xrange(81):
            if board[position] is None:
                board[position] = 0
            else:
                board[position] += 1

        return board

    def board_for_entries(self, entries):
        """Get array with tuples of position and value.
        This method will return an array with final array
        with values (Numbers and None).

        Keyword arguments:
        entries -- Array of tuples e.g.: [(23, 5), (80, 9),..., (2, 5), (15, 1)]
        return  -- Array e.g.: [4, 9, 3, None, 5, ...., 8, 8, None, None, 1]
        """
        board = [None] * 81
        for position, number in entries:
            board[position] = number
        return board

    def get_solution(self, board):
        """Get an empty array with 81 positions and call
        solve_board method to get a solved sudoku.

        Keyword arguments:
        board -- Array e.g.: [None, None,..., None, None]
        return  -- Array e.g.: [4, 9, 3, 4, 5, ...., 8, 7, 4, 8, 1]
        """
        return self.solve_board(board)[1]

    def solve_board(self, original):
        """Get an empty array (it can be resolve the puzzle)
        and create an arrays of board in order to get an unique solution

        Keyword arguments:
        original -- Array of Arrays e.g.: [[None, None,..., None, None]]
        return  -- Array e.g.: [4, 9, 3, 4, 5, ...., 8, 7, 4, 8, 1]
        """
        board = list(original)
        guesses = self.deduce(board)
        if guesses is None:
            return [], board
        track = [(guesses, 0, board)]
        return self.solve_next(track)

    def solve_next(self, remembered):
        """Get a board and guesses required if game is empty,
        it will create all game until a board does not contains None values

        Keyword arguments:
        remembered -- Contain all boards guesses, it is an Array e.g.: [[None, None,..., None, None]]
        return  -- Array e.g.: [4, 9, 3, 4, 5, ...., 8, 7, 4, 8, 1]
        """
        while len(remembered) > 0:
            guesses, count, board = remembered.pop()
            if count >= len(guesses):
                continue
            remembered.append((guesses, count + 1, board))
            workspace = list(board)
            pos, n = guesses[count]
            workspace[pos] = n
            guesses = self.deduce(workspace)
            if guesses is None:
                return (remembered, workspace)
            remembered.append((guesses, 0, workspace))
        return [], None

    def deduce(self, board):
        """Get a board that require to deduce the value following the
         sudoku rules

        Keyword arguments:
        board -- Array e.g.: [[None, None,..., None, None]]
        return  -- Array of tuples [(Position, Value)], the number of array items depends of number gasses found
        """
        while True:
            stuck, guess, count = True, None, 0
            # fill in any spots determined by direct conflicts
            allowed, needed = self.calculate_bits(board)
            board, allowed, stuck, guess, count = self.move_on_board(board, allowed, stuck, guess, count)
            if not stuck:
                allowed, needed = self.calculate_bits(board)
            # fill in any spots determined by elimination of other locations
            board, stuck, guess, count = self.move_on_board_for_axis(needed ,allowed ,board,guess, count, stuck)
            if stuck:
                return self.get_is_stuck(guess)

    def get_is_stuck(self, guess):
        """Ask about guess value

        Keyword arguments:
        guess -- inherited from deduce function
        return  -- return an integer from 1 to 9
        """
        if guess is not None:
            random.shuffle(guess)
        return guess

    def move_on_board_for_axis(self,needed ,allowed ,board,guess, count, stuck):
        """Move on board for each axis and guess needed and allowed values

        Keyword arguments:
        needed -- Array of numbers needed to resolve puzzle
        allowed -- Array of numbers allowed to resolve puzzle
        board -- inherited from deduce function
        guess -- Array of random numbers from 1 to 9
        count -- Count how many times pick the best option of guesses
        stuck -- Verify if game stuck returning true or false
        return  -- Tuple of (board, stuck, guess, count)
        """
        for axis in xrange(3):
            board, stuck, guess, count = self.move_on_x_position(needed, allowed, board, guess, count, axis, stuck)
        return board, stuck, guess, count

    def move_on_x_position(self,needed ,allowed ,board, guess, count, axis, stuck):
        """Move on axis position for each axis x  and guess needed and allowed values

        Keyword arguments:
        needed -- inherited from move_on_board_for_axis function
        allowed -- inherited from move_on_board_for_axis function
        board -- inherited from move_on_board_for_axis function
        guess -- inherited from move_on_board_for_axis function
        count -- inherited from move_on_board_for_axis function
        axis -- inherited from move_on_board_for_axis function
        stuck -- inherited from move_on_board_for_axis function
        return  -- Tuple of (board, stuck, guess, count)
        """
        for x in xrange(9):
            numbers = self.list_bits(needed[axis * 9 + x])
            zero,board,stuck,guess,count =  self.move_for_each_numbers(allowed ,board, guess, count, axis, x, numbers, stuck)
            if zero == 0:
                return []
        return board,stuck,guess,count

    def move_for_each_numbers(self, allowed ,board, guess, count, axis,x, numbers, stuck):
        """Move on axis position for each axis x  and guess needed and allowed values

        Keyword arguments:
        needed -- inherited from move_on_x_position function
        allowed -- inherited from move_on_x_position function
        board -- inherited from move_on_x_position function
        guess -- inherited from move_on_x_position function
        count -- inherited from move_on_x_position function
        x  -- inherited from move_on_x_position function
        axis -- inherited from move_on_x_position function
        stuck -- inherited from move_on_x_position function
        return  -- Tuple of (spots_empty,board,stuck,guess,count) where spots_empty is a flag
        """
        spots_empty = 1
        for number in numbers:
            bit = 1 << number
            spots = []
            spots = self.move_for_y_position(allowed, x, axis, bit, spots)
            if len(spots) == 0:
                spots_empty = 0
            elif len(spots) == 1:
                board[spots[0]] = number
                stuck = False
            elif stuck:
                guess, count = self.pick_better(guess, count, [(position, number) for position in spots])
        return spots_empty,board,stuck,guess,count

    def move_for_y_position(self,allowed, x, axis, bit, spots):
        """Move on axis position for each axis y  and guess allowed values

        Keyword arguments:
        allowed -- inherited from move_for_each_numbers function
        x  -- inherited from move_for_each_numbers function
        axis -- inherited from move_for_each_numbers function
        bit -- get a 0 or 1 for flag deduction
        spots -- It has a candidate numbers to be chosen
        return  -- a list os spots for allowed values
        """
        for y in xrange(9):
            position = self.set_position_for(x, y, axis)
            if allowed[position] & bit:
                spots.append(position)
        return spots

    def move_on_board(self, board, allowed, stuck, guess, count):
        """Move on board for each position from 1 to 81

        Keyword arguments:
        allowed -- Array of numbers allowed to resolve puzzle
        board -- inherited from deduce function
        guess -- Array of random numbers from 1 to 9
        count -- Count how many times pick the best option of guesses
        stuck -- Verify if game stuck returning true or false
        return  -- Tuple of (board, allowed, stuck, guess, count)
        """
        for position in xrange(81):
            result = self.verify_board(position, board, allowed, stuck, guess, count)
            if result[0] == 0:
                return []
            if result[0] == 1:
                board = result[1]
                stuck = result[2]
            if result[0] == 2:
                guess = result[1]
                count = result[2]
        return board, allowed, stuck, guess, count

    def verify_board(self, position, board, allowed, stuck, guess, count):
        """Move on board for each position from 1 to 81

        Keyword arguments:
        position -- inherited from move_on_board function
        allowed -- inherited from move_on_board function
        board -- inherited from move_on_board function
        guess -- inherited from move_on_board function
        count -- inherited from move_on_board function
        stuck -- inherited from move_on_board function
        return  -- Tuple of (zero, board, stuck, guess, count) where zero is a flag
        """
        zero = 1
        if None == board[position]:
            numbers = self.list_bits(allowed[position])
            if len(numbers) == 0:
                zero = 0
            elif len(numbers) == 1:
                board[position] = numbers[0]
                stuck = False
            elif stuck:
                guess, count = self.pick_better(guess, count, [(position, number) for number in numbers])
        return zero, board, stuck, guess, count

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

    def pick_better(self, guess, count, positions_in_spot):
        """Determine with of positions in spot is the best to solve puzzle.

        Keyword arguments:
        guess -- Array returned by figure_bits method
        count -- Count how many times position was guessed
        positions_in_spot -- Array of positions got from spots.
        return  -- It will return an array guess and count
        """
        if guess is None or len(positions_in_spot) < len(guess):
            return positions_in_spot, 1
        if len(positions_in_spot) > len(guess):
            return guess, count
        if random.randint(0, count) == 0:
            return positions_in_spot, count + 1
        else:
            return guess, count + 1
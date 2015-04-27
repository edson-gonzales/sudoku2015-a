# algorithm_solver.py
# author: Daniel Jauergui
# date: 4-23-2015


class AlgorithmSolver(object):

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def solve(self, board_object):
        """Get the board object and modify it from int array values to string array values, and vice versa
        when returns the board game with new values or the same values if it is stuck.

        Keyword arguments:
        board_object -- Object of Class Board
        return -- Board game with new values or the same values if it is stuck.
        """
        board = board_object.board
        board = [str(numeric_string) for numeric_string in board]
        result = self.algorithm.solve(board)
        if result is not None:
            board = [int(numeric_string) for numeric_string in result]
            print("\nAlgorithm solve this board!\n")
            board_object.print_board(board_object.resolved)
            raw_input("\n...(please press any key to continue)")
        else:
            print("\nAlgorithm cannot solve this board, please see below in solved game and compare: \n")
            board = [int(numeric_string) for numeric_string in board]
            board_object.print_board(board_object.resolved)
            raw_input("\n...(please press any key to continue)")
        return board
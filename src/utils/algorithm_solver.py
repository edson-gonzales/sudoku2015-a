# algorithm_solver.py
# author: Daniel Jauergui
# date: 4-23-2015


class AlgorithmSolver(object):

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def solve(self, board_object):
        board = board_object.board
        board = [str(numeric_string) for numeric_string in board]
        result = self.algorithm.solve(board)
        if result is not None:
            board = [int(numeric_string) for numeric_string in result]
        else:
            print("\nAlgorithm cannot solve this board, please see below in solved game and compare: \n")
            board = [int(numeric_string) for numeric_string in board]
            board_object.print_board(board_object.resolved)
            raw_input("\n...(please press any key to continue)")
        return board

    def print_result(self, board):
        self.algorithm.print_result(board)

    def change_algorithm(self, new_algorithm):
        self.algorithm = new_algorithm
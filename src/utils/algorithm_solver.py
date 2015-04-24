# algorithm_solver.py
# author: Daniel Jauergui
# date: 4-23-2015


class AlgorithmSolver(object):

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def solve(self, board):
        board = [str(numeric_string) for numeric_string in board]
        board = self.algorithm.solve(board)
        board = [int(numeric_string) for numeric_string in board]
        return board

    def print_result(self, board):
        self.algorithm.print_result(board)

    def change_algorithm(self, new_algorithm):
        self.algorithm = new_algorithm
# backtracking_solver_test.py

import unittest

from Backtracking_solver import BacktrackingSolver


class BackTrackingSolverTest(unittest.TestCase):
 
    game1 = """
- - 6 2 - 1 - - -
8 - - - - - - 7 1
- - 1 7 - - - 3 2
- - 7 - 3 - - 4 -
- 5 - - - - - 8 -
- 8 - - 4 - 7 - -
4 6 - - - 5 8 - -
1 7 - - - - - - 4
- - - 4 - 6 5 - -"""

    game1_solution = """7 3 6 2 9 1 4 5 8
8 4 2 6 5 3 9 7 1
5 9 1 7 8 4 6 3 2
9 1 7 5 3 8 2 4 6
2 5 4 9 6 7 1 8 3
6 8 3 1 4 2 7 9 5
4 6 9 3 1 5 8 2 7
1 7 5 8 2 9 3 6 4
3 2 8 4 7 6 5 1 9
"""

    game2 = """
9 0 0   0 0 0   9 0 7 
0 0 0   4 2 0   1 8 0
0 0 0   7 0 5   0 2 6
1 0 0   9 0 4   0 0 0
0 5 0   0 0 0   0 4 0
0 0 0   5 0 7   0 0 9
9 2 0   1 0 8   0 0 0
0 3 4   0 5 9   0 0 0
5 0 7   0 0 0   0 0 0"""

    def test_backtracking_algorithm_can_solve_sudoku_game1(self):
        print "my testing"
        Backtracking_Solver = BacktrackingSolver()
        print "my testing"
        Backtracking_Solver.loadPuzzle(self.game1)
        print "my testing"
        # Backtracking_Solver.solve()
        print "my testing"
        self.assertEquals(self.game1_solution, Backtracking_Solver.solve())

        
"""   def test_backtracking_return_false_if_game2_cannot_be_solved(self):
        Backtracking_Solver = BacktrackingSolver()
        Backtracking_Solver.load_puzzle(self.game2)
        self.assertFalse(Backtracking_Solver.solve())
"""
if __name__ == '__main__':
    unittest.main()
# norvig_solver_test.py
# author: Josue Mendoza
# date: 4-12-2015

import unittest
import os

from Fallin_solver import FallinSolver


class FallingSolverTest(unittest.TestCase):
 
    game1 = """
0 6 0   1 0 4   0 5 0
0 0 8   3 0 5   6 0 0
2 0 0   0 0 0   0 0 1

8 0 0   4 0 7   0 0 6
0 0 6   0 0 0   3 0 0
7 0 0   9 0 1   0 0 4

5 0 0   0 0 0   0 0 2
0 0 7   2 0 6   9 0 0
0 4 0   5 0 8   0 7 0"""

    game1_solution = """9 6 3   1 7 4   2 5 8   
1 7 8   3 2 5   6 4 9   
2 5 4   6 8 9   7 3 1   

8 2 1   4 3 7   5 9 6   
4 9 6   8 5 2   3 1 7   
7 3 5   9 6 1   8 2 4   

5 8 9   7 1 3   4 6 2   
3 1 7   2 4 6   9 8 5   
6 4 2   5 9 8   1 7 3   

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
    

    def test_fallin_algorithm_can_solve_sudoku_game1(self):
        Fallin_Solver = FallinSolver()
        Fallin_Solver.load_string(self.game1)
        Fallin_Solver.solve()      
        self.assertEquals(self.game1_solution, Fallin_Solver.dump_string())
        
    def test_fallin_return_false_if_game2_cannot_be_solved(self):
        Fallin_Solver = FallinSolver()
        Fallin_Solver.load_string(self.game2)        
        self.assertFalse(Fallin_Solver.solve())
    
if __name__ == '__main__':
    unittest.main()
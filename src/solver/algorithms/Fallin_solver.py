# Fallin_solver.py
# author: Lenny Flores
# date: 4-24-2015

class FallinSolver(object):
    """Initialize cells and count matrices"""
    def __init__(self):    
        self.cells = []
        self.count = []
        for i in range(9):
            self.cells += [ [] ]
            self.count += [ [] ]
            for j in range(9):
                self.cells[i] += [0]
                self.count[i] += [0]
        self.known = 0
    
    def copy(self):
        """Makes a copy of the sudoku data
        Instantiate the FallingSolver class and then, makes a copy of game at the current state and assign them to
        the attributes of class, then return the array of numbers that represent the game solved at the current state
        """
        copy = FallinSolver()
        for i in range(9):
            for j in range(9):
                copy.cells[i][j] = self.cells[i][j]
                copy.count[i][j] = self.count[i][j]
                copy.known = self.known
        return copy

    def load(self, data):
        """Loads from external data
        Data is a simple array of array of matrix of numbers that represent the sudoku game pending to solve"""
        self.known = 0
        for i in range(9):
            for j in range(9):
                self.compare_cell(i, j, data)
                
    def dump(self):
        """Dumps to external data (ie, a simple matrix/array-of-arrays)
        dump returns the sudoku game solution on a matrix output type
        """
        out = []
        for i in range(9):
            out += [ [] ]
            for j in range(9):
                self.out_cell(i, j, out)        
        return out
        
    def load_string(self, str):
        """Transform string to a set of row and lines, without the spaces and line breaks str, receive the sudoku game as an string with format and then values 
        are stored in lines and rows lists respectively
        """
        block_of_nine = str.split("\n");
        lines = []
        self.verify_block_of_nine(block_of_nine, lines)        
    
    def verify_block_of_nine(self, block_of_nine, lines):
        """verify in a block of nine"""
        for line in block_of_nine:
            line = line.strip()            
            if(line == ''):
                continue
            row = []            
            block_of_three = line.split()
            self.verify_block_of_three(block_of_three, line, row)          
            lines += [row]
        self.load(lines)
    
    def verify_block_of_three(self, block_of_three, line, row):
        """Verify in a block of three"""
        for field in block_of_three:
            field = field.strip()
            if(field == ''):
                continue
            element = int(field)
            row += [element]

    def dump_string(self):
        """Release the solution on an string format
        receive the dump results in a simple array and transform the array of sultion in a string with format i.e: spaces and line breaks""" 
        out = self.dump()
        out_str = ""
        for i in range(9):
            for j in range(9):
                out_str += str(out[i][j]) + " "
                out_str=self.concat_spaces(j, out_str)        
            out_str += "\n"
            if(i % 3 == 2): 
                out_str += "\n"
        return out_str
        
    def concat_spaces(self, j, out_str):
        """Concatenate spaces"""
        if(j % 3 == 2): 
            out_str += "  "
        return out_str
    
    def check_row(self, i, possible):
        """Check row""" 
        for n in range(9):
          self.verify_key(i, n, possible)
        
    def reduce(self):
        """finds possible elements for each position"""
        self.known = 0        
        for i in range(9):
            self.check_has_solution(i) 
        """ done: successful (ie, no impossible entries)"""
        return 1

    def check_has_solution(self, i):
        """Continue the verification if apply of the next possible solution for the game and store it on known value"""
        for j in range(9):
            """One possible: increase number of knowns"""
            if(self.count[i][j] == 1):
                self.known = self.known + 1
                continue
            possible = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}        
            self.check_row(i, possible)              
            self.check_column(j, possible)              
            self.check_inner(i, j, possible)                         
            self.count[i][j] = len(possible.keys())                       
            self.has_no_solution(i, j)
            if(self.count[i][j] == 1):
              self.known = self.known + 1                      
            self.cells[i][j] = possible

    def has_no_solution(self, i, j):
        """Verify if sudoku game has none possible: no solutions"""
        if(self.count[i][j] == 0):
            return 0
    

    def check_column(self, j, possible):
        """check column"""
        for n in range(9):
            self.verify_key(n, j, possible)            

    def verify_key(self, n, j, possible):
        """Verify key of block """ 
        if(self.count[n][j] == 1):
            x = self.cells[n][j].keys()[0]
            if(possible.has_key(x)):
                del possible[x]
    
    def check_inner(self, i, j, possible):
        """Check inner box"""
        box_i = i - (i % 3)
        box_j = j - (j % 3)
        for a in range(box_i, box_i+3):
            for b in range(box_j, box_j+3):
                self.verify_key(a, b, possible)                
            
    def compare_cell(self, i, j, data):
        """Compare cell"""
        if(data[i][j] != 0):
            self.cells[i][j] = { data[i][j]: 1 }
            self.count[i][j] = 1
            self.known = self.known + 1
        else:
            self.cells[i][j] = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
            self.count[i][j] = 9
    
    def out_cell(self, i, j, out):
        """auxiliar copy the sudoku game solution and store it on out auxiliar list"""
        if(self.count[i][j] == 1):
            out[i] += [self.cells[i][j].keys()[0]]
        else:
            out[i] += [0]
    
    def solve(self, start = 0):      
        """reduce as many times as necessary until we get no new known cells"""
        while 1:
            current_known = self.known
            if(self.reduce() == 0):
                return 0
            if self.known == current_known:
                break
        """all numbers known: done"""
        if(self.known == 9 * 9):
            return 1
        """find the first cell with more than one possibility"""       
        x = -1
        y = -1
        flag = 0
        b = start % 9
        a = (start - b) / 9
        for i in range(a, 9):
            if(i > a): 
                b = 0            
            (x, y, flag)=self.set_flag(b, i)             
            if flag == 1:
              break          
        """not all numbers known, yet nothing with a possibility count > 1 ? shouldn't happen"""
        if(x == -1 or y == -1):
            return 0        
        possible = self.cells[x][y]
        self.try_possibilites(possible, x, y)        
        return 0

    def set_flag(self, b, i, x=-1, y=-1, flag=0):        
        for j in range(b, 9):                                       
            if(self.count[i][j] > 1):
                x = i
                y = j
                flag = 1
                break
        return (x, y, flag)

    def try_possibilites(self, possible, x, y):
        """try the possibilities, the recursive s.solve() call will take care of updating s.known"""                
        for p in possible.keys():
            s = self.copy()            
            s.cells[x][y] = { p: 1 }
            s.count[x][y] = 1
            if(s.solve((x * 9 + y) + 1)):
                self.cells = s.cells
                self.count = s.count
                self.known = s.known
                return 1                

            
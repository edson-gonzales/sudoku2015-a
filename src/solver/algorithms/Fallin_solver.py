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
        return a matrix with data of current game as a simple array-of-arrays
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
        Data -- array of string that will be send to compare_cell method for verification"""
        self.known = 0
        for i in range(9):
            for j in range(9):
                self.compare_cell(i, j, data)
                
    def dump(self):
        """Dumps to external data (ie, a simple matrix/array-of-arrays output type)        
        Return the matrix with game at that state after verification on out cell method
        """
        out = []
        for i in range(9):
            out += [ [] ]
            for j in range(9):
                self.out_cell(i, j, out)        
        return out
        
    def load_string(self, str):
        """Transform string to a set of row and lines, without format -spaces,line breaks 
        str -- string that represent sudoku game with format line breaks, spaces
        """
        block_of_nine = str.split("\n");
        lines = []
        self.verify_block_of_nine(block_of_nine, lines)        
    
    def verify_block_of_nine(self, block_of_nine, lines):
        """verify in a block of nine
        block_of_nine -- Represents the split part of sudoku game in a list of nine elements i.e.: 123 456 789
        """
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
        """Verify in a block of three
        block_of_three -- Represent the split part of sudoku game in a list three elements e.g.: 123
        """
        for field in block_of_three:
            field = field.strip()
            if(field == ''):
                continue
            element = int(field)
            row += [element]

    def dump_string(self):
        """Release the solution on an string format
        returns the game solution in an string variable with format, including spaces, line breaks""" 
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
        """Concatenate spaces
        out_str -- List of elements of sudoku game that was concatenated with spaces
        Returns the string with an space concatenated if there are more than three elements count
        """
        if(j % 3 == 2): 
            out_str += "  "
        return out_str
    
    def check_row(self, i, possible):
        """Check row
        i -- iterator sent from check_has_solution
        possible -- array of array that represent game at any point on solve process
        """ 
        for n in range(9):
          self.verify_key(i, n, possible)
        
    def reduce(self):
        """finds possible elements for each position
        return 1 that means that game has a possible solution to continue iterating)
        """
        self.known = 0        
        for i in range(9):
            self.check_has_solution(i) 
        return 1

    def check_has_solution(self, i):
        """Continue the verification if apply of the next possible solution for the game
        i -- Iterator for row in array
        """
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
        """Verify if sudoku game has none no solutions
        i --Iterator for row in array
        j -- Iterator for column in array
        Returns 0 that means no possible solutions were found for the game
        """
        if(self.count[i][j] == 0):
            return 0
    

    def check_column(self, j, possible):
        """Verify column
        j -- iterator of row
        possible -- array of string of game at any state of solution
        """
        for n in range(9):
            self.verify_key(n, j, possible)            

    def verify_key(self, n, j, possible):
        """Verify key of block 
        n -- iterator for row
        j -- iterator for column
        possible -- array with the possible values for game solution
        """ 
        if(self.count[n][j] == 1):
            x = self.cells[n][j].keys()[0]
            if(possible.has_key(x)):
                del possible[x]
    
    def check_inner(self, i, j, possible):
        """Check inner box
        i -- iterator for row
        j -- iterator for column
        possible -- array with the possible values for game solution
        """
        box_i = i - (i % 3)
        box_j = j - (j % 3)
        for a in range(box_i, box_i+3):
            for b in range(box_j, box_j+3):
                self.verify_key(a, b, possible)                
            
    def compare_cell(self, i, j, data):
        """Compare cell
        i -- iterator for row
        j -- iterator for column
        data -- array of strings with the possible values for game solution
        """
        if(data[i][j] != 0):
            self.cells[i][j] = { data[i][j]: 1 }
            self.count[i][j] = 1
            self.known = self.known + 1
        else:
            self.cells[i][j] = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
            self.count[i][j] = 9
    
    def out_cell(self, i, j, out):
        """auxiliar copy the sudoku game solution and store it on out auxiliar list
        i -- iterator for row
        j -- iterator for column
        out -- list concatenated with the possible values
        """
        if(self.count[i][j] == 1):
            out[i] += [self.cells[i][j].keys()[0]]
        else:
            out[i] += [0]
    
    def solve(self, start = 0):      
        """reduce as many times as necessary until we get no new known cells
        start -- by default 0 the begin the iterator to verify known value
        returns 1/0 when game has or not a possible solution
        """
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
        """
        b -- row possition to verify if value has a possible solution
        i -- Iterator of row
        x -- parameter to assign the new possition of column
        y -- parameter to assign the new possition of row
        flag -- mark if the current element has a solution

        Returns x,y,flag for the current possition and verification to the next iteration level
        """
        for j in range(b, 9):                                       
            if(self.count[i][j] > 1):
                x = i
                y = j
                flag = 1
                break
        return (x, y, flag)

    def try_possibilites(self, possible, x, y):
        """try the possibilities, the recursive s.solve() call will take care of updating s.known
        possible --
        x -- Iterator of column
        y -- Iterator of row
        Returns 1 means that there is a successfull verification on element about possible solution
        """
        for p in possible.keys():
            s = self.copy()            
            s.cells[x][y] = { p: 1 }
            s.count[x][y] = 1
            if(s.solve((x * 9 + y) + 1)):
                self.cells = s.cells
                self.count = s.count
                self.known = s.known
                return 1
# Fallin_solver.py
# author: Lenny Flores
# date: 4-24-2015

class FallinSolver(object):
    """Initialize cells and count matrices"""
    def __init__(self):    
        self.cells = []
        self.count = []
        for column_index in range(9):
            self.cells += [ [] ]
            self.count += [ [] ]
            for row_index in range(9):
                self.cells[column_index] += [0]
                self.count[column_index] += [0]
        self.known = 0
    
    def copy(self):
        """Makes col copy of the sudoku data
        return col matrix with data of current game as col simple array-of-arrays
        """
        copy = FallinSolver()
        for column_index in range(9):
            for row_index in range(9):
                copy.cells[column_index][row_index] = self.cells[column_index][row_index]
                copy.count[column_index][row_index] = self.count[column_index][row_index]
                copy.known = self.known
        return copy

    def load(self, data):
        """Loads from external data
        Data -- array of string that will be send to compare_cell method for verification"""
        self.known = 0
        for column_index in range(9):
            for row_index in range(9):
                self.compare_cell(column_index, row_index, data)
                
    def dump(self):
        """Dumps to external data (ie, col simple matrix/array-of-arrays output type)        
        Return the matrix with game at that state after verification on out cell method
        """
        out = []
        for column_index in range(9):
            out += [ [] ]
            for row_index in range(9):
                self.out_cell(column_index, row_index, out)        
        return out
        
    def load_string(self, str):
        """Transform string to col set of row and lines, without format -spaces,line breaks 
        str -- string that represent sudoku game with format line breaks, spaces
        """
        block_of_nine = str.split("\n");
        lines = []
        self.verify_block_of_nine(block_of_nine, lines)        
    
    def verify_block_of_nine(self, block_of_nine, lines):
        """verify in col block of nine
        block_of_nine -- Represents the split part of sudoku game in col list of nine elements column_index.e.: 123 456 789
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
        """Verify in col block of three
        block_of_three -- Represent the split part of sudoku game in col list three elements e.g.: 123
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
        for column_index in range(9):
            for row_index in range(9):
                out_str += str(out[column_index][row_index]) + " "
                out_str=self.concat_spaces(row_index, out_str)        
            out_str += "\n"
            if(column_index % 3 == 2): 
                out_str += "\n"
        return out_str
        
    def concat_spaces(self, row_index, out_str):
        """Concatenate spaces
        out_str -- List of elements of sudoku game that was concatenated with spaces
        Returns the string with an space concatenated if there are more than three elements count
        """
        if(row_index % 3 == 2): 
            out_str += "  "
        return out_str
    
    def check_row(self, column_index, possible):
        """Check row
        column_index -- iterator sent from check_has_solution
        possible -- array of array that represent game at any point on solve process
        """ 
        for row in range(9):
          self.verify_key(column_index, row, possible)
        
    def reduce(self):
        """finds possible elements for each position
        return 1 that means that game has col possible solution to continue iterating)
        """
        self.known = 0        
        for column_index in range(9):
            self.check_has_solution(column_index) 
        return 1

    def check_has_solution(self, column_index):
        """Continue the verification if apply of the next possible solution for the game
        column_index -- Iterator for row in array
        """
        for row_index in range(9):
            """One possible: increase number of knowns"""
            if(self.count[column_index][row_index] == 1):
                self.known = self.known + 1
                continue
            possible = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}        
            self.check_row(column_index, possible)              
            self.check_column(row_index, possible)              
            self.check_inner(column_index, row_index, possible)                         
            self.count[column_index][row_index] = len(possible.keys())                       
            self.has_no_solution(column_index, row_index)
            if(self.count[column_index][row_index] == 1):
              self.known = self.known + 1                      
            self.cells[column_index][row_index] = possible

    def has_no_solution(self, column_index, row_index):
        """Verify if sudoku game has none no solutions
        column_index --Iterator for row in array
        row_index -- Iterator for column in array
        Returns 0 that means no possible solutions were found for the game
        """
        if(self.count[column_index][row_index] == 0):
            return 0
    

    def check_column(self, row_index, possible):
        """Verify column
        row_index -- iterator of row
        possible -- array of string of game at any state of solution
        """
        for col in range(9):
            self.verify_key(col, row_index, possible)            

    def verify_key(self, col, row_index, possible):
        """Verify key of block 
        n -- iterator for row
        row_index -- iterator for column
        possible -- array with the possible values for game solution
        """ 
        if(self.count[col][row_index] == 1):
            x = self.cells[col][row_index].keys()[0]
            if(possible.has_key(x)):
                del possible[x]
    
    def check_inner(self, column_index, row_index, possible):
        """Check inner box
        column_index -- iterator for row
        row_index -- iterator for column
        possible -- array with the possible values for game solution
        """
        box_i = column_index - (column_index % 3)
        box_j = row_index - (row_index % 3)
        for col in range(box_i, box_i+3):
            for row in range(box_j, box_j+3):
                self.verify_key(col, row, possible)                
            
    def compare_cell(self, column_index, row_index, data):
        """Compare cell
        column_index -- iterator for row
        row_index -- iterator for column
        data -- array of strings with the possible values for game solution
        """
        if(data[column_index][row_index] != 0):
            self.cells[column_index][row_index] = { data[column_index][row_index]: 1 }
            self.count[column_index][row_index] = 1
            self.known = self.known + 1
        else:
            self.cells[column_index][row_index] = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
            self.count[column_index][row_index] = 9
    
    def out_cell(self, column_index, row_index, out):
        """auxiliar copy the sudoku game solution and store it on out auxiliar list
        column_index -- iterator for row
        row_index -- iterator for column
        out -- list concatenated with the possible values
        """
        if(self.count[column_index][row_index] == 1):
            out[column_index] += [self.cells[column_index][row_index].keys()[0]]
        else:
            out[column_index] += [0]
    
    def solve(self, start = 0):      
        """reduce as many times as necessary until we get no new known cells
        start -- by default 0 the begin the iterator to verify known value
        returns 1/0 when game has or not col possible solution
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
        row = start % 9
        col = (start - row) / 9
        for column_index in range(col, 9):
            if(column_index > col): 
                row = 0            
            (x, y, flag)=self.set_flag(row, column_index)             
            if flag == 1:
              break          
        """not all numbers known, yet nothing with col possibility count > 1 ? shouldn't happen"""
        if(x == -1 or y == -1):
            return 0        
        possible = self.cells[x][y]
        self.try_possibilites(possible, x, y)        
        return 0

    def set_flag(self, row, column_index, x=-1, y=-1, flag=0):        
        """
        row -- row possition to verify if value has col possible solution
        column_index -- Iterator of row
        x -- parameter to assign the new possition of column
        y -- parameter to assign the new possition of row
        flag -- mark if the current element has col solution

        Returns x,y,flag for the current possition and verification to the next iteration level
        """
        for row_index in range(row, 9):                                       
            if(self.count[column_index][row_index] > 1):
                x = column_index
                y = row_index
                flag = 1
                break
        return (x, y, flag)

    def try_possibilites(self, possible, x, y):
        """try the possibilities, the recursive s.solve() call will take care of updating s.known
        possible --
        x -- Iterator of column
        y -- Iterator of row
        Returns 1 means that there is col successfull verification on element about possible solution
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
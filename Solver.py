import math
import sys
from gmpy import is_square

class Sudoku:

    def __init__(self, input_file):

        self.parseFile(input_file)#initializes self.grid and self.size

    def parseFile(self, input_file):#parses a text file for its Sudoku grid
        '''
        files will be saved in the the following format:
            1,2,3,4,5,6,7,8,9
            2,3,4,5,6,7,8,9,1
            ...
            9,8,7,6,4,5,3,1,2
        '''
        try:
            with open(input_file,"r") as f:
                self.grid = f.read().split("\n")
                if self.grid[-1] == "":
                    self.grid.pop(-1)
                self.size = len(self.grid)
                if not is_square(self.size):
                    sys.exit("Invalid input file length")
                for i in range(self.size):
                    self.grid[i] = self.grid[i].split(",")
                    if len(self.grid[i]) != self.size:
                        sys.exit("Input file is formatted incorrectly")
                    for j in range(self.size):
                        try:
                            self.grid[i][j] = [int(self.grid[i][j])]
                        except ValueError:
                            if self.grid[i][j] == "-"
                                self.grid[i][j] = [i for i in range(1,self.size+1)]
                            else:
                                sys.exit("Input file is formatted incorrectly")
        except IOError:
            sys.exit("Input file does not exist")

    def solve(self):


board = Sudoku("source.txt")

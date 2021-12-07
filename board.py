# Name: Varun Golusupudi
# Instructor: Harikrishna Kuttivelli
# Course: CSE 20
# Purpose of the file: This is the board file for tic-tac-toe. It has the tic-tak-toe board and stores valid choices which the user can enter.

class Board:    # Defining Board class
    _count = 0  # A private class variable 
    def __init__(self):     # Defining the constructor method
        
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""
    def get_size(self,size):
          return self.size # optional, return the board size (an instance size)
    def get_winner(self):
        return self.winner # return the winner's sign O or X (an instance winner)     
    def set(self, cell, sign):
        self.sign=sign#self.sign is assigned the value of the user
        valid_choice=['A1','B1','C1','A2','B2','C2','A3','B3','C3']#list of valid choice to be chosen for checking
        index=valid_choice.index(cell)#index of the cell is taken on this line
        self.board[index]=sign#the sign is assigned to the index on the board
        return
        # mark the cell on the board with the sign X or O
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can use a tuple ("A1", "B1",...) or a dictionary to obtain indexes 
        # this implementation is up to you
    def isempty(self, cell):
        valid_choice=['A1','B1','C1','A2','B2','C2','A3','B3','C3'] # list of valid choice for checking the empty cell
        index=valid_choice.index(cell)  # index of the cell is taken on this line
        if self.board[index]!='X' and self.board[index]!='O':   # here they check if the cell is empty or not
            return True     # if the the cell is empty they return True
        else:
            return False    # if the cell is not empty they return false
        # return True if the cell is empty (not marked with X or O)
    def isdone(self):#here they check whether there is a win or tie
        if ((self.board[0]==self.board[1]==self.board[2]==self.sign and self.board[0]==self.board[1]==self.board[2]!=" ") or#winning condition for horizontal row 1
           (self.board[3]==self.board[4]==self.board[5]==self.sign and self.board[3]==self.board[4]==self.board[5]!=" ") or#winning condition for horizontal row 2
           (self.board[6]==self.board[7]==self.board[8]==self.sign and self.board[6]==self.board[7]==self.board[8]!=" ") or#winning condition for horizontal row 3
           (self.board[0]==self.board[3]==self.board[6]==self.sign and self.board[0]==self.board[3]==self.board[6]!=" ") or#winning condition for vertical column 1
           (self.board[1]==self.board[4]==self.board[7]==self.sign and self.board[1]==self.board[4]==self.board[7]!=" ") or#winning condition for vertical column 2
           (self.board[2]==self.board[5]==self.board[8]==self.sign and self.board[2]==self.board[5]==self.board[8]!=" ") or#winning condition for vertical column 3
           (self.board[0]==self.board[4]==self.board[8]==self.sign and self.board[0]==self.board[4]==self.board[8]!=" ") or#winning condition for Diagonal from left
           (self.board[2]==self.board[4]==self.board[6]==self.sign and self.board[2]==self.board[4]==self.board[6]!=" ")):#winning condition for Diagonal from right
            self.winner=self.sign   # winner is assigned the sign of the winner of game
            done=True   # flag
            return done   # returns the flag
        for k in range(0,9):    # for loop is travesed from all the index of the board
            if self.board[k]==" ":  # here if the cell is emmpty it breaks
                break
            elif k==8:  # the condition is checked if the cell is at 8 that is last cell of the board
                done=True   # flag
                return done  # returns the flag
        done = False    # this is the cindition used for when there is no winning condition
        return done  # returns the flag
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
    def show(self):
            # draw the board
            print('   A   B   C')   # this are the column naming
            print(' +---+---+---+') # this is for the design of the board
            print('1| {} | {} | {} |'.format(self.board[0],self.board[1],self.board[2]))    # the respective space is assigned a cell from the list using format function
            print(' +---+---+---+') # this is for the design of the board
            print('2| {} | {} | {} |'.format(self.board[3],self.board[4],self.board[5]))    # the respective space is assigned a cell from the list using format function
            print(' +---+---+---+')
            print('3| {} | {} | {} |'.format(self.board[6],self.board[7],self.board[8]))    # the respective space is assigned a cell from the list using format function
            print(' +---+---+---+') # this is for the design of the board

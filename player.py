# Name: Varun Golusupudi
# Instructor: Harikrishna Kuttivelli
# Course: CSE 20
# Purpose of the file: This is the player file for tic-tac-toe. It takes the inputs from the user by selecting the box on the board.

from random import choice     # Importing choice from random module
class Player:  # Defining Player class
      _counter = 0 # A private class variable 
      def __init__(self, name, sign, board = None):  # Defining the constructor method
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
            self.board = board
      def get_sign(self): 
          return self.sign
            # return an instance sign
      def set_sign(self, sign):
          self.sign = sign # sets the instance sign
      def get_name(self):
          return self.name
            # return an instance name
      def set_name(self, name):
          self.name = name # sets the instance name
      def choose(self, board):
            valid_choice=['A1','A2','A3','B1','B2','B3','C1','C2','C3']#list for valid choice for user
            while True:
                  dec=input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n")#input is taken from user
                  if dec in valid_choice:#value entered is checked in valid choice
                        if board.isempty(dec) == True:#checks if board is empty on that particular cell
                              board.set(dec,self.sign)#value is assigned to the cell
                              break#after assigning the value the loop is break
                        else:
                              print("You did not choose correctly.")#prompts if the cell is chosen wrongly
                  else:
                        print("You did not choose correctly.")#prompts if the cell is chosen wrongly
                  
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            return      
class AI(Player): #Creating a class AI and inheriting from Player class
      def __init__(self, name, sign, board = None):  # Defining the constructor method
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
            self.board = board
      def get_sign(self): 
          return self.sign
            # return an instance sign
      def set_sign(self, sign):
          self.sign = sign # sets the instance sign
      def get_name(self):
          return self.name
            # return an instance name
      def set_name(self, name):
          self.name = name # sets the instance name
      def choose(self,board): 
            valid_moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]#list for valid choice for AI
            while True:
                  cell = choice(valid_moves)#input is taken from random module from the list
                  if cell in valid_moves:#value entered is checked in valid moves
                        if board.isempty(cell) == True:#checks if board is empty on that particular cell
                              board.set(cell,self.sign)#value is assigned to the cell
                              break#after assigning the value the loop is break

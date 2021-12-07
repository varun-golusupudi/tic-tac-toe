# Name: Varun Golusupudi
# Instructor: Harikrishna Kuttivelli
# Course: CSE 20
# Purpose of the file: To implement the game of tic-tac-toe which has two options of playing with a friend and playing with AI.

from board import Board     # Importing Board class from board.py to the main file.
#from player import Player
from player import Player, AI       # Importing Player and AI classes from player.py to main file.

# main program  # Defining a main() function to run functions at once
def main():
    print("Welcome to TIC-TAC-TOE Game!")       # Printing a welcome message
    while True:                 # Infinite While loop which will break after the game ends.
        board = Board()     # Adding the Board class to a variable named board
        player1 = Player("Bob", "X")        # Name and Value of Player1
        #player1 = AI("Bob", "X", board)        # This line enables AI. You must commment the above line in order to use AI
        player2 = Player("Alice", "O")      # Name and Value of Player2
        turn = True
        while True:         # While Loop which will execute till the game ends.
            board.show()
            if turn:
                player1.choose(board)
                turn = False
            else:
                player2.choose(board)
                turn = True
            if board.isdone():
                break
        board.show()
        if board.get_winner() == player1.get_sign():        # if loop which checks if Player1 won
            print(f"{player1.get_name()} is a winner!")         # Printing Player1 won the game
        elif board.get_winner() == player2.get_sign():   # elif loop which checks if Player2 won
            print(f"{player2.get_name()} is a winner!")  # Printing Player2 won the game
        else:       # else block executes if it is a tie
            print("It is a tie!")   # Printing it is a tie
        ans = input("Would you like to play again? [Y/N] \n").upper()   # Asking the user to continue or exit the game.
        if (ans != "Y"):
            break
    print("Goodbye!")   # Exiting the program.


if __name__=="__main__":        # Executes the main() function
    main()

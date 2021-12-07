
# Two Player and computer Tic-Tac-Toe

A fun python program to play tic-tac-toe with your friend or a bot. This file will explain the code and guide you in running the program.

CONTENTS OF README FILE
---------------------
 * Class & File Documentation
   * tictac.py 
   * player.py
   * board.py
 * Demo Program Documentation


Class & File Documentation
---------------------
This section briefly explains each file and their classes.

* **tictac.py**- This is the main file and it has main() function. It imports player.py and board.py to run the game. It is a class for two player tic-tac-toe. This is also the demo program.
* **player.py**- This is the player file and it takes the inputs from the user by selecting the box on the board. It has two Classes: 
    * **Player class**- This class takes inputs from the users and checks with the list containing valid choices. This class has one constructor method and five methods and one private class variable. 
        * **get_sign()** method- This method is used to return the sign "O" or "X".
        * **set_sign()** method- This method is used to set the value to the instance variable, 'self.sign'.
        * **get_name()** method- This method is used to return the name of the player.
        * **set_name()** method- This method is used to set the name to the instance variable, 'self.name'.
        * **choose()** method- This method is used to ask the users for the input of the location on the board, and check the if the inputs are valid.
        * ***_counter*** private class variable- This variable was made for a formality as there is no need for a class variable in the code, and fulfills the requirements of the assignment.
    * **AI class**- This class has a bot which automatically randomly inputs a value on the board, It is a class for single player tic-tac-toe. This class has one constructor method and five methods.
        * **get_sign()** method- This method is used to return the sign "O" or "X".
        * **set_sign()** method- This method is used to set the value to the instance variable, 'self.sign'.
        * **get_name()** method- This method is used to return the name of the player.
        * **set_name()** method- This method is used to set the name to the instance variable, 'self.name'.
        * **choose()** method- This method is used to ask the user for the input of the location on the board, and check the if the input is valid.   
* **board.py**- This is the board file for tic-tac-toe. It has the tic-tak-toe board and stores valid choices which the user can enter. This file has one class:
    * **Board class**- This class is used for format the board and it's size. It contains the list of valid choices and  the checks for the winner and prints the sign "O" or "X" with the name. This class has six methods and one private class variable.
        *  **get_size**- This method is used to return the tic-tac-toe board size. 
        *  **get_winner**- This method is used to return the winner's sign "O" or "X".  
        *  **set()**- This method sets the sign for the instance variable, 'self.sign'.
        *  **isempty**- This method checks if the cell on the board is empty and prints an error if it's already full.
        *  **isdone**- This method check the winning conditions and exits the program after printing the name.
        *  **show**- This method used to format the tic-tac-toe board.
        * ***_count*** private class variable- This variable was made for a formality as there is no need for a class variable in the code, and fulfills the requirements of the assignment.

Demo Program Documentation
---------------------
tictac.py is the demo program file which executes the code.
* **Requirements**:-
    * The user should have tictac.py, player.py, and board.py installed on the system(laptop/desktop).
    * The user should have Python IDLE or python compiler installed with a python extension.
* **Instructions**:-
    * In order to play two player tic-tac toe, follow these steps:-
        * Make sure to the code from lines 15-17 are like the following:-
            ``` 
            player1 = Player("Bob", "X")        
            #player1 = AI("Bob", "X", board)       
            player2 = Player("Alice", "O")  

        * After that, run the code by clicking the run button on the compiler or F5 on Python IDLE.
        * Enter the valid inputs from the following: ['A1','B1','C1','A2','B2','C2','A3','B3','C3'].
        * The program will exit after the game is completed and you can type 'y' or 'Y' to play again or type 'n' or 'N' to exit the program.
    * In order to play with the computer, follow these steps:-
       * Make sure to the code from lines 15-17 are like the following:-
            ``` 
            #player1 = Player("Bob", "X")        
            player1 = AI("Bob", "X", board)       
            player2 = Player("Alice", "O")  

        * After that, run the code by clicking the run button on the compiler or F5 on Python IDLE.
        * Enter the valid inputs from the following: ['A1','B1','C1','A2','B2','C2','A3','B3','C3'].
        * The program will exit after the game is completed and you can type 'y' or 'Y' to play again or type 'n' or 'N' to exit the program.

* **Custom Player Name**- Follow these steps to put your own name:-
    * Make sure to the code from lines 15-17 are like the following:-
         ``` 
            player1 = Player("Custom_Name", "X")        
            #player1 = AI("Custom_Name", "X", board)       
            player2 = Player("Custom_Name", "O") 
        ``` 
    * You can put your custom name in the quotes, make sure your name is within the quotes.


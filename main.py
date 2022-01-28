# student name: Mayank Rastogi
# student number: 74196783
import random


class TicTacToe:
    def __init__(self):  # Use as is
        """ initializes data fields (board and played) 
            and prints the banner messages 
            and prints the initial board on the screen
        """
        self.board = [' '] * 9  # A list of 9 strings, one for each cell,
        # will contain ' ' or 'X' or 'O'
        # Set (of cell num) already played: to keep track of the played cells
        self.played = set()
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()

    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """
        print("")
        print(
            f"   {self.board[0]} | {self.board[1]} | {self.board[2]}    0 | 1 | 2")
        print("   --+---+--    --+---+--")
        print(
            f"   {self.board[3]} | {self.board[4]} | {self.board[5]}    3 | 4 | 5")
        print("   --+---+--    --+---+--")
        print(
            f"   {self.board[6]} | {self.board[7]} | {self.board[8]}    6 | 7 | 8")
        print("")

    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number; 
            error checks that the input is a valid cell number; 
            and prints the info and the updated self.board;
        """
        """ Conditions to check:
        1. If it's int
        2. If it's in the range 0-9
        3. If the move is already played
        """
        # Loop continues to accept values until valid cell number is added
        while True:
            try:
                player_move = int(
                    input("> Next move for X (state a valid cell num): "))
                if (player_move < 0 or player_move > 8):
                    print("Must enter a valid cell number")
                elif (self.board[player_move] != " "):
                    print("Must enter a valid cell number")
                else:
                    # Valid cell number is entered
                    print(f"You chose cell {player_move}")
                    # Adds an X at the position of cell number in board list
                    self.board[player_move] = 'X'
                    # Adds the player move to the set played
                    self.played.add(player_move)
                    self.printBoard()
                    break
            except ValueError:
                print("Must be an integer")

    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell, 
            and prints the info and the updated self.board 
        """
        # Loop continues to generate random number between 0 and 8 (inclusive) until empty cell is found
        while True:
            computer_move = random.randint(0, 8)
            # Checks if cell number is empty or not
            if (self.board[computer_move] == " "):
                print(f"Computer chose cell {computer_move}")
                # Adds an O at the position of cell number in board list
                self.board[computer_move] = 'O'
                # Adds the computer move to the set played
                self.played.add(computer_move)
                self.printBoard()
                break

    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
        """Checking all rows and columns and diagonals"""
        # Check if any of the 3 rows have all Xs or Os
        if(self.board[0] == who and self.board[1] == who and self.board[2] == who):
            return True
        elif(self.board[3] == who and self.board[4] == who and self.board[5] == who):
            return True
        elif(self.board[6] == who and self.board[7] == who and self.board[8] == who):
            return True
        # Check if any of the 3 columns have all Xs or Os
        elif(self.board[0] == who and self.board[3] == who and self.board[6] == who):
            return True
        elif(self.board[1] == who and self.board[4] == who and self.board[7] == who):
            return True
        elif(self.board[2] == who and self.board[5] == who and self.board[8] == who):
            return True
        # Check if any of the 2 diagonals have all Xs or Os
        elif(self.board[0] == who and self.board[4] == who and self.board[8] == who):
            return True
        elif(self.board[2] == who and self.board[4] == who and self.board[6] == who):
            return True
        else:
            return False

    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or 
                 "You lost! Thanks for playing." or 
                 "A draw! Thanks for playing."  
        """
        if (self.hasWon(who) == True):
            if(who == 'X'):
                print("You won! Thanks for playing.")
                return True
            elif(who == 'O'):
                print("You lost! Thanks for playing.")
                return True
            else:
                print("Invalid move")
                return False
        # If no one won and length of played is 9, then it's a DRAW
        elif (len(self.played) == 9):
            print("A draw! Thanks for playing.")
            return True
        else:
            return False


if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')):
            break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')):
            break   # if O won or a draw, print message and terminate

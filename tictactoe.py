# AP Computer Science Principles Final Project: TicTacToe
#
#   Author: 
#   Date:   5/1/23


class TicTacToe:
    def __init__(self):
        self.board = [-1 for _ in range(9)]     # initialize board
        self.x_turn = False                     # start on false, for O's turn 
                                                # (will switch to X turn later)
        self.is_draw = False

    def play(self):
        """
            Main Loop. This loop:
            - prints the board
            - recieves user input for each player
            - places their move on the board
            - checks if there is a winner or draw

            The loop continues until there is a winner or a draw
        """

        print('Welcome to TicTacToe!\n\nWhen it is your turn, enter the position' +
              ' you would like to place an x or o \n\t(eg. Enter 3 1 to place a' + 
              ' mark on the bottom right square)\n')
        
        # Main loop: continue until game is over by winner or draw
        while not self.game_over():

            # switch turn to other player
            self.x_turn = not self.x_turn     

            # Print the current board to user
            self.print_board()

            # Get user input for position
            print(f'\nPlayer {"X" if self.x_turn else "O"}\'s Turn!')

            # Get user input for next move
            (x,y) = self.get_input()

            # Execute player's move
            self.place_marker(x, y)

        # Print results
        if self.is_draw:
            # Game was a draw
            print('Draw!\n')
        else:
            # Current player (indicated by x_turn) has won
            print(f'Player {"X" if self.x_turn else "O"} has won!\n')

        # Print final board
        self.print_board()

    
    def get_marker(self, x: int, y: int) -> int: 
        """
            Returns the marker (-1, 0, or 1) at the position (x,y)
            -1 for an empty spot, 0 for an O, and 1 for an X

        Args:
            x (int): x position
            y (int): y position

        Returns:
            int: marker at the position (x,y)
        """

        return self.board[x + 3*y]
    
    def place_marker(self, x: int, y: int):
        """
            Places a marker for the currect player (indicated by x_turn) at 
            the given (x,y) coordinate. Saves a 0 for O and 1 for X

        Args:
            x (int): x position
            y (int): y position
        """
        self.board[x + 3*y] = int(self.x_turn)

    def get_input(self) -> tuple[int,int]:
        """
            This function gets an x and y input from the user
            It ensures valid input by checking:
                - input is the correct length and xy is numeric
                - xy input is within range of the board
                - (x,y) position on the board is unoccupied by another marker

        Returns:
            tuple[int,int]: validated x and y that user provided
        """

        while True:

            # Get User Input
            uin = input("Enter the position to place a piece: x y\n")

            # Check if user input is the right length len("x y")==3
            if len(uin) != 3:
                print('Invalid input - must be format: x y')
                continue

            # Check if xy input is numeric and assign the values to xy
            x = self.check_input(uin[0])
            y = self.check_input(uin[2])
            if x is None or y is None:
                print('Invalid input - x and y must be integers')
                continue

            # Check if xy are in range of the board (1-3)
            if x not in [0,1,2] or y not in [0,1,2]:
                print('Invalid Input - x and y must be in range [1,2,3]')
                continue

            # Swap y to make y=0 be the bottom row instead of the top
            if y == 0:
                y = 2
            elif y == 2:
                y = 0

            # Check if position (x,y) on board is occupied
            if (self.get_marker(x,y) != -1):
                print(f'Invalid Input - position on board is occupied')
                continue

            # Input is valid - break loop
            break

        return (x,y)
    
    def check_input(self, ch: str) -> int | None:
        """
            Checks user input character (uin) and returns an integer or None if
            the character is not a valid integer

            Args:
                str: User input character
            
            Returns:
                int or None: user input converted to an integer or None if not valid
        """
        if ch.isnumeric():
            return int(ch) - 1
        else:
            return None


    def game_over(self) -> bool:
        """
            Checks if the game is over by winning or draw. Checks if the 
            markers of the current player match any of defined winning 
            positions. If not, but the board is still full (no empty spots),
            the game is a draw.

            If the game is a draw, self.is_draw is set True

        Returns:
            bool: True if the game is over by draw or winning
        """

        # convert board into 1's for each marker of current player and 0's for
        # all other positions - eg. if X is the current player, all X's on the 
        # board are saved as 1 while every other position is saved as 0
        player_board = [int(marker==int(self.x_turn)) for marker in self.board]

        # List of winning positions - if player_board at each index of any 
        # of the following winning positions is 1, then thatplayer has reached
        # a winning position and has won
        winning_pos = [
            [0, 1, 2],    # first row
            [3, 4, 5],    # second row
            [6, 7, 8],    # third row
            [0, 3, 6],    # first column
            [1, 4, 7],    # second column
            [2, 5, 8],    # third column
            [0, 4, 8],    # first diagnol
            [2, 4, 6],    # second diagnol
        ]

        # Check if player_board is in a winning position
        for pos in winning_pos:
            win = True
            for m in pos:
                if not player_board[m]:
                    win = False
            if win:
                # Game over if player has won
                return True
        
        # Check if draw - draw if board is full but no winner
        self.is_draw = True 
        for marker in self.board:
            if marker == -1:
                self.is_draw = False
        return self.is_draw

    def print_board(self):
        """
            Prints the board to the console.
            Empty spots are printed as '_'
        """

        print('Board:')
        for i in range(3):
            for j in range(3):
                ch = '_'
                if self.board[j+3*i] == 0:
                    ch = 'O'
                elif self.board[j+3*i] == 1:
                    ch = 'X'
                print(ch, end=' ')
            print()
        

if __name__ == '__main__':
    # Main method initializes the TicTacToe game and runs it
    game = TicTacToe()
    game.play()
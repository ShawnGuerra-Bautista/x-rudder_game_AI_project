To run the game, simply run the script.

HUMAN MODE
The game starts with player 1, and then switched to player 2, and then back to player 1, and so on.
Player 1's token is represented by an 'X'
Player 2's token is represented by an 'O'
Each player can place a token in an open space, or move a token in an open space.
It could also move tokens on the same place (logic: the token is taken and the place it was in is now free)
The game ends when:
	All players have used their 15 tokens resulting in a TIE if there are no winners
	A player has formed an 'X' on a 3x3 section of the board 
		without the opposing player's token placed on the left and right side of the 'X'.

AI MODE
To activate AI mode, make sure the variable in the code (is_player_2_human = False).
To set the AI as Player 1, make sure the variable in the code (is_ai_max = True).
All variables are located on the top of the code.

The player can place a token in an open space or move their tokens.
The AI, using the minmax algorithm, will figure out its best move to either prevent the player from winning, or
	achieve the best position in order to win

Note: This script is using 'numpy', so installation of 'numpy' may be required into the local machine.

Library used:
Numpy
Math

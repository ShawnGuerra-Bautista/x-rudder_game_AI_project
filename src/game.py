import numpy as np


def placing_token(board_game, board_token, board_row, board_column):
    board_game[board_row, board_column] = board_token
    return


def remove_token(board_game, board_row, board_column):
    board_game[board_row, board_column] = ' '
    return


def true_row_position(board_row):
    return (10 - board_row) % 10


def true_column_position(board_column):
    true_column = 0
    if board_column == 'a':
        true_column = 1
    elif board_column == 'b':
        true_column = 2
    elif board_column == 'c':
        true_column = 3
    elif board_column == 'd':
        true_column = 4
    elif board_column == 'e':
        true_column = 5
    elif board_column == 'f':
        true_column = 6
    elif board_column == 'g':
        true_column = 7
    elif board_column == 'h':
        true_column = 8
    elif board_column == 'i':
        true_column = 9
    elif board_column == 'j':
        true_column = 10
    elif board_column == 'k':
        true_column = 11
    elif board_column == 'l':
        true_column = 12

    return true_column


'''
    Quadrant 1
        [ ][ ][X][ ][X]
        [ ][ ][ ][X][ ]
        [ ][ ]['X'][ ][X]
        [ ][ ][ ][ ][ ]
        [ ][ ][ ][ ][ ]
'''


def check_quadrant_1(board_game, board_row, board_column, token, opposing_token):
    if board_row - 2 < 0 or board_column + 2 > 12:
        return False
    else:
        return board_game[board_row][board_column] == token \
               and board_game[board_row][board_column + 2] == token \
               and board_game[board_row - 2][board_column] == token \
               and board_game[board_row - 1][board_column + 1] == token \
               and board_game[board_row - 2][board_column + 2] == token \
               and (board_game[board_row - 1][board_column] != opposing_token
                    or board_game[board_row - 1][board_column + 2] != opposing_token)


'''
    Quadrant 2
        [X][ ][X][ ][ ]
        [ ][X][ ][ ][ ]
        [X][ ]['X'][ ][ ]
        [ ][ ][ ][ ][ ]
        [ ][ ][ ][ ][ ]
'''


def check_quadrant_2(board_game, board_row, board_column, token, opposing_token):
    if board_row - 2 < 0 or board_column - 2 < 1:
        return False
    else:
        return board_game[board_row][board_column] == token \
               and board_game[board_row][board_column - 2] == token \
               and board_game[board_row - 2][board_column] == token \
               and board_game[board_row - 1][board_column - 1] == token \
               and board_game[board_row - 2][board_column - 2] == token \
               and (board_game[board_row - 1][board_column] != opposing_token
                    or board_game[board_row - 1][board_column - 2] != opposing_token)


'''
    Quadrant 3
        [ ][ ][ ][ ][ ]
        [ ][ ][ ][ ][ ]
        [X][ ]['X'][ ][ ]
        [ ][X][ ][ ][ ]
        [X][ ][X][ ][ ]
'''


def check_quadrant_3(board_game, board_row, board_column, token, opposing_token):
    if board_row + 2 > 9 or board_column - 2 < 1:
        return False
    else:
        return board_game[board_row][board_column] == token \
               and board_game[board_row][board_column - 2] == token \
               and board_game[board_row + 2][board_column] == token \
               and board_game[board_row + 1][board_column - 1] == token \
               and board_game[board_row + 2][board_column - 2] == token \
               and (board_game[board_row + 1][board_column] != opposing_token
                    or board_game[board_row + 1][board_column - 2] != opposing_token)


'''
    Quadrant 4
        [ ][ ][ ][ ][ ]
        [ ][ ][ ][ ][ ]
        [ ][ ]['X'][ ][X]
        [ ][ ][ ][X][ ]
        [ ][ ][X][ ][X]
'''


def check_quadrant_4(board_game, board_row, board_column, token, opposing_token):
    if board_row + 2 > 9 or board_column + 2 > 12:
        return False
    else:
        return board_game[board_row][board_column] == token \
               and board_game[board_row][board_column + 2] == token \
               and board_game[board_row + 2][board_column] == token \
               and board_game[board_row + 1][board_column + 1] == token \
               and board_game[board_row + 2][board_column + 2] == token \
               and (board_game[board_row + 1][board_column] != opposing_token
                    or board_game[board_row + 1][board_column + 2] != opposing_token)


'''
    Quadrant 5
        [ ][ ][ ][ ][ ]
        [ ][X][ ][X][ ]
        [ ][ ]['X'][ ][ ]
        [ ][X][ ][X][ ]
        [ ][ ][ ][ ][ ]
'''


# 'quadrant 5' refers to the 'center' where the token is placed
def check_quadrant_5(board_game, board_row, board_column, token, opposing_token):
    if board_row + 1 > 9 or board_column + 1 > 12 or board_row - 1 < 0 or board_column - 1 < 1:
        return False
    else:
        return board_game[board_row][board_column] == token \
               and board_game[board_row - 1][board_column + 1] == token \
               and board_game[board_row - 1][board_column - 1] == token \
               and board_game[board_row + 1][board_column - 1] == token \
               and board_game[board_row + 1][board_column + 1] == token \
               and (board_game[board_row][board_column + 1] != opposing_token
                    or board_game[board_row][board_column - 1] != opposing_token)


def is_player_1_winner(board_game, board_row, board_column):
    return check_quadrant_1(board_game, board_row, board_column, 'X', 'O') \
           or check_quadrant_2(board_game, board_row, board_column, 'X', 'O') \
           or check_quadrant_3(board_game, board_row, board_column, 'X', 'O') \
           or check_quadrant_4(board_game, board_row, board_column, 'X', 'O') \
           or check_quadrant_5(board_game, board_row, board_column, 'X', 'O')


def is_player_2_winner(board_game, board_row, board_column):
    return check_quadrant_1(board_game, board_row, board_column, 'O', 'X') \
           or check_quadrant_2(board_game, board_row, board_column, 'O', 'X') \
           or check_quadrant_3(board_game, board_row, board_column, 'O', 'X') \
           or check_quadrant_4(board_game, board_row, board_column, 'O', 'X') \
           or check_quadrant_5(board_game, board_row, board_column, 'O', 'X')


# ==========================================GAME=============================================
# Variables

player_1_tokens = 15  # Denoted by an X
player_2_tokens = 15  # Denoted by an O
player_1_turn = True
total_moves = 30
winner = 'NONE'

# The board's row number are upside down in this program so use mod 10
board_body = [['10', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']]

# Prints in array format
board = np.array(board_body)
print(board)

# Emulates a do-while loop
while player_1_tokens != 0 or player_2_tokens != 0 or total_moves != 0:
    if player_1_turn:
        print()
        print('===============================')
        print('===========PLAYER 1============')
        print('===============================')
        print('========TOKEN REMAINING========')
        print('============= ' + str(player_1_tokens) + ' ==============')
        print('===============================')
        print('========MOVES REMAINING========')
        print('============= ' + str(total_moves) + ' ==============')
        print('===============================')
        print()

        position = input('Choose a position: ')
        row = true_row_position(int(position[1:3]))
        column = true_column_position(position[0].lower())

        old_row = -1
        old_column = -1

        if player_1_tokens != 0:
            while board[row, column] == 'O':
                position = input('Choose another position: ')
                row = true_row_position(int(position[1:3]))
                column = true_column_position(position[0].lower())

            if board[row, column] == 'X':
                old_row = row
                old_column = column
                remove_token(board, row, column)

                position = input('Choose the position you want to move the token: ')
                row = true_row_position(int(position[1:3]))
                column = true_column_position(position[0].lower())

                while board[row, column] != ' ':
                    position = input('Choose another position: ')
                    row = true_row_position(int(position[1:3]))
                    column = true_column_position(position[0].lower())
                total_moves -= 1

            else:
                player_1_tokens -= 1
        else:
            while board[row, column] != 'X':
                position = input('Choose one of your token to move: ')
                row = true_row_position(int(position[1:3]))
                column = true_column_position(position[0].lower())

            old_row = row
            old_column = column
            remove_token(board, row, column)

            position = input('Choose the position you want to move the token: ')
            row = true_row_position(int(position[1:3]))
            column = true_column_position(position[0].lower())

            while board[row, column] != ' ':
                position = input('Choose another position: ')
                row = true_row_position(int(position[1:3]))
                column = true_column_position(position[0].lower())
            total_moves -= 1

        placing_token(board, 'X', row, column)

        print()
        print(board)

        if is_player_1_winner(board, row, column):
            winner = 'Player 1'
            break

        if old_row - 1 >= 0 and board[old_row - 1, old_column] == 'O' \
                and is_player_2_winner(board, old_row - 1, old_column):
            winner = 'Player 2'
            break

        if old_row + 1 <= 9 and board[old_row + 1, old_column] == 'O' \
                and is_player_2_winner(board, old_row + 1, old_column):
            winner = 'Player 2'
            break

        player_1_turn = False

    else:
        print()
        print('===============================')
        print('===========PLAYER 2============')
        print('===============================')
        print('========TOKEN REMAINING========')
        print('============= ' + str(player_2_tokens) + ' ==============')
        print('===============================')
        print('========MOVES REMAINING========')
        print('============= ' + str(total_moves) + ' ==============')
        print('===============================')

        print()

        position = input('Choose a position: ')
        row = true_row_position(int(position[1:3]))
        column = true_column_position(position[0].lower())

        old_row = -1
        old_column = -1

        if player_2_tokens != 0:
            while board[row, column] == 'X':
                position = input('Choose another position: ')
                row = true_row_position(int(position[1:3]))
                column = true_column_position(position[0].lower())

            if board[row, column] == 'O':
                old_row = row
                old_column = column
                remove_token(board, row, column)

                position = input('Choose the position you want to move the token: ')
                row = true_row_position(int(position[1:3]))
                column = true_column_position(position[0].lower())

                while board[row, column] != ' ':
                    position = input('Choose another position: ')
                    row = true_row_position(int(position[1:3]))
                    column = true_column_position(position[0].lower())
                total_moves -= 1

            else:
                player_2_tokens -= 1
        else:
            while board[row, column] != 'O':
                position = input('Choose another position: ')
                row = true_row_position(int(position[1:3]))
                column = true_column_position(position[0].lower())

            old_row = row
            old_column = column
            remove_token(board, row, column)

            position = input('Choose the position you want to move the token: ')
            row = true_row_position(int(position[1:3]))
            column = true_column_position(position[0].lower())

            while board[row, column] != ' ':
                position = input('Choose another position: ')
                row = true_row_position(int(position[1:3]))
                column = true_column_position(position[0].lower())
            total_moves -= 1

        placing_token(board, 'O', row, column)

        print()
        print(board)

        if is_player_2_winner(board, row, column):
            winner = 'Player 2'
            break

        if old_row - 1 >= 0 and board[old_row - 1, old_column] == 'X' \
                and is_player_1_winner(board, old_row - 1, old_column):
            winner = 'Player 1'
            break

        if old_row + 1 <= 9 and board[old_row + 1, old_column] == 'X' \
                and is_player_1_winner(board, old_row + 1, old_column):
            winner = 'Player 1'
            break

        player_1_turn = True

print()
if winner != 'NONE':
    print(winner + ' is the Winner!!!')
else:
    print('TIE!')

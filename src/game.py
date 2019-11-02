import numpy as np

# Variables
player_1_tokens = 5  # Denoted by an X
player_1_token = 'X'
player_2_tokens = 5  # Denoted by an O
player_2_token = 'O'
is_player_1_turn = True
total_moves = 30
winner = None

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


def placing_token(board_game, board_token, board_row, board_column):
    board_game[board_row, board_column] = board_token
    return


def remove_token(board_game, board_row, board_column):
    board_game[board_row, board_column] = ' '
    return


def true_row_position(board_row):
    return 10 - board_row


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


def is_move_possible(board_game, board_row, board_column, old_board_row, old_board_column):
    return old_board_row + 1 >= board_row >= old_board_row - 1 \
           and old_board_column + 1 >= board_column >= old_board_column - 1 \
           and 9 >= board_row >= 0 and 12 >= board_column >= 1 \
           and board_game[board_row][board_column] == ' '


def is_placement_possible(board_row, board_column):
    return 9 >= board_row >= 0 and 12 >= board_column >= 1


def is_player_winner(board_game, board_row, board_column, player_token, opposing_player_token):
    return check_quadrant_1(board_game, board_row, board_column, player_token, opposing_player_token) \
           or check_quadrant_2(board_game, board_row, board_column, player_token, opposing_player_token) \
           or check_quadrant_3(board_game, board_row, board_column, player_token, opposing_player_token) \
           or check_quadrant_4(board_game, board_row, board_column, player_token, opposing_player_token) \
           or check_quadrant_5(board_game, board_row, board_column, player_token, opposing_player_token)


def winner_evaluation(board_game, board_row, board_column, board_old_row, board_old_column, is_turn_of_player_one):
    player_token = 'X' if is_turn_of_player_one else 'O'
    opposing_player_token = 'O' if is_turn_of_player_one else 'X'

    evaluated_winner = None

    if is_player_winner(board_game, board_row, board_column, player_token, opposing_player_token):
        evaluated_winner = 'Player 1' if is_turn_of_player_one else 'Player 2'

    if ((board_old_row - 1 >= 0 and board_game[board_old_row - 1, board_old_column] == opposing_player_token and
         is_player_winner(board_game, board_old_row - 1, board_old_column, opposing_player_token, player_token)) or
            (board_old_row + 1 <= 9 and board_game[board_old_row + 1, board_old_column] == opposing_player_token and
             is_player_winner(board_game, board_old_row + 1, board_old_column, opposing_player_token, player_token))):
        evaluated_winner = 'Player 2' if is_turn_of_player_one else 'Player 1'

    return evaluated_winner


def turn_of_player(board_game, player_token, opposing_player_token):
    global is_player_1_turn
    global total_moves
    global player_1_tokens
    global player_2_tokens
    global winner

    print('===============================')
    print('===========' + ('Player 1' if is_player_1_turn else 'Player 2') + '============')
    print('===============================')
    print('========TOKEN REMAINING========')
    print('============= ' + str(player_1_tokens if is_player_1_turn else player_2_tokens) + ' ==============')
    print('===============================')
    print('========MOVES REMAINING========')
    print('============= ' + str(total_moves) + ' ==============')
    print('===============================')
    print()
    print(board_game)

    position = input('Choose a position to move/place a token: ')
    row = true_row_position(int(position[1:3]))
    column = true_column_position(position[0].lower())

    old_row = -1
    old_column = -1

    if (player_1_tokens if is_player_1_turn else player_2_tokens) != 0:
        while board_game[row, column] == opposing_player_token or not is_placement_possible(row, column):
            position = input('Choose another position to move/place the token: ')
            row = true_row_position(int(position[1:3]))
            column = true_column_position(position[0].lower())

        if board_game[row, column] == player_token:
            old_row = row
            old_column = column
            remove_token(board_game, row, column)

            position = input('Choose the position you want to move the token: ')
            row = true_row_position(int(position[1:3]))
            column = true_column_position(position[0].lower())

            while not is_move_possible(board_game, row, column, old_row, old_column):
                position = input('Choose another position to move the token: ')
                row = true_row_position(int(position[1:3]))
                column = true_column_position(position[0].lower())
            total_moves -= 1

        else:
            if is_player_1_turn:
                player_1_tokens -= 1
            else:
                player_2_tokens -= 1
    else:
        while board_game[row, column] != player_token:
            position = input('Choose one of your tokens to move: ')
            row = true_row_position(int(position[1:3]))
            column = true_column_position(position[0].lower())

        old_row = row
        old_column = column
        remove_token(board_game, row, column)

        position = input('Choose the position you want to move the token: ')
        row = true_row_position(int(position[1:3]))
        column = true_column_position(position[0].lower())

        while not is_move_possible(board_game, row, column, old_row, old_column):
            position = input('Choose another position to move: ')
            row = true_row_position(int(position[1:3]))
            column = true_column_position(position[0].lower())
        total_moves -= 1

    placing_token(board_game, player_token, row, column)

    winner = winner_evaluation(board_game, row, column, old_row, old_column, is_player_1_turn)

    return winner


# ==========================================GAME============================================
# Emulates a do-while loop

while player_1_tokens != 0 or player_2_tokens != 0 or total_moves != 0:
    is_player_1_turn = True
    if turn_of_player(board, player_1_token, player_2_token) is not None:
        break
    is_player_1_turn = False
    if turn_of_player(board, player_2_token, player_1_token) is not None:
        break

if winner is not None:
    print(winner + ' is the Winner!!!')
else:
    print('TIE!')

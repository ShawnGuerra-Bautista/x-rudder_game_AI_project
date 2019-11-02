import math

import numpy as np

# ==========================================GAME VARIABLE============================================
# Variables
player_1_tokens = 15  # Denoted by an X
PLAYER_1_TOKEN = 'X'  # Represents Max Player
player_2_tokens = 15  # Denoted by an O
PLAYER_2_TOKEN = 'O'  # Represents Min Player

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


# ==========================================HELPER============================================


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


# ===========================================AI=============================================

# For optimization, but will think about it later
player_1_history_tokens = []
player_2_history_tokens = []
free_spaces = []


def initialize_free_spaces():
    global free_spaces
    for row in range(0, 10):
        for column in range(1, 13):
            free_spaces.append(tuple((row, column)))


def generate_possible_all_possible_list(board_game, row, column):
    valid_moves = []
    for r in range(-1, 2):
        for c in range(-1, 2):
            if is_move_possible(board_game, row + r, column + c, row, column):
                valid_moves.append(tuple((row + r, column + c)))
    return valid_moves


def is_strikethrough_in_quadrant(board_game, row_of_center, column_of_center, is_max_playing):
    return (board_game[row_of_center, column_of_center - 1] == PLAYER_1_TOKEN
            and board_game[row_of_center, column_of_center + 1] == PLAYER_1_TOKEN) if not is_max_playing \
        else (board_game[row_of_center, column_of_center - 1] == PLAYER_2_TOKEN
              and board_game[row_of_center, column_of_center + 1] == PLAYER_2_TOKEN)


def scoring_token_counter_for_quadrant(board_game, row_of_center, column_of_center):
    token_of_max = 0
    token_of_min = 0

    if board_game[row_of_center - 1, column_of_center - 1] != ' ':
        if board_game[row_of_center - 1, column_of_center - 1] == PLAYER_1_TOKEN:
            token_of_max += 1
        else:
            token_of_min += 1
    if board_game[row_of_center - 1, column_of_center + 1] != ' ':
        if board_game[row_of_center - 1, column_of_center + 1] == PLAYER_1_TOKEN:
            token_of_max += 1
        else:
            token_of_min += 1

    if board_game[row_of_center, column_of_center] != ' ':
        if board_game[row_of_center, column_of_center] == PLAYER_1_TOKEN:
            token_of_max += 1
        else:
            token_of_min += 1

    if board_game[row_of_center + 1, column_of_center - 1] != ' ':
        if board_game[row_of_center + 1, column_of_center - 1] == PLAYER_1_TOKEN:
            token_of_max += 1
        else:
            token_of_min += 1

    if board_game[row_of_center + 1, column_of_center + 1] != ' ':
        if board_game[row_of_center + 1, column_of_center + 1] == PLAYER_1_TOKEN:
            token_of_max += 1
        else:
            token_of_min += 1

    return token_of_max, token_of_min


def score_of_quadrant(board_game, row_of_center, column_of_center, is_max_playing):
    token_of_max, token_of_min = scoring_token_counter_for_quadrant(board_game, row_of_center, column_of_center)
    value = 0

    if is_strikethrough_in_quadrant(board_game, row_of_center, column_of_center, is_max_playing):
        value += 0
    elif token_of_max == 5:
        value += 100000
    elif token_of_min == 5:
        value -= 100000
    elif token_of_max == 4:
        value += 10000
    elif token_of_min == 4:
        value -= 10000
    elif token_of_max == 3:
        value += 1000
    elif token_of_min == 3:
        value -= 1000
    elif token_of_max == 2:
        value += 100
    elif token_of_min == 2:
        value -= 100
    elif token_of_max == 1:
        value += 10
    elif token_of_min == 1:
        value -= 10

    return value


def score_of_position(board_game, row, column, is_max_playing):
    value = 0

    # Score of Quad 1
    if row - 2 >= 0 and column + 2 <= 12:
        value += score_of_quadrant(board_game, row - 1, column + 1, is_max_playing)

    # Score of Quad 2
    if row - 2 >= 0 and column - 2 >= 1:
        value += score_of_quadrant(board_game, row - 1, column - 1, is_max_playing)

    # Score of Quad 3
    if row + 2 <= 9 and column - 2 >= 1:
        value += score_of_quadrant(board_game, row + 1, column - 1, is_max_playing)

    # Score of Quad 4
    if row + 2 <= 9 and column + 2 <= 12:
        value += score_of_quadrant(board_game, row + 1, column + 1, is_max_playing)

    # Score of Quad 5
    if row - 1 >= 0 and row + 1 <= 9 and column - 1 >= 1 and column + 1 <= 12:
        value += score_of_quadrant(board_game, row, column, is_max_playing)

    return value


"""
    USE IS_MOVE/PLACEMENT_POSSIBLE to check which position are valid to take (used inside minmax)
"""


def is_node_a_leaf(board_game, board_row, board_column):
    return is_player_winner(board_game, board_row, board_column, PLAYER_1_TOKEN, PLAYER_2_TOKEN) \
           or is_player_winner(board_game, board_row, board_column, PLAYER_2_TOKEN, PLAYER_1_TOKEN) \
           or (total_moves == 0 and player_1_tokens == 0 and player_2_tokens == 0)


def minmax(board_game, row, column, is_max_playing, alpha, beta, depth, valid_placement):
    if depth == 0 or is_node_a_leaf(board_game, row, column):
        return row, column, score_of_position(board_game, row, column, is_max_playing)

    if is_max_playing and player_1_tokens != 0:
        value = -math.inf
        (best_row, best_column) = valid_placement[0]
        for new_row, new_column in free_spaces:
            board_copy = board_game.copy()
            placing_token(board_copy, PLAYER_1_TOKEN, new_row, new_column)
            new_valid_placement = valid_placement.copy()
            new_valid_placement.remove(tuple((new_row, new_column)))
            score = minmax(board_copy, new_row, new_column, False, alpha, beta, depth - 1, new_valid_placement)[2]
            if score > value:
                value = score
                best_row = new_row
                best_column = new_column
            alpha = max(value, alpha)
            if alpha >= beta:
                break
        return best_row, best_column, value
    elif is_max_playing and total_moves != 0:
        value = math.inf
        return row, column, value
    elif not is_max_playing and player_2_tokens != 0:
        value = math.inf
        (best_row, best_column) = valid_placement[0]
        for new_row, new_column in free_spaces:
            board_copy = board_game.copy()
            placing_token(board_copy, PLAYER_2_TOKEN, new_row, new_column)
            new_valid_placement = valid_placement.copy()
            new_valid_placement.remove(tuple((new_row, new_column)))
            score = minmax(board_copy, new_row, new_column, True, alpha, beta, depth - 1, new_valid_placement)[2]
            if score < value:
                value = score
                best_row = new_row
                best_column = new_column
            alpha = max(value, alpha)
            if alpha >= beta:
                break
        return best_row, best_column, value
    elif not is_max_playing and total_moves != 0:
        value = math.inf
        return row, column, value
    else:
        return minmax(board_game, row, column, not is_max_playing, alpha, beta, depth, valid_placement)
    # TODO: MinMax Algorithm which returns the row, column and Value
    # Recursive function and base case is if depth = 0 or is_node_a_leaf
    # Should return a tuple of row, column, value


def turn_of_ai():
    # TODO: Same as players turn, but optimize moves
    return


# ==========================================HUMAN============================================


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

        global player_1_history_tokens
        global free_spaces
        if old_row != -1 and old_column != -1:
            player_1_history_tokens.remove(tuple((old_row, old_column)))
            player_1_history_tokens.append(tuple((row, column)))
            free_spaces.append(tuple((old_row, old_column)))
            free_spaces.remove(tuple((row, column)))
        else:
            player_1_history_tokens.append(tuple((row, column)))
            free_spaces.remove(tuple((row, column)))
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

        global player_2_history_tokens
        global free_spaces
        if old_row != -1 and old_column != -1:
            player_2_history_tokens.remove(tuple((old_row, old_column)))
            player_2_history_tokens.append(tuple((row, column)))
            free_spaces.append(tuple((old_row, old_column)))
            free_spaces.remove(tuple((row, column)))
        else:
            player_2_history_tokens.append(tuple((row, column)))
            free_spaces.remove(tuple((row, column)))

    placing_token(board_game, player_token, row, column)

    winner = winner_evaluation(board_game, row, column, old_row, old_column, is_player_1_turn)

    return winner


# ==========================================GAME============================================

initialize_free_spaces()

while player_1_tokens != 0 or player_2_tokens != 0 or total_moves != 0:
    is_player_1_turn = True
    if turn_of_player(board, PLAYER_1_TOKEN, PLAYER_2_TOKEN) is not None:
        break
    is_player_1_turn = False
    if turn_of_player(board, PLAYER_2_TOKEN, PLAYER_1_TOKEN) is not None:
        break

if winner is not None:
    print(winner + ' is the Winner!!!')
else:
    print('TIE!')

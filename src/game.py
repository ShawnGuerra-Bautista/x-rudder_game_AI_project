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
is_ai_max = True

# The board's row number are upside down in this program so use mod 10
board_body = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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


# Initialize all free spaces on the board (for optimization)
def initialize_free_spaces():
    global free_spaces
    for row in range(0, 10):
        for column in range(1, 13):
            free_spaces.append(tuple((row, column)))


# Generate all possible moves that a token can make (for optimization)
def generate_all_possible_moves_list(board_game, row, column):
    valid_moves = []
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if is_move_possible(board_game, row + r, column + c, row, column):
                valid_moves.append(tuple((row + r, column + c)))
    return valid_moves


# Check if there's a strikethrough in that quadrant depending on which player is playing
# e.g. if it's player 1, ['O' '~' 'O'], putting a token in the middle will net you 0
# That's because that quadrant has been already "negated" by the other player
def is_strikethrough_in_quadrant(board_game, row_of_center, column_of_center, is_max_playing):
    return (board_game[row_of_center, column_of_center - 1] == PLAYER_1_TOKEN
            and board_game[row_of_center, column_of_center + 1] == PLAYER_1_TOKEN) if not is_max_playing \
        else (board_game[row_of_center, column_of_center - 1] == PLAYER_2_TOKEN
              and board_game[row_of_center, column_of_center + 1] == PLAYER_2_TOKEN)


# Calculates the number of non scoring tokens in the quadrant of each player
def non_scoring_token_in_quadrant(board_game, row_of_center, column_of_center):
    token_of_max = 0
    token_of_min = 0

    if board_game[row_of_center - 1, column_of_center] != ' ':
        if board_game[row_of_center - 1, column_of_center] == PLAYER_1_TOKEN:
            token_of_max += 1
        else:
            token_of_min += 1
    if board_game[row_of_center, column_of_center - 1] != ' ':
        if board_game[row_of_center - 1, column_of_center + 1] == PLAYER_1_TOKEN:
            token_of_max += 1
        else:
            token_of_min += 1

    if board_game[row_of_center, column_of_center - 1] != ' ':
        if board_game[row_of_center, column_of_center + 1] == PLAYER_1_TOKEN:
            token_of_max += 1
        else:
            token_of_min += 1

    if board_game[row_of_center + 1, column_of_center] != ' ':
        if board_game[row_of_center + 1, column_of_center] == PLAYER_1_TOKEN:
            token_of_max += 1
        else:
            token_of_min += 1

    return token_of_max, token_of_min


# Count the number of tokens of each player in a "quadrant's" winning position
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


# Depending on the number of tokens for each player, assign a score to the position of that "quadrant"
# Before that check, if there is a strikethrough
def score_of_quadrant(board_game, row_of_center, column_of_center, is_max_playing):
    scoring_token_of_max, scoring_token_of_min = scoring_token_counter_for_quadrant(board_game,
                                                                                    row_of_center, column_of_center)
    non_scoring_token_max, non_scoring_token_min = non_scoring_token_in_quadrant(board_game,
                                                                                 row_of_center, column_of_center)
    value = 0

    if is_strikethrough_in_quadrant(board_game, row_of_center, column_of_center, is_max_playing):
        value += 0
    elif scoring_token_of_max == 5:
        value += 1000000
    elif scoring_token_of_min == 5:
        value -= 1000000
    elif scoring_token_of_max == 4:
        value += 100000
    elif scoring_token_of_min == 4:
        value -= 100000
    elif scoring_token_of_max == 3:
        value += 10000
    elif scoring_token_of_min == 3:
        value -= 10000
    elif scoring_token_of_max == 2:
        value += 1000
    elif scoring_token_of_min == 2:
        value -= 1000
    elif scoring_token_of_max == 1:
        value += 100
    elif scoring_token_of_min == 1:
        value -= 100

    if non_scoring_token_max == 4:
        value += 1000
    elif non_scoring_token_min == 4:
        value -= 1000
    elif non_scoring_token_max == 3:
        value += 100
    elif non_scoring_token_min == 3:
        value -= 100
    elif non_scoring_token_max == 2:
        value += 10
    elif non_scoring_token_min == 2:
        value -= 10
    elif non_scoring_token_max == 1:
        value += 1
    elif non_scoring_token_min == 1:
        value -= 1

    return value


# Scores the position using the 5 "quadrants"
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


# If the game is ending during that turn, then true
def is_node_a_leaf(board_game, board_row, board_column, max_player_tokens, min_player_tokens, total_player_moves):
    return board_row != -1 and board_column != -1 \
           and is_player_winner(board_game, board_row, board_column, PLAYER_1_TOKEN, PLAYER_2_TOKEN) \
           or is_player_winner(board_game, board_row, board_column, PLAYER_2_TOKEN, PLAYER_1_TOKEN) \
           or (total_player_moves == 0 and max_player_tokens == 0 and min_player_tokens == 0)


# Minmax algorithm for moving; same logic as below's algorithm for placing
def minmax_for_moving(board_game, row, column, max_player_tokens, min_player_tokens, total_player_moves,
                      is_max_playing, alpha, beta, depth,
                      valid_max_player_tokens, valid_min_player_tokens):
    if depth == 0 or is_node_a_leaf(board_game, row, column, max_player_tokens, min_player_tokens, total_player_moves):
        if is_player_winner(board_game, row, column, PLAYER_1_TOKEN, PLAYER_2_TOKEN):
            return None, None, None, None, 1000000
        elif is_player_winner(board_game, row, column, PLAYER_2_TOKEN, PLAYER_1_TOKEN):
            return None, None, None, None, -1000000
        else:
            return None, None, None, None, score_of_position(board_game, row, column, not is_max_playing)

    (best_row, best_column, old_row, old_column) = None, None, None, None

    if is_max_playing:
        value = -math.inf
        for player_tokens_position in valid_max_player_tokens:
            board_copy = board_game.copy()
            remove_token(board_copy, player_tokens_position[0], player_tokens_position[1])
            valid_max_player_moves = generate_all_possible_moves_list(board_copy,
                                                                      player_tokens_position[0],
                                                                      player_tokens_position[1])
            for player_move_position in valid_max_player_moves:
                placing_token(board_copy, PLAYER_1_TOKEN, player_move_position[0], player_move_position[1])
                new_valid_max_player_tokens = valid_max_player_tokens.copy()
                new_valid_max_player_tokens.remove(tuple((player_tokens_position[0], player_tokens_position[1])))
                new_valid_max_player_tokens.append(tuple((player_move_position[0], player_move_position[1])))
                score = minmax_for_moving(board_copy, player_move_position[0], player_move_position[1],
                                          max_player_tokens, min_player_tokens, total_player_moves - 1,
                                          False, alpha, beta, depth - 1,
                                          new_valid_max_player_tokens, valid_min_player_tokens)[4]
                if score > value:
                    value = score
                    old_row = player_tokens_position[0]
                    old_column = player_tokens_position[1]
                    best_row = player_move_position[0]
                    best_column = player_move_position[1]
                alpha = max(value, alpha)
                if alpha >= beta:
                    break
        return best_row, best_column, old_row, old_column, value
    else:
        value = math.inf
        for player_tokens_position in valid_min_player_tokens:
            board_copy = board_game.copy()
            remove_token(board_copy, player_tokens_position[0], player_tokens_position[1])
            valid_min_player_moves = generate_all_possible_moves_list(board_copy,
                                                                      player_tokens_position[0],
                                                                      player_tokens_position[1])
            for player_move_position in valid_min_player_moves:
                placing_token(board_copy, PLAYER_2_TOKEN, player_move_position[0], player_move_position[1])
                new_valid_min_player_tokens = valid_min_player_tokens.copy()
                new_valid_min_player_tokens.remove(tuple((player_tokens_position[0], player_tokens_position[1])))
                new_valid_min_player_tokens.append(tuple((player_move_position[0], player_move_position[1])))
                score = minmax_for_moving(board_copy, player_move_position[0], player_move_position[1],
                                          max_player_tokens, min_player_tokens, total_player_moves - 1,
                                          True, alpha, beta, depth - 1,
                                          valid_max_player_tokens, new_valid_min_player_tokens)[4]
                if score < value:
                    value = score
                    old_row = player_tokens_position[0]
                    old_column = player_tokens_position[1]
                    best_row = player_move_position[0]
                    best_column = player_move_position[1]
                beta = min(value, beta)
                if alpha >= beta:
                    break
        return best_row, best_column, old_row, old_column, value


# Minmax algorithm for placing tokens
def minmax_for_placing(board_game, row, column, max_player_tokens, min_player_tokens, total_player_moves,
                       is_max_playing, alpha, beta, depth, valid_placement):
    if depth == 0 or is_node_a_leaf(board_game, row, column, max_player_tokens, min_player_tokens, total_player_moves):
        # If depth is zero, or the game is going to end, then it's a leaf node
        # Reason it doesn't pass the position is that we don't want the position of the leaf node
        # We want the position of the child of root that leads to the leaf node
        # Also, added 2 if statements for faster computation
        if is_player_winner(board_game, row, column, PLAYER_1_TOKEN, PLAYER_2_TOKEN):
            return None, None, 1000000
        elif is_player_winner(board_game, row, column, PLAYER_2_TOKEN, PLAYER_1_TOKEN):
            return None, None, -1000000
        else:
            return None, None, score_of_position(board_game, row, column, not is_max_playing)

    # row and column that the AI will choose
    (best_row, best_column) = None, None

    # When Max/player_1 is playing
    if is_max_playing:
        value = -math.inf
        for space_tuple in valid_placement:
            board_copy = board_game.copy()
            placing_token(board_copy, PLAYER_1_TOKEN, space_tuple[0], space_tuple[1])
            new_valid_placement = valid_placement.copy()
            new_valid_placement.remove(tuple((space_tuple[0], space_tuple[1])))
            score = minmax_for_placing(board_copy, space_tuple[0], space_tuple[1], max_player_tokens - 1,
                                       min_player_tokens, total_player_moves,
                                       False, alpha, beta, depth - 1, new_valid_placement)[2]
            if score > value:
                value = score
                best_row = space_tuple[0]
                best_column = space_tuple[1]
            alpha = max(value, alpha)
            if alpha >= beta:
                break
        return best_row, best_column, value
    # When Min/Player_2 is playing
    else:
        value = math.inf
        for space_tuple in valid_placement:
            board_copy = board_game.copy()
            placing_token(board_copy, PLAYER_2_TOKEN, space_tuple[0], space_tuple[1])
            new_valid_placement = valid_placement.copy()
            new_valid_placement.remove(tuple((space_tuple[0], space_tuple[1])))
            score = minmax_for_placing(board_copy, space_tuple[0], space_tuple[1], max_player_tokens,
                                       min_player_tokens - 1, total_player_moves,
                                       True, alpha, beta, depth - 1, new_valid_placement)[2]
            if score < value:
                value = score
                best_row = space_tuple[0]
                best_column = space_tuple[1]
            beta = min(value, beta)
            if alpha >= beta:
                break
        return best_row, best_column, value


def turn_of_ai(board_game, player_token):
    global winner
    global free_spaces
    global player_1_tokens
    global player_2_tokens
    global total_moves

    print('===============================')
    print('===========' + ('Player 1' if is_ai_max else 'Player 2') + '============')
    print('===============================')
    print('========TOKEN REMAINING========')
    print('============= ' + str(player_1_tokens if is_ai_max else player_2_tokens) + ' ==============')
    print('===============================')
    print('========MOVES REMAINING========')
    print('============= ' + str(total_moves) + ' ==============')
    print('===============================')

    row = -1
    column = -1
    old_row = -1
    old_column = -1

    # Reason placing tokens takes priority over moving is that moving
    if (player_1_tokens if is_ai_max else player_2_tokens) != 0:
        row, column, value = minmax_for_placing(board_game, -1, -1, player_1_tokens, player_2_tokens,
                                                total_moves, is_ai_max, -math.inf, math.inf, 3, free_spaces)
        placing_token(board_game, player_token, row, column)
        if is_ai_max:
            player_1_tokens -= 1
            player_1_history_tokens.append(tuple((row, column)))
        else:
            player_2_tokens -= 1
            player_2_history_tokens.append(tuple((row, column)))
        free_spaces.remove(tuple((row, column)))
    else:
        row, column, old_row, old_column, value = minmax_for_moving(board_game, -1, -1, player_1_tokens,
                                                                    player_2_tokens, total_moves, is_ai_max,
                                                                    -math.inf, math.inf, 3,
                                                                    player_1_history_tokens,
                                                                    player_2_history_tokens)
        remove_token(board_game, old_row, old_column)
        placing_token(board_game, player_token, row, column)
        total_moves -= 1
        if is_ai_max:
            player_1_history_tokens.append(tuple((row, column)))
            player_1_history_tokens.remove(tuple((old_row, old_column)))
        else:
            player_2_history_tokens.append(tuple((row, column)))
            player_2_history_tokens.remove(tuple((old_row, old_column)))
        free_spaces.append(tuple((old_row, old_column)))
        free_spaces.remove(tuple((row, column)))
    print()
    print(board_game)

    winner = winner_evaluation(board_game, row, column, old_row, old_column, is_player_1_turn)

    return winner


# ==========================================HUMAN============================================


def turn_of_player(board_game, player_token, opposing_player_token):
    global total_moves
    global player_1_tokens
    global player_2_tokens
    global winner
    global player_1_history_tokens
    global player_2_history_tokens
    global free_spaces

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

    old_row = -1
    old_column = -1
    can_play = True

    position = input('Choose a position to move/place a token: ')
    row = true_row_position(int(position[1:3]))
    column = true_column_position(position[0].lower())

    if (player_1_tokens if is_player_1_turn else player_2_tokens) != 0:
        while board_game[row, column] == opposing_player_token or \
                not is_placement_possible(row, column) or \
                (total_moves == 0 and board_game[row, column] == player_token):
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
    elif total_moves == 0 and (player_1_tokens if is_player_1_turn else player_2_tokens) != 0:
        print("Sorry, you've used all your tokens and moves!")
        can_play = False
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

    if old_row != -1 and old_column != -1:
        if not is_ai_max:
            player_1_history_tokens.remove(tuple((old_row, old_column)))
            player_1_history_tokens.append(tuple((row, column)))
            free_spaces.append(tuple((old_row, old_column)))
            free_spaces.remove(tuple((row, column)))
        else:
            player_2_history_tokens.remove(tuple((old_row, old_column)))
            player_2_history_tokens.append(tuple((row, column)))
            free_spaces.append(tuple((old_row, old_column)))
            free_spaces.remove(tuple((row, column)))
    elif can_play:
        if not is_ai_max:
            player_1_history_tokens.append(tuple((row, column)))
            free_spaces.remove(tuple((row, column)))
        else:
            player_2_history_tokens.append(tuple((row, column)))
            free_spaces.remove(tuple((row, column)))
    else:
        return None

    placing_token(board_game, player_token, row, column)

    winner = winner_evaluation(board_game, row, column, old_row, old_column, is_player_1_turn)

    return winner


# ==========================================GAME============================================

initialize_free_spaces()

while player_1_tokens != 0 or player_2_tokens != 0 or total_moves != 0:
    if not is_ai_max:
        is_player_1_turn = True
        if (total_moves == 0 and player_1_tokens == 0) \
                or turn_of_player(board, PLAYER_1_TOKEN, PLAYER_2_TOKEN) is not None:
            break
        is_player_1_turn = False
        if (total_moves == 0 and player_2_tokens == 0) \
                or turn_of_ai(board, PLAYER_2_TOKEN) is not None:
            break
    else:
        is_player_1_turn = True
        if (total_moves == 0 and player_1_tokens == 0) \
                or turn_of_ai(board, PLAYER_1_TOKEN) is not None:
            break
        is_player_1_turn = False
        if (total_moves == 0 and player_2_tokens == 0) \
                or turn_of_player(board, PLAYER_2_TOKEN, PLAYER_1_TOKEN) is not None:
            break

if winner is not None:
    print(winner + ' is the Winner!!!')
else:
    print('TIE!')

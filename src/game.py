import numpy as np


class XRudder:
    # Class Variables
    player_1_tokens = 15  # Denoted by an X
    player_2_tokens = 15  # Denoted by an O

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

    def __init__(self):
        pass

    def placing_token(self, board_token, board_row, board_column):
        self.board[board_row, board_column] = board_token
        return

    def remove_token(self, board_row, board_column):
        self.board[board_row, board_column] = ' '
        return

    @staticmethod
    def true_row_position(board_row):
        return 10 - board_row

    @staticmethod
    def true_column_position(board_column):
        true_column = -1
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

    def check_quadrant_1(self, board_row, board_column, token, opposing_token):
        if board_row - 2 < 0 or board_column + 2 > 12:
            return False
        else:
            return self.board[board_row][board_column] == token \
                   and self.board[board_row][board_column + 2] == token \
                   and self.board[board_row - 2][board_column] == token \
                   and self.board[board_row - 1][board_column + 1] == token \
                   and self.board[board_row - 2][board_column + 2] == token \
                   and (self.board[board_row - 1][board_column] != opposing_token
                        or self.board[board_row - 1][board_column + 2] != opposing_token)

    '''
        Quadrant 2
            [X][ ][X][ ][ ]
            [ ][X][ ][ ][ ]
            [X][ ]['X'][ ][ ]
            [ ][ ][ ][ ][ ]
            [ ][ ][ ][ ][ ]
    '''

    def check_quadrant_2(self, board_row, board_column, token, opposing_token):
        if board_row - 2 < 0 or board_column - 2 < 1:
            return False
        else:
            return self.board[board_row][board_column] == token \
                   and self.board[board_row][board_column - 2] == token \
                   and self.board[board_row - 2][board_column] == token \
                   and self.board[board_row - 1][board_column - 1] == token \
                   and self.board[board_row - 2][board_column - 2] == token \
                   and (self.board[board_row - 1][board_column] != opposing_token
                        or self.board[board_row - 1][board_column - 2] != opposing_token)

    '''
        Quadrant 3
            [ ][ ][ ][ ][ ]
            [ ][ ][ ][ ][ ]
            [X][ ]['X'][ ][ ]
            [ ][X][ ][ ][ ]
            [X][ ][X][ ][ ]
    '''

    def check_quadrant_3(self, board_row, board_column, token, opposing_token):
        if board_row + 2 > 9 or board_column - 2 < 1:
            return False
        else:
            return self.board[board_row][board_column] == token \
                   and self.board[board_row][board_column - 2] == token \
                   and self.board[board_row + 2][board_column] == token \
                   and self.board[board_row + 1][board_column - 1] == token \
                   and self.board[board_row + 2][board_column - 2] == token \
                   and (self.board[board_row + 1][board_column] != opposing_token
                        or self.board[board_row + 1][board_column - 2] != opposing_token)

    '''
        Quadrant 4
            [ ][ ][ ][ ][ ]
            [ ][ ][ ][ ][ ]
            [ ][ ]['X'][ ][X]
            [ ][ ][ ][X][ ]
            [ ][ ][X][ ][X]
    '''

    def check_quadrant_4(self, board_row, board_column, token, opposing_token):
        if board_row + 2 > 9 or board_column + 2 > 12:
            return False
        else:
            return self.board[board_row][board_column] == token \
                   and self.board[board_row][board_column + 2] == token \
                   and self.board[board_row + 2][board_column] == token \
                   and self.board[board_row + 1][board_column + 1] == token \
                   and self.board[board_row + 2][board_column + 2] == token \
                   and (self.board[board_row + 1][board_column] != opposing_token
                        or self.board[board_row + 1][board_column + 2] != opposing_token)

    '''
        Quadrant 5
            [ ][ ][ ][ ][ ]
            [ ][X][ ][X][ ]
            [ ][ ]['X'][ ][ ]
            [ ][X][ ][X][ ]
            [ ][ ][ ][ ][ ]
    '''

    # 'quadrant 5' refers to the 'center' where the token is placed
    def check_quadrant_5(self, board_row, board_column, token, opposing_token):
        if board_row + 1 > 9 or board_column + 1 > 12 or board_row - 1 < 0 or board_column - 1 < 1:
            return False
        else:
            return self.board[board_row][board_column] == token \
                   and self.board[board_row - 1][board_column + 1] == token \
                   and self.board[board_row - 1][board_column - 1] == token \
                   and self.board[board_row + 1][board_column - 1] == token \
                   and self.board[board_row + 1][board_column + 1] == token \
                   and (self.board[board_row][board_column + 1] != opposing_token
                        or self.board[board_row][board_column - 1] != opposing_token)

    def is_move_possible(self, board_row, board_column, old_board_row, old_board_column):
        return old_board_row + 1 >= board_row >= old_board_row - 1 \
               and old_board_column + 1 >= board_column >= old_board_column - 1 \
               and 9 >= board_row >= 0 and 12 >= board_column >= 1 \
               and self.board[board_row][board_column] == ' '

    @staticmethod
    def is_placement_possible(board_row, board_column):
        return 9 >= board_row >= 0 and 12 >= board_column >= 1

    def is_player_winner(self, board_row, board_column, player_token, opposing_player_token):
        return self.check_quadrant_1(board_row, board_column, player_token, opposing_player_token) \
               or self.check_quadrant_2(board_row, board_column, player_token, opposing_player_token) \
               or self.check_quadrant_3(board_row, board_column, player_token, opposing_player_token) \
               or self.check_quadrant_4(board_row, board_column, player_token, opposing_player_token) \
               or self.check_quadrant_5(board_row, board_column, player_token, opposing_player_token)

    def winner_evaluation(self, board_row, board_column, board_old_row, board_old_column, is_turn_of_player_one):
        player_token = 'X' if is_turn_of_player_one else 'O'
        opposing_player_token = 'O' if is_turn_of_player_one else 'X'

        evaluated_winner = None

        if self.is_player_winner(board_row, board_column, player_token, opposing_player_token):
            evaluated_winner = 'Player 1' if is_turn_of_player_one else 'Player 2'

        if ((board_old_row - 1 >= 0 and self.board[board_old_row - 1, board_old_column] == opposing_player_token and
             self.is_player_winner(board_old_row - 1, board_old_column, opposing_player_token, player_token)) or
                (board_old_row + 1 <= 9 and self.board[board_old_row + 1, board_old_column] == opposing_player_token and
                 self.is_player_winner(board_old_row + 1, board_old_column, opposing_player_token, player_token))):
            evaluated_winner = 'Player 2' if is_turn_of_player_one else 'Player 1'

        return evaluated_winner


class PlayingGame:
    is_player_1_turn = True
    total_moves = 30
    winner = None
    player_1_token = 'X'
    player_2_token = 'O'

    def __init__(self, x_rudder: XRudder):
        self.x_rudder = x_rudder

    def turn_of_player(self, player_token, opposing_player_token):

        current_player_tokens = self.x_rudder.player_1_tokens if self.is_player_1_turn \
            else self.x_rudder.player_2_tokens

        print('===============================')
        print('===========' + ('Player 1' if self.is_player_1_turn else 'Player 2') + '============')
        print('===============================')
        print('========TOKEN REMAINING========')
        print('============= ' + str(current_player_tokens) + ' ==============')
        print('===============================')
        print('========MOVES REMAINING========')
        print('============= ' + str(self.total_moves) + ' ==============')
        print('===============================')
        print()
        print(self.x_rudder.board)
        print()

        position = input('Choose a position to move/place a token: ')
        row = self.x_rudder.true_row_position(int(position[1:3]))
        column = self.x_rudder.true_column_position(position[0].lower())

        old_row = -1
        old_column = -1

        if current_player_tokens != 0:
            while self.x_rudder.board[row, column] == opposing_player_token \
                    or not self.x_rudder.is_placement_possible(row, column):
                position = input('Choose another position to move/place the token: ')
                row = self.x_rudder.true_row_position(int(position[1:3]))
                column = self.x_rudder.true_column_position(position[0].lower())

            if self.x_rudder.board[row, column] == player_token:
                old_row = row
                old_column = column
                self.x_rudder.remove_token(row, column)

                position = input('Choose the position you want to move the token: ')
                row = self.x_rudder.true_row_position(int(position[1:3]))
                column = self.x_rudder.true_column_position(position[0].lower())

                while not self.x_rudder.is_move_possible(row, column, old_row, old_column):
                    position = input('Choose another position to move the token: ')
                    row = self.x_rudder.true_row_position(int(position[1:3]))
                    column = self.x_rudder.true_column_position(position[0].lower())
                self.total_moves -= 1

            else:
                if self.is_player_1_turn:
                    self.x_rudder.player_1_tokens -= 1
                else:
                    self.x_rudder.player_2_tokens -= 1
        else:
            while self.x_rudder.board[row, column] != player_token:
                position = input('Choose one of your tokens to move: ')
                row = self.x_rudder.true_row_position(int(position[1:3]))
                column = self.x_rudder.true_column_position(position[0].lower())

            old_row = row
            old_column = column
            self.x_rudder.remove_token(row, column)

            position = input('Choose the position you want to move the token: ')
            row = self.x_rudder.true_row_position(int(position[1:3]))
            column = self.x_rudder.true_column_position(position[0].lower())

            while not self.x_rudder.is_move_possible(row, column, old_row, old_column):
                position = input('Choose another position to move: ')
                row = self.x_rudder.true_row_position(int(position[1:3]))
                column = self.x_rudder.true_column_position(position[0].lower())
            self.total_moves -= 1

        self.x_rudder.placing_token(player_token, row, column)

        self.winner = self.x_rudder.winner_evaluation(row, column, old_row, old_column, self.is_player_1_turn)

        return self.winner

    # ==========================================GAME============================================

    def start(self):
        while (self.x_rudder.player_1_tokens != 0
               or self.x_rudder.player_2_tokens != 0 or self.total_moves != 0):

            self.is_player_1_turn = True
            if self.turn_of_player(self.player_1_token, self.player_2_token) is not None:
                break

            self.is_player_1_turn = False
            if self.turn_of_player(self.player_2_token, self.player_1_token) is not None:
                break

        print(self.x_rudder.board)

        if self.winner is not None:
            print(self.winner + ' is the Winner!!!')
        else:
            print('TIE!')


default_game = XRudder()
play = PlayingGame(default_game)
play.start()

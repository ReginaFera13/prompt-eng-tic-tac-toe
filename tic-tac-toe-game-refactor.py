import random

class Game:
    X = 'x'
    O = 'o'
    EMPTY = ''
    
    def __init__(self):
        self.board = self.create_board(3, 3)
        self.player_selection = self.set_x_or_o()
        self.player = self.player_char()
        self.computer = self.computer_char()
    
    
    def create_board(self, rows, cols, value=EMPTY):
        return [[value for _ in range(cols)] for _ in range(rows)]
    
    def set_x_or_o(self):
        return input('Choose x or o: ')
    
    def player_char(self):
        if self.player_selection == 'x':
            return Game.X
        elif self.player_selection == 'o':
            return Game.O
        
    def computer_char(self):
        if self.player_selection == 'x':
            return Game.O
        elif self.player_selection == 'o':
            return Game.X
    
    def display_board(self):
        for row in self.board:
            print(row)
    
    def player_move(self):
        (row, col) = int(input('Insert at which row: ')) - 1, int(input('Insert at which column: ')) - 1
        if self.board[row][col] == Game.X or self.board[row][col] == Game.O:
            print('Space already taken. Pick another space.')
            return self.player_move()
        elif self.board[row][col] == Game.EMPTY:
            self.board[row][col] = self.player
            return self.board
    
    def computer_move(self):
        (row, col) = random.randint(0, 2), random.randint(0, 2)
        if self.board[row][col] == Game.X or self.board[row][col] == Game.O:
            return self.computer_move()
        elif self.board[row][col] == Game.EMPTY:
                self.board[row][col] = self.computer
                return self.board
        
    def round_player_first(self):
        self.player_move()
        self.check_winner()
        self.is_board_full()
        self.computer_move()
        self.check_winner()
        self.is_board_full()
        self.display_board()
    
    def round_computer_first(self):
        self.computer_move()
        self.check_winner()
        self.is_board_full()
        self.player_move()
        self.check_winner()
        self.is_board_full()
        self.display_board()


    def goes_first(self):
        if self.player == Game.X:
           self.round_player_first()
        elif self.player == Game.O:
            self.round_computer_first()
    
    def check_winner(self):
        for i in range(3):
            # row
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != Game.EMPTY:
                return self.board[i][0]
            # column
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != Game.EMPTY:
                return self.board[0][i]
        # diagnals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != Game.EMPTY:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != Game.EMPTY:
            return self.board[0][2]
        else:
            return None
        
    def is_board_full(self):
        spaces_filled = 0
        for i, row in enumerate(self.board):
            for j, col in enumerate(self.board[i]):
                if col == Game.X or col == Game.O:
                    spaces_filled += 1
        return spaces_filled
    

    def tic_tac_toe(self):
        self.display_board()
        print('player selection:', self.player_selection)
        print('player character:', self.player)
        print('computer character:', self.computer)
        while self.is_board_full() < 9 and self.check_winner() is None:
            self.goes_first()
            
            winner = self.check_winner()
            if winner == self.player:
                print('PLAYER WINS!')
            elif winner == self.computer:
                print('COMPUTER WINS!')
            elif self.is_board_full() == 9:
                print('CATS GAME!')

game = Game()
game.tic_tac_toe()


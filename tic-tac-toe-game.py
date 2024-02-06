import random
X = 'x'
O = 'o'
EMPTY = ''

def create_board(rows, cols, value=EMPTY):
    return [[value for _ in range(cols)] for _ in range(rows)]

board = create_board(3, 3)

def display_board():
    for row in board:
        print(row)

def set_x_or_o():
    return input('Choose x or o: ')

player_selection = set_x_or_o()

def player_char():
    if player_selection == 'x':
        return X
    elif player_selection == 'o':
        return O
    
player = player_char()

def computer_char():
    if player_selection == 'x':
        return O
    elif player_selection == 'o':
        return X
    
computer = computer_char()

def player_move():
    (row, col) = int(input('Insert at which row: ')) - 1, int(input('Insert at which column: ')) - 1
    if board[row][col] == X or board[row][col] == O:
        print('Space already taken. Pick another space.')
        return player_move()
    elif board[row][col] == EMPTY:
        board[row][col] = player
        return board

def computer_move():
    (row, col) = random.randint(0, 2), random.randint(0, 2)
    if board[row][col] == X or board[row][col] == O:
        return computer_move()
    elif board[row][col] == EMPTY:
        board[row][col] = computer
        return board

def round_player_first():
    player_move()
    check_winner()
    is_board_full()
    computer_move()
    check_winner()
    is_board_full()
    display_board()
    
def round_computer_first():
    computer_move()
    check_winner()
    is_board_full()
    player_move()
    check_winner()
    is_board_full()
    display_board()

def goes_first():
    if player == X:
        round_player_first()
    elif player == O:
        round_computer_first()

def check_winner():
    for i in range(3):
        # row
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        # column
        elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    # diagnals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    else:
        return None

def is_board_full():
    spaces_filled = 0
    for i, row in enumerate(board):
        for j, col in enumerate(board[i]):
            if col == X or col == O:
                spaces_filled += 1
    return spaces_filled

def tic_tac_toe():
    display_board()
    print('player selection:', player_selection)
    print('player character:', player)
    print('computer character:', computer)
    while is_board_full() < 9 and check_winner() is None:
        goes_first()
        
        winner = check_winner()
        if winner == player:
            return 'PLAYER WINS!'
        elif winner == computer:
            return 'COMPUTER WINS!'
        elif is_board_full() == 9:
            return 'CATS GAME!'

print(tic_tac_toe())
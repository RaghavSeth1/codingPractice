import random
def player_input():
    marker = ''
    while marker not in ['O', 'X']:
        marker = input("Choose O/X:").upper()
        if marker not in ['O', 'X']:
            print("Sorry , Choose O/X")
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ''


def full_board_check(full_board_check):
    for i in range(0, 9):
        if space_check(board, i):
            return False
    return True  # Board Full


def player_choice(board):
    position = 0
    while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or not space_check(board, position):
        position = int(input("Pick a position('0','1','2','3','4','5','6','7','8'):"))

    return position


def display_board(game_list):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def find_winner(board, mark):
    return (board[0] == board[1] == board[2] == mark) or \
           (board[3] == board[4] == board[5] == mark) or \
           (board[6] == board[7] == board[8] == mark) or \
           (board[0] == board[3] == board[6] == mark) or \
           (board[1] == board[4] == board[7] == mark) or \
           (board[2] == board[5] == board[8] == mark) or \
           (board[0] == board[4] == board[8] == mark) or \
           (board[2] == board[4] == board[6] == mark)


def place_marker(board, marker, position):
    board[position] = marker


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe')
while True:
    board = [''] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' Will go first!')
    play_game = input("Ready to play y/n:")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            if find_winner(board, player1_marker):
                display_board(board)
                print('Player 1 Won')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Game tied!')
                    game_on = False

                else:
                    turn = 'Player 2'

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if find_winner(board, player2_marker):
                display_board(board)
                print('Player 2 Won')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Game tied!')

                    break
                else:
                    turn = 'Player 1'

    if not replay():
                break
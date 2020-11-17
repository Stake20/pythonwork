import re

board =["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

game_continuing = True
winner = None
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def start_game():

    display_board()

    while game_continuing:
        handle_turn(current_player)
        check_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Draw")


def handle_turn(player):

    print(player + "s turn.")
    position = input("Choose a block position (1-9): ")

    valid = False
    while not valid:
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while position not in numbers:
            position = input("Choose a block position (1-9): ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go Again.")

    board[position] = player
    display_board()

def check_game_over():
    check_win()
    check_draw()

def check_win():

    global  winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():

    global game_continuing

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[0] == board[1] == board[2] != "-"
    row3 = board[0] == board[1] == board[2] != "-"

    if row1 or row2 or row3:
        game_continuing = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():

    global game_continuing

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[7] == board[8] != "-"

    if column1 or column2 or column3:
        game_continuing = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]

    return

def check_diagonals():
    global game_continuing

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        game_continuing = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]

    return

def check_draw():
    global game_continuing
    if "-" not in board:
        game_continuing = False

    return

def flip_player():

    global  current_player

    if current_player == "X":
        current_player ="O"
    elif current_player =="O":
        current_player = "X"
    return


start_game()
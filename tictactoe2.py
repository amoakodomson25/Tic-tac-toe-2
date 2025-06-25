import random

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def print_board():

    print('|' + ' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('|' + ' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('|' + ' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')


def check_win(player):
    w = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
         (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
         (0, 4, 8), (2, 4, 6)]  # diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in w)


def get_available_moves():
    return [i for i in range(9) if board[i] not in ['X', 'O']]

def get_winning_moves(player):
    w = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
         (0, 3, 6), (1, 4, 7), (2, 5, 8),
         (0, 4, 8), (2, 4, 6)]
    winning_moves = []
    for a, b, c in w:
        line = [board[a], board[b], board[c]]
        if line.count(player) == 2 and any(board[i] not in ['X', 'O'] for i in (a, b, c)):
            for i in (a, b, c):
                if board[i] not in ['X', 'O']:
                    winning_moves.append(i)
    return winning_moves


turn = "X"  # You are X, CPU is O

for _ in range(9):
    print_board()
    if turn == "X":
        # Human turn
        while True:
            try:
                move = int(input("Your move (1–9): ")) - 1
                if move < 0 or move > 8:
                    print("Pick a spot from 1–9.")
                elif board[move] in ['X', 'O']:
                    print("That spot is already taken.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number (1–9).")
    else:
        # CPU turn
        print("CPU is thinking...")
        move = None
        winning = get_winning_moves("O")
        if winning:
            move = winning[0]
        else:
            # Block player win
            block = get_winning_moves("X")
            if block:
                move = block[0]
            else:
                # Pick random move
                move = random.choice(get_available_moves())

    board[move] = turn
    if check_win(turn):
        print_board()
        if turn == "X":
            print("You win!")
        else:
            print(" CPU wins!")
        break

    # Switch turn
    turn = "O" if turn == "X" else "X"

else:
    print_board()
    print("It's a tie!")

import numpy as np

input = []
with open("input.txt") as file:
    input = file.readlines()

winning_numbers = input[0].strip().split(',')

boards_amount = int((len(input) - 1) / 6)

boards = np.zeros((boards_amount, 5, 5))

board_num = 0
board_row = 0
for line_num in range(2, len(input)):
    if len(input[line_num]) < 14:
        board_num += 1
        board_row = 0
    else:
        row = list(filter(None, input[line_num].strip().split(' ')))
        for column in range(0, 5):
            boards[board_num][board_row][column] = row[column]
        board_row += 1

def check_board_for_win(board):
    for i in range(0, 5):
        if int(board[i][0]) == -1 and int(board[i][1]) == -1 and int(board[i][2]) == -1 and int(board[i][3]) == -1 and int(board[i][4]) == -1:
            return True
    for i in range(0, 5):
        if int(board[0][i]) == -1 and int(board[1][i]) == -1 and int(board[2][i]) == -1 and int(board[3][i]) == -1 and int(board[4][i]) == -1:
            return True
    return False

def mark_number_in_board(board, number):
    for i in range(0, 5):
        for j in range(0, 5):
            if int(board[i][j]) == int(number):
                board[i][j] = -1
    return board

def calc_score(board, number):
    score = int(0)
    for i in range(0, 5):
        for j in range(0, 5):
            if int(board[i][j]) != -1:
                score += int(board[i][j])
    score = int(score) * int(number)
    return score

has_won = []

for i in range(0, len(winning_numbers)):
    for j in range(0, boards_amount):
        boards[j] = mark_number_in_board(boards[j], winning_numbers[i])
        if check_board_for_win(boards[j]):
            if j not in has_won:
                has_won.append(j)
                print("Board", j, "in", i + 1, "turns. Last number was", winning_numbers[i])
                print("Score:", calc_score(boards[j], winning_numbers[i]))

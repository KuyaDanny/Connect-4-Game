import pygame
import numpy as np

ROWS = 6
COLUMNS = 7

pygame.init()
pygame.font.init()
pygame.display.set_caption('Connect 4')
#screen = pygame.display.set_mode((800, 700))

def game_board():
    board = np.zeros((ROWS,COLUMNS))
    return board

def place_choice(board, row, column, choice):
    board[row][column] = choice

def valid_choice(board, column):
    return board[5][column] == 0

def next_row(board, column):
    for i in range(ROWS):
        if board[i][column] == 0:
            return i

# checks for wins on board
def player_win(board, choice):
    # Vertical win checks
    for i in range(COLUMNS):
        for j in range(ROWS-3):
            if board[j][i] == choice and board[j+1][i] == choice and board[j+2][i] == choice and board[j+3][i] == choice:
                return True

    # Horizontal win checks
    for i in range(COLUMNS-3):
        for j in range(ROWS):
            if board[j][i] == choice and board[j][i+1] == choice and board[j][i+2] == choice and board[j][i+3] == choice:
                return True
    
    # Forward diagonal win checks
    for i in range(COLUMNS-3):
      for j in range(ROWS-3):
        if board[j][i] == choice and board[j+1][i+1] == choice and board[j+2][i+2] == choice and board[j+3][i+3] == choice:
          return True

    # Backward diagonal win checks
    for i in range(COLUMNS-3):
      for j in range(3, ROWS):
        if board[j][i] == choice and board[j-1][i+1] == choice and board[j-2][i+2] == choice and board[j-3][i+3] == choice:
          return True

# Flips board so choices appear at bottom instead of top
def reverse_board(board):
    print(np.flip(board, 0))

board = game_board()
reverse_board(board)
turn = 0
game_over = False

#Player turns

while not game_over:
    if turn == 0:
        column = int(input("Player 1 choose a column (0-6):"))
        if valid_choice(board, column):
            row = next_row(board, column)
            place_choice(board, row, column, 1)

            if player_win(board, 1):
                print("Player 1 wins")
                game_over = True
    else:
        column = int(input("Player 2 choose a column (0-6):"))
        if valid_choice(board, column):
            row = next_row(board, column)
            place_choice(board, row, column, 2)

            if player_win(board, 2):
                print("Player 2 wins")
                game_over = True

    # Alternates player turns
    reverse_board(board)
    turn += 1
    turn = turn % 2

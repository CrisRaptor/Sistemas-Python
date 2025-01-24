import random
import os
import time

def create_board(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_board(board):
    for row in board:
        print(' '.join(['*' if cell else ' ' for cell in row]))
    print()

def count_alive_neighbors(board, row, col):
    rows, cols = len(board), len(board[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            count += board[r][c]
    return count

def next_generation(board):
    rows, cols = len(board), len(board[0])
    new_board = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            alive_neighbors = count_alive_neighbors(board, row, col)
            if board[row][col] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_board[row][col] = 0
                else:
                    new_board[row][col] = 1
            else:
                if alive_neighbors == 3:
                    new_board[row][col] = 1
    return new_board


rows, cols = 10, 10
board = create_board(rows, cols)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(board)
    choice = input("Press Enter to continue or type 'q' to quit: ")
    if choice.lower() == 'q':
        break
    board = next_generation(board)
    time.sleep(1)

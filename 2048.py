import random
import numpy as np


def start_game():
    matrix = np.zeros((4, 4))

    print("Commands are as follows:")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    add_new_2(matrix)
    add_new_2(matrix)

    print(matrix)

    game_active = True
    while game_active:
        user_input = input("Enter your move (W, A, S, D): ").strip().upper()
        if user_input in ["W", "A", "S", "D"]:
            if user_input == "W":
                matrix, changed = move_up(matrix)
            elif user_input == "A":
                matrix, changed = move_left(matrix)
            elif user_input == "S":
                matrix, changed = move_down(matrix)
            elif user_input == "D":
                matrix, changed = move_right(matrix)

            if changed:
                add_new_2(matrix)

            game_active = not check_game_over(matrix)
            print(matrix)
        else:
            print("Invalid Input! Use W, A, S, D.")

    print("Game Over!")


def add_new_2(matrix):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if matrix[i][j] == 0]
    if empty_cells:
        row, column = random.choice(empty_cells)
        matrix[row][column] = 2


def check_game_over(matrix):
    if any(2048 in row for row in matrix):
        return True

    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return False
            if i < 3 and matrix[i][j] == matrix[i + 1][j]:
                return False
            if j < 3 and matrix[i][j] == matrix[i][j + 1]:
                return False

    return True


def compress(matrix):
    new_matrix = np.zeros((4, 4))
    for i in range(4):
        pos = 0
        for j in range(4):
            if matrix[i][j] != 0:
                new_matrix[i][pos] = matrix[i][j]
                pos += 1
    return new_matrix


def merge(matrix):
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                matrix[i][j] *= 2
                matrix[i][j + 1] = 0
    return matrix


def reverse(matrix):
    new_matrix = np.zeros((4, 4))
    for i in range(4):
        new_matrix[i] = matrix[i][::-1]
    return new_matrix


def transpose(matrix):
    return np.transpose(matrix)


def move_left(matrix):
    new_matrix = compress(matrix)
    new_matrix = merge(new_matrix)
    new_matrix = compress(new_matrix)
    return new_matrix, not np.array_equal(matrix, new_matrix)


def move_right(matrix):
    new_matrix = reverse(matrix)
    new_matrix, changed = move_left(new_matrix)
    new_matrix = reverse(new_matrix)
    return new_matrix, changed


def move_up(matrix):
    new_matrix = transpose(matrix)
    new_matrix, changed = move_left(new_matrix)
    new_matrix = transpose(new_matrix)
    return new_matrix, changed


def move_down(matrix):
    new_matrix = transpose(matrix)
    new_matrix, changed = move_right(new_matrix)
    new_matrix = transpose(new_matrix)
    return new_matrix, changed


start_game()

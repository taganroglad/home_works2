from task3 import check_queens
import random

def generate_random_queens():
    queens_positions = []
    for _ in range(8):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        queens_positions.append((x, y))
    return queens_positions

def check_and_print_successful_arrangements():
    successful_arrangements = 0
    while successful_arrangements < 4:
        queens_positions = generate_random_queens()
        if check_queens(queens_positions):
            print("Successful arrangement:")
            for row in range(1, 9):
                line = ""
                for col in range(1, 9):
                    if (row, col) in queens_positions:
                        line += "Q "
                    else:
                        line += ". "
                print(line)
            print()
            successful_arrangements += 1

check_and_print_successful_arrangements()

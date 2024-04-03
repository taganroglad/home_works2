def check_queens(queens_positions):
    for i in range(len(queens_positions)):
        for j in range(i+1, len(queens_positions)):
            if queens_positions[i][0] == queens_positions[j][0] or queens_positions[i][1] == queens_positions[j][1] or abs(queens_positions[i][0] - queens_positions[j][0]) == abs(queens_positions[i][1] - queens_positions[j][1]):
                return False
    return True
# Как вариант:
print(check_queens([(1, 6), (3, 2), (5, 4), (7, 8), (2, 5), (4, 7), (6, 1), (8, 3)]))

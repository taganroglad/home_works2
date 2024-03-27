def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    return transposed

matrix = [
    [1, 10, 20],
    [5, 15, 25]
]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)

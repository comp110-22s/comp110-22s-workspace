"""Finds the determinant of a square matrix."""

from copy import deepcopy


def smaller_matrix(original_matrix, row, column):
    # so the new matrix does not affect the original matrix
    new_matrix = deepcopy(original_matrix)
    # the indices to do the removal depend on the original matrix
    new_matrix.remove(original_matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].remove(new_matrix[i][column])
    return new_matrix


def determinant(matrix):
    num_rows = len(matrix)
    # makes sure the matrix is square
    for row in matrix:
        if len(row) != num_rows:
            print("Not a square matrix.")
            return
    # base case that returns a simple determinatrix
    if len(matrix) == 2:
        simp_d = matrix[0][0] * \
            matrix[1][1] - \
            matrix[1][0] * \
            matrix[0][1]
        return simp_d
    else:
        # cofactor expansion
        answer = 0
        num_columns = num_rows
        for i in range(num_columns):
            cofactor = (-1) ** i * matrix[0][i] \
                * determinant(smaller_matrix(matrix, 0, i))
            answer += cofactor
        return answer


# looks like:
# [5 9]
# [6]
# [1, 4]
matrix_1 = [[5, 9], [6], [1, 4]]
print(determinant(matrix_1))

# looks like:
# [5 2]
# [3 6]
matrix_2 = [[5, 2], [3, 6]]
print(determinant(matrix_2))

# looks like:
# [2 3 7 1]
# [7 1 9 8]
# [8 6 1 4]
# [0 1 4 2]
matrix_3 = [[2, 3, 7, 1], [7, 1, 9, 8], [8, 6, 1, 4], [0, 1, 4, 2]]
print(determinant(matrix_3))
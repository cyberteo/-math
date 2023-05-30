# Take the matrix size as input from the user as an integer.
size = int(input("Enter the matrix size: "))

# Take the matrix elements one by one from the user.
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        element = int(input("Enter the element at row {}, column {}: ".format(i+1, j+1)))
        row.append(element)
    matrix.append(row)

# Calculate the determinant of the matrix based on the user's input.
def calculate_determinant(matrix):
    # If the user enters a 1x1 matrix, it will work.
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        # If the user enters a 2x2 matrix, it will work.
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        # If the user enters a 3x3 or larger matrix, it will work. It is recommended to use a 3x3 matrix for the calculations.
        for j in range(len(matrix)):
            sub_matrix = []
            for i in range(1, len(matrix)):
                sub_matrix_row = []
                for k in range(len(matrix)):
                    if k != j:
                        sub_matrix_row.append(matrix[i][k])
                sub_matrix.append(sub_matrix_row)
            det += matrix[0][j] * (-1) ** j * calculate_determinant(sub_matrix)
        return det

# Calculate the determinant of the matrix when running this function.
determinant = calculate_determinant(matrix)

# Print the result to the screen.
print("____result____")
print("Matrix:\n", matrix)
print("Determinant:", determinant)
print("Matrix size:", size, "x", size)

# This code allows us to calculate the determinant of a matrix. In short, it provides a way to calculate the determinant without using the NumPy library.

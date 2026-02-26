def straight_gauss_method(n, matrixAb):
    swap_count = 0  

    for k in range(n - 1):

        
        max_row = k
        max_value = abs(matrixAb[k][k])

        for i in range(k + 1, n):
            if abs(matrixAb[i][k]) > max_value:
                max_value = abs(matrixAb[i][k])
                max_row = i

        
        if max_value == 0:
            return None, None

        if max_row != k:
            matrixAb[k], matrixAb[max_row] = matrixAb[max_row], matrixAb[k]
            swap_count += 1

        
        for i in range(k + 1, n):
            m = matrixAb[i][k] / matrixAb[k][k]
            for j in range(k, n + 1):
                matrixAb[i][j] -= m * matrixAb[k][j]

    return matrixAb, swap_count

def calculate_determinant(n, triangular_matrix, swap_count):
    det = 1
    for i in range(n):
        det *= triangular_matrix[i][i]

    if swap_count % 2 == 1:
        det = -det

    return det

def gay_gauss_method(n, triangular_matrix):
    X = [0] * n
    for i in range(n-1, -1, -1):
        s = triangular_matrix[i][n]  
        for j in range(i+1, n):
            s -= triangular_matrix[i][j] * X[j]
        X[i] = s / triangular_matrix[i][i]
    
    return X

def calculate_residual_vector(n, original_matrix, solution):
   
    residual = [0] * n
    
    for i in range(n):
        s = 0
        for j in range(n):
            s += original_matrix[i][j] * solution[j]
        

        residual[i] = original_matrix[i][n] - s
    
    return residual

def solve_system(n, matrix):

    matrix_copy = [row[:] for row in matrix]

    triangular_matrix, swap_count = straight_gauss_method(n, matrix_copy)

    if triangular_matrix is None:
        print("Matrix is singular. No unique solution.")
        return None, None, None, None

    det = calculate_determinant(n, triangular_matrix, swap_count)

    if abs(det) == 0:
        print("Determinant is zero. No unique solution.")
        return triangular_matrix, None, det, None

    solution = gay_gauss_method(n, triangular_matrix)
    residual = calculate_residual_vector(n, matrix, solution)

    return triangular_matrix, solution, det, residual
import numpy as np
from Gauss_Solver import solve_system
from Matrix_input import matrix_input


def print_matrix(matrix):
    print("\nTriangular matrix (including column B):")
    for row in matrix:
        print(" ".join(f"{elem:10.5f}" for elem in row))


def main():
    
    n, matrix = matrix_input()

    print("\nOriginal matrix:")
    for row in matrix:
        print(row)

   
    triangular_matrix, solution, det, residual = solve_system(n, matrix)

    if triangular_matrix is None:
        return

    print_matrix(triangular_matrix)

    
    print(f"\nDeterminant (Gauss method) {det}:")
    if solution is None:
        print("\nSystem has no unique solution (determinant is zero).")
        return
    
    print("\nSolution vector:")
    for i, x in enumerate(solution):
        print(f"x{i+1} = {x}")


    print("\nResidual vector:")
    for i, r in enumerate(residual):
        print(f"r{i+1} = {r}")

    print("\n NumPy solution")

    A = np.array([row[:n] for row in matrix], dtype=float)
    B = np.array([row[n] for row in matrix], dtype=float)

    try:
        np_solution = np.linalg.solve(A, B)
        np_det = np.linalg.det(A)

        print("\nNumPy determinant:", np_det)

        print("\nNumPy solution vector:")
        for i, x in enumerate(np_solution):
            print(f"x{i+1} = {x}")

        
        print("\nDifference between solutions:")
        for i in range(n):
            print(f"|x{i+1}_gauss - x{i+1}_numpy| = {abs(solution[i] - np_solution[i])}")

        print("\nDifference between determinants:")
        print(f"|det_gauss - det_numpy| = {abs(det - np_det)}")

    except np.linalg.LinAlgError:
        print("Matrix is singular (NumPy). No unique solution.")


if __name__ == "__main__":
    main()
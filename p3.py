#Write a program to multiply two matrices using the Strassen’s algorithm for matrix
#multiplication.
import numpy as np

def strassen_multiply(A, B):
    n = A.shape[0]
    
    # Base case when matrix is 1x1
    if n == 1:
        return A * B

    # Splitting the matrices into quadrants
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Strassen's formulas
    M1 = strassen_multiply(A11 + A22, B11 + B22)
    M2 = strassen_multiply(A21 + A22, B11)
    M3 = strassen_multiply(A11, B12 - B22)
    M4 = strassen_multiply(A22, B21 - B11)
    M5 = strassen_multiply(A11 + A12, B22)
    M6 = strassen_multiply(A21 - A11, B11 + B12)
    M7 = strassen_multiply(A12 - A22, B21 + B22)

    # Calculating the quadrants of the result matrix C
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combining the quadrants into a single matrix
    C = np.zeros((n, n))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C

def strassen_algorithm(A, B):
    assert A.shape == B.shape
    assert len(A.shape) == 2
    assert A.shape[0] == A.shape[1]

    n = A.shape[0]
    
    # Making the matrices size a power of 2 by padding with zeros
    m = 1
    while m < n:
        m *= 2
    if m != n:
        A_padded = np.zeros((m, m))
        B_padded = np.zeros((m, m))
        A_padded[:n, :n] = A
        B_padded[:n, :n] = B
        C_padded = strassen_multiply(A_padded, B_padded)
        return C_padded[:n, :n]
    else:
        return strassen_multiply(A, B)

# Example usage
if __name__ == "__main__":
    A = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

    B = np.array([[16, 15, 14, 13],
                  [12, 11, 10, 9],
                  [8, 7, 6, 5],
                  [4, 3, 2, 1]])

    C = strassen_algorithm(A, B)
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Matrix C (Result of A * B):")
    print(C)

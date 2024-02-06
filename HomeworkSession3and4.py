import numpy as np

print("Homework after sessions 3 and 4")
print("Linear algebra with python:")

A = np.array([[3, 7, 5], [2, 5, 4], [3, 5, 9]])
B = A.T
print(f"Matrix A: {A.shape} {A.shape[0]} rows and {A.shape[1]} columns")
print(A)
print(f"Matrix B: {B.shape} {B.shape[0]} rows and {B.shape[1]} columns")
print(B)
print("Matrix B is now matrix A transposed, but what happens if we transpose B?")
print(B.T)
print("We return to Matrix A!")

print("Now lets look at a property of matrix A and its inverse: ")
print("Inverse matrix of A: ")
InverseA = np.linalg.inv(A)
print(InverseA)
print("The multiplication of a matrix and its inverse should return the identity matrix I.")
print(np.identity(3))
print("Matrices A and InverseA multiplied: ")
print((A@InverseA).round(10))
print("The matrices A and InverseA are in fact inverses of each other!")

import numpy as numpy

def input_matrix(name):

    rows = int(input(f"Enter number of rows for Matrix {name}: "))

    cols = int(input(f"Enter number of columns for Matrix {name}: "))

    print(f"\nEnter elements of Matrix {name} row by row:")

    matrix = []

    for i in range(rows):

        row = list(map(float, input(f"Row {i+1}: ").split()))

        matrix.append(row)

    return numpy.array(matrix)

while True:

    print("\n========== MATRIX OPERATIONS TOOL ==========")

    print("1. Matrix Addition")

    print("2. Matrix Subtraction")

    print("3. Matrix Multiplication")

    print("4. Matrix Transpose")

    print("5. Matrix Determinant")

    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        A = input_matrix("A")

        B = input_matrix("B")

        if A.shape == B.shape:

            print("\nResult:")

            print(A + B)

        else:

            print("\nError: Matrices must have the same dimensions.")

    elif choice == "2":

        A = input_matrix("A")

        B = input_matrix("B")

        if A.shape == B.shape:

            print("\nResult:")

            print(A - B)

        else:

            print("\nError: Matrices must have the same dimensions.")

    elif choice == "3":

        A = input_matrix("A")

        B = input_matrix("B")

        if A.shape[1] == B.shape[0]:

            print("\nResult:")

            print(numpy.matmul(A, B))

        else:

            print("\nError: Columns of Matrix A must equal Rows of Matrix B.")

    elif choice == "4":

        A = input_matrix("A")

        print("\nTranspose:")

        print(A.T)

    elif choice == "5":

        A = input_matrix("A")

        if A.shape[0] == A.shape[1]:

            print("\nDeterminant:")

            print(numpy.linalg.det(A))

        else:

            print("\nError: Determinant can only be calculated for square matrices.")

    elif choice == "6":

        print("\nThank you for using Matrix Operations Tool!")

        break

    else:

        print("\nInvalid Choice! Please try again.")
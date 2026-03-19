import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements of {name} row-wise:")
    
    elements = []
    for i in range(rows):
        row = [int(x) for x in input().split()]
        if len(row) != cols:
            print("Number of elements doesn't match columns! Try again.")
            return input_matrix(name)
        elements.append(row)
    return np.array(elements)

def menu():
    print("\n--- Matrix Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    
    if choice == "5":
        print("Exiting...")
        break
    

    if choice in ["1","2","3"]:
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
    
        if choice == "1":
            if A.shape == B.shape:
                print("Result:\n", A + B)
            else:
                print("Matrices must have same shape!")

        elif choice == "2":
            if A.shape == B.shape:
                print("Result:\n", A - B)
            else:
                print("Matrices must have same shape!")
                
        elif choice == "3":
            if A.shape[1] == B.shape[0]:
                print("Result:\n", np.dot(A, B))
            else:
                print("Columns of A must be equal to Rows of B!")
    

    elif choice == "4":
        A = input_matrix("Matrix")
        print("Transpose:\n", np.transpose(A))
    
    else:
        print("Invalid choice!")
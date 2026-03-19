# 🧮 Matrix Calculator (Python + NumPy)

A simple command-line **Matrix Calculator** built using Python and NumPy. Perform basic matrix operations like addition, subtraction, multiplication, and transpose interactively.

---

## 🎯 Features

- Menu-driven interface for easy operation selection
- Input validation to ensure proper matrix dimensions
- Supports operations:
  - Addition (A + B)
  - Subtraction (A - B)
  - Multiplication (A × B)
  - Transpose (Aᵀ)
- Works with matrices of any size (as long as dimensions are compatible)
- Continuous loop until the user chooses to exit

---

## 🧠 Concepts Used

- Python functions, loops, and conditional statements
- User input handling and validation
- NumPy arrays for matrix representation
- Matrix operations using NumPy: addition, subtraction, dot product, transpose
- Error handling for invalid dimensions or operations

---

## 💻 How to Use

1. Run the script in a Python environment (Python 3.x recommended)
2. Choose an operation from the menu:


Addition

Subtraction

Multiplication

Transpose

Exit


3. Enter the required matrix dimensions and elements as prompted
4. View the result instantly in the console
5. Repeat or exit by selecting option 5

---

## 🛠 Example


--- Matrix Calculator ---

Addition

Subtraction

Multiplication

Transpose

Exit
Enter your choice: 1

Enter number of rows for Matrix A: 2
Enter number of columns for Matrix A: 2
Enter elements of Matrix A row-wise:
1 2
3 4

Enter number of rows for Matrix B: 2
Enter number of columns for Matrix B: 2
Enter elements of Matrix B row-wise:
5 6
7 8

Result:
[[ 6 8]
[10 12]]


---

## ⚡ Requirements

- Python 3.x
- NumPy (`pip install numpy`)

---

## 📂 File Structure
```
matrix_calculator/
│
├─ matrix_calculator.py   # Main script
└─ README.md             # Project documentation
```
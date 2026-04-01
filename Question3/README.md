# Sudoku Solver using CSP (Constraint Satisfaction Problem)

## 📌 Problem Description

Sudoku is a popular number puzzle played on a 9×9 grid. The objective is to fill the grid such that every row, every column, and each 3×3 subgrid contains all digits from 1 to 9 without repetition.

In this project, Sudoku is solved using the concept of **Constraint Satisfaction Problem (CSP)** with a backtracking approach.

---

## 🧠 CSP Formulation

### Variables:

Each empty cell in the Sudoku grid is considered a variable.

### Domain:

Each variable can take values from:
{1, 2, 3, 4, 5, 6, 7, 8, 9}

### Constraints:

1. Each number must appear only once in a row.
2. Each number must appear only once in a column.
3. Each number must appear only once in a 3×3 subgrid.

---

## 🔢 Sudoku Grid Example

Initial Puzzle:

5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
---------------------

8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
---------------------

0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9

(0 represents empty cells)

---

## ⚙️ Algorithm Used

### Backtracking Algorithm:

1. Find an empty cell in the grid.
2. Try placing digits (1–9) in the cell.
3. Check if the assignment satisfies all constraints.
4. If valid, move to the next empty cell.
5. If no valid number exists, backtrack to the previous cell.
6. Repeat until the grid is completely filled.

---

## 💻 How to Run the Program

1. Save the Python file as:
   sudoku.py

2. Open terminal in the file directory.

3. Run the program:
   python sudoku.py

---

## 📌 Sample Output

Solved Sudoku:

5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------

8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------

9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9

---

## 📚 Conclusion

This project demonstrates how Sudoku can be modeled and solved as a Constraint Satisfaction Problem. The backtracking approach efficiently explores possible solutions while ensuring all constraints are satisfied.

---

## 🚀 Key Concepts

* Constraint Satisfaction Problem (CSP)
* Backtracking Algorithm
* Recursion
* Constraint Checking

---

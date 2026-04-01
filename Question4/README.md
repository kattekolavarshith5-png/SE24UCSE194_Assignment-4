# Cryptarithmetic Puzzle using CSP (SEND + MORE = MONEY)

## 📌 Problem Description

Cryptarithmetic (or crypt-analysis) puzzles are mathematical problems where digits are replaced by letters. The objective is to find the correct digit for each letter such that the arithmetic equation holds true.

In this project, we solve the classic puzzle:

SEND + MORE = MONEY

using the concept of **Constraint Satisfaction Problem (CSP)**.

---

## 🧠 CSP Formulation

### Variables:

S, E, N, D, M, O, R, Y

### Domain:

Digits {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

### Constraints:

1. Each letter must be assigned a unique digit.
2. Leading digits cannot be zero:

   * S ≠ 0
   * M ≠ 0
3. The arithmetic constraint must be satisfied:
   SEND + MORE = MONEY

---

## 🔢 Puzzle Representation

```
  S E N D
+ M O R E
-----------
M O N E Y
```

---

## ⚙️ Algorithm Used

### Backtracking (Generate and Test):

1. Assign digits to letters from the domain.
2. Ensure all digits are unique.
3. Check leading digit constraints.
4. Verify if the arithmetic equation holds.
5. If constraints fail, backtrack and try another assignment.
6. Continue until a valid solution is found.

---

## 💻 How to Run the Program

1. Save the Python file as:
   crypt.py

2. Open terminal in the file directory.

3. Run the program:
   python crypt.py

---

## 📌 Sample Output

Solution Found:

SEND  = 9567
MORE  = 1085
MONEY = 10652

Mapping:
S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2

---

## 📚 Conclusion

This project demonstrates how CSP can be applied to solve cryptarithmetic puzzles. The backtracking approach systematically explores possible assignments while ensuring all constraints are satisfied.

---

## 🚀 Key Concepts

* Constraint Satisfaction Problem (CSP)
* Backtracking Algorithm
* Permutations and Combinations
* Artificial Intelligence

---

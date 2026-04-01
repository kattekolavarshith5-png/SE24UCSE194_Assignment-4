# Map Coloring Problem using CSP (Australia)

## 📌 Problem Description

The Map Coloring problem is a classic example of a Constraint Satisfaction Problem (CSP) in Artificial Intelligence. The goal is to assign colors to different regions of a map such that no two adjacent regions share the same color.

In this project, we apply CSP to color the seven principal states and territories of Australia:

* WA (Western Australia)
* NT (Northern Territory)
* Queensland (Q)
* SA (South Australia)
* NSW (New South Wales)
* V (Victoria)
* T (Tasmania)

---

## 🧠 CSP Formulation

### Variables:

Each region is considered a variable:
WA, NT, Q, SA, NSW, V, T

### Domain:

Each region can take one of the following colors:
{Red, Green, Blue}

### Constraints:

* No two adjacent regions can have the same color.
* Tasmania (T) has no neighboring regions.

---

## 🔗 Adjacency (Neighbors)

* WA → NT, SA
* NT → WA, SA, Q
* Q → NT, SA, NSW
* SA → WA, NT, Q, NSW, V
* NSW → Q, SA, V
* V → SA, NSW
* T → (no neighbors)

---

## ⚙️ Algorithm Used

Backtracking is used to solve the CSP:

1. Select an unassigned region.
2. Assign a color from the domain.
3. Check constraints with neighboring regions.
4. If valid, proceed; otherwise, backtrack.
5. Repeat until all regions are assigned.

---

## 💻 How to Run the Program

1. Save the Python file as:
   map_coloring.py

2. Open terminal in the file directory.

3. Run the program:
   python map_coloring.py

---

## 📌 Sample Output

Example valid coloring:

WA  -> Red
NT  -> Green
Q   -> Red
SA  -> Blue
NSW -> Green
V   -> Red
T   -> Red

(Note: Output may vary as multiple valid solutions exist.)

---

## 📚 Conclusion

This implementation demonstrates how CSP can be used to solve real-world problems like map coloring. The backtracking approach ensures that all constraints are satisfied while exploring possible solutions efficiently.

---



---

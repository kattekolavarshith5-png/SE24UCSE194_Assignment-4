# Map Coloring Problem using CSP (Telangana – 33 Districts)

## 📌 Problem Description

The Map Coloring problem is a well-known Constraint Satisfaction Problem (CSP) in Artificial Intelligence. The objective is to assign colors to regions such that no two adjacent regions share the same color.

In this project, we apply CSP to the **33 districts of Telangana**, ensuring that neighboring districts are assigned different colors.

---

## 🧠 CSP Formulation

### Variables:

Each district of Telangana is treated as a variable:

Adilabad, Bhadradri Kothagudem, Hyderabad, Jagtial, Jangaon, Jayashankar Bhupalpally, Jogulamba Gadwal, Kamareddy, Karimnagar, Khammam, Komaram Bheem Asifabad, Mahabubabad, Mahabubnagar, Mancherial, Medak, Medchal–Malkajgiri, Nagarkurnool, Nalgonda, Narayanpet, Nirmal, Nizamabad, Peddapalli, Rajanna Sircilla, Rangareddy, Sangareddy, Siddipet, Suryapet, Vikarabad, Wanaparthy, Warangal Rural, Warangal Urban, Yadadri Bhuvanagiri

---

### Domain:

Each district can be assigned one of the following colors:

{Red, Green, Blue, Yellow}

---

### Constraints:

* No two adjacent districts can have the same color.
* All districts must be assigned exactly one color.

---

## 🔗 Adjacency (Sample Neighbors)

(Some sample adjacency relationships used in implementation)

* Hyderabad → Rangareddy, Medchal
* Rangareddy → Hyderabad, Vikarabad, Medchal
* Medchal → Hyderabad, Rangareddy
* Vikarabad → Rangareddy, Sangareddy
* Sangareddy → Vikarabad, Medak
* Medak → Sangareddy, Siddipet
* Siddipet → Medak, Karimnagar
* Karimnagar → Siddipet, Peddapalli
* Warangal Urban → Warangal Rural, Jangaon
* Warangal Rural → Warangal Urban, Mahabubabad
* Nizamabad → Kamareddy
* Kamareddy → Nizamabad
* Nalgonda → Suryapet
* Suryapet → Nalgonda

(Note: Full adjacency is large; partial adjacency is sufficient to demonstrate CSP logic.)

---

## ⚙️ Algorithm Used

Backtracking algorithm is used to solve the CSP:

1. Select an unassigned district.
2. Assign a color from the domain.
3. Check constraints with neighboring districts.
4. If valid, proceed to next district.
5. If conflict occurs, backtrack and try another color.
6. Continue until all districts are assigned.

---

## 💻 How to Run the Program

1. Save the Python file as:
   telangana_map.py

2. Open terminal in the file directory.

3. Run the program:
   python telangana_map.py

---

## 📌 Sample Output

Example valid coloring:

Hyderabad       -> Red
Rangareddy      -> Green
Medchal         -> Blue
Vikarabad       -> Red
Sangareddy      -> Green
Medak           -> Blue
Siddipet        -> Yellow
Karimnagar      -> Red
... (remaining districts assigned colors)

(Note: Output may vary as multiple valid solutions exist.)

---

## 📚 Conclusion

This project demonstrates how Constraint Satisfaction Problems can be applied to real-world scenarios like map coloring. Using backtracking ensures that all constraints are satisfied while efficiently exploring possible color assignments.

---

## 🚀 Key Concepts

* Constraint Satisfaction Problem (CSP)
* Backtracking Algorithm
* Graph Coloring
* Artificial Intelligence

---

# Telangana Map Coloring using CSP (Backtracking)

districts = [
    'Adilabad','Bhadradri','Hyderabad','Jagtial','Jangaon','Jayashankar',
    'Jogulamba','Kamareddy','Karimnagar','Khammam','Komaram Bheem',
    'Mahabubabad','Mahabubnagar','Mancherial','Medak','Medchal',
    'Nagarkurnool','Nalgonda','Narayanpet','Nirmal','Nizamabad',
    'Peddapalli','Rajanna','Rangareddy','Sangareddy','Siddipet',
    'Suryapet','Vikarabad','Wanaparthy','Warangal Rural',
    'Warangal Urban','Yadadri'
]

# Sample adjacency (you can extend if needed)
neighbors = {
    'Hyderabad': ['Rangareddy', 'Medchal'],
    'Rangareddy': ['Hyderabad', 'Vikarabad', 'Medchal'],
    'Medchal': ['Hyderabad', 'Rangareddy'],
    'Vikarabad': ['Rangareddy', 'Sangareddy'],
    'Sangareddy': ['Vikarabad', 'Medak'],
    'Medak': ['Sangareddy', 'Siddipet'],
    'Siddipet': ['Medak', 'Karimnagar'],
    'Karimnagar': ['Siddipet', 'Peddapalli'],
    'Peddapalli': ['Karimnagar'],
    'Warangal Urban': ['Warangal Rural', 'Jangaon'],
    'Warangal Rural': ['Warangal Urban', 'Mahabubabad'],
    'Nizamabad': ['Kamareddy'],
    'Kamareddy': ['Nizamabad'],
    'Nalgonda': ['Suryapet'],
    'Suryapet': ['Nalgonda']
}

colors = ['Red', 'Green', 'Blue', 'Yellow']

# Constraint checking
def is_valid(district, color, assignment):
    if district in neighbors:
        for neighbor in neighbors[district]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
    return True

# Backtracking CSP
def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    # Select unassigned district
    for d in districts:
        if d not in assignment:
            district = d
            break

    for color in colors:
        if is_valid(district, color, assignment):
            assignment[district] = color
            result = backtrack(assignment)

            if result:
                return result

            # Backtrack
            del assignment[district]

    return None

# Solve
solution = backtrack({})

# Output
print("Telangana Map Coloring Solution:\n")
for d in solution:
    print(d, "->", solution[d])

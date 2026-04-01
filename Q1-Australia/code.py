# Map Coloring for Australia using CSP (Backtracking)

regions = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

# Adjacency (neighbors)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []   # Tasmania has no neighbors
}

colors = ['Red', 'Green', 'Blue']

# Check constraints
def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm
def backtrack(assignment):
    # If all regions are assigned
    if len(assignment) == len(regions):
        return assignment

    # Select unassigned region
    for region in regions:
        if region not in assignment:
            break

    # Try colors
    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)

            if result:
                return result

            # Backtrack
            del assignment[region]

    return None

# Solve
solution = backtrack({})

# Output
print("Map Coloring Solution (Australia):")
for region in solution:
    print(region, "->", solution[region])

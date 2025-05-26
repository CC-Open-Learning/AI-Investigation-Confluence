elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

# Sort by number and name
elements.sort(key=lambda e: (e[1], e[2]))
print("Sorted by number and name:", elements)

# Sort by name (case-insensitive) and then by number
elements.sort(key=lambda e: (e[2].lower(), e[1]))
print("Sorted by name and number:", elements)

# Lambda for area calculation
area = lambda b, h: 0.5 * b * h
print("Area of triangle (base=6, height=5):", area(6, 5))

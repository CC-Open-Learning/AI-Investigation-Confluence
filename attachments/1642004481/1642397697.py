def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

print("Factorial of 5:", factorial(5))

def indented_list_sort(indented_list, indent="    "):
    KEY, ITEM, CHILDREN = range(3)

    def add_entry(level, key, item, children):
        children.append((level, key, item, []))

    def update_indented_list(entry):
        level, key, item, children = entry
        indented_list.append(indent * level + item)
        for child in sorted(children):
            update_indented_list(child)

    entries = []
    for item in indented_list:
        level = 0
        i = 0
        while item.startswith(indent, i):
            i += len(indent)
            level += 1
        key = item.strip().lower()
        add_entry(level, key, item, entries)

    indented_list = []
    for entry in sorted(entries):
        update_indented_list(entry)
    return indented_list

before = ["Nonmetals", " Hydrogen", " Carbon", " Nitrogen", " Oxygen", 
          "Inner Transitionals", " Lanthanides", " Cerium", " Europium", 
          " Actinides", " Uranium", " Curium", " Plutonium", "Alkali Metals", 
          " Lithium", " Sodium", " Potassium"]

after = indented_list_sort(before)
print("Sorted Indented List:", after)

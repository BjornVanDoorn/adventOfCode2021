
file = open('./input.txt')
content = file.read()
depths = content.splitlines()

print(len(depths))

# depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def changed_depth(depths):
    results = 0
    changes = len(depths)
    for i in range(0, changes):
        current_value = depths[i]
        previous_value = depths[i - 1]
        if i == 0:
            print(str(current_value) + " (N/A - no previous measurement)")
        elif current_value > previous_value:
            print(str(current_value) + " (Increased)")
            results = results + 1
        else:
            print(str(current_value) + " (Decreased)")
    return results


solution = changed_depth(depths)
print(solution)

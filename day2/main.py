file = open('./input.txt')
content = file.read()
directions = content.splitlines()

def get_int(string):
    for word in string.split():
        if word.isdigit():
            return int(word)

y_axis = 0 # Depth
x_axis = 0 # horizontal axis

for direction in directions:
    if "forward" in direction:
        x_axis = x_axis + get_int(direction)
    elif "up" in direction:
        y_axis = y_axis - get_int(direction)
    else:
        y_axis = y_axis + get_int(direction)

print(y_axis)
print(x_axis)
print(x_axis * y_axis)

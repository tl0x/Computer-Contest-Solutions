from enum import Enum

# Used enums because it looks nicer (Not because its more efficient)

class Shapes(Enum):
    RHOMBUS = 0
    SQUARE = 1
    CIRCLE = 2
    TRIANGLE = 3

n, q = map(int, input().split())
lst = [Shapes.RHOMBUS]*n

for i in range(q):
    command, shape, element = input().split()
    ele = int(element) - 1

    if command == "set":
        if shape == "square":
            lst[ele] = Shapes.SQUARE
        elif shape == "circle":
            lst[ele] = Shapes.CIRCLE
        elif shape == "triangle":
            lst[ele] = Shapes.TRIANGLE
    elif command == "get":
        if shape == "square":
            if lst[ele] == Shapes.SQUARE:
                print(1)
            else:
                print(0)
        elif shape == "circle":
            if lst[ele] == Shapes.CIRCLE:
                print(1)
            else:
                print(0)
        elif shape == "triangle":
            if lst[ele] == Shapes.TRIANGLE:
                print(1)
            else:
                print(0)
        else:
            if lst[ele] == Shapes.RHOMBUS:
                print(0)


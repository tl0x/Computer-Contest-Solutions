flips = input()
square = [[1,2], [3,4]]

for flip in flips:
    if flip == "H":
        temp = square[0][0]
        square[0][0] = square[1][0]
        square[1][0] = temp

        temp2 = square[0][1]
        square[0][1] = square[1][1]
        square[1][1] = temp2
    if flip == "V":
        temp = square[0][0]
        square[0][0] = square[0][1]
        square[0][1] = temp

        temp2 = square[1][0]
        square[1][0] = square[1][1]
        square[1][1] = temp2

print(square)
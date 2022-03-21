square = []
for i in range(4):
    square.append(list(map(int,input().split())))
target = sum(square[1])

flag = True

for i in range(0,4):
    counter = 0
    counter2 = 0
    for j in range(0,4):
        counter += square[i][j]
        counter2 += square[j][i]

    if counter != target or counter2 != target:
        print("not magic")
        flag = False
        break

if flag == True:
    print("magic")

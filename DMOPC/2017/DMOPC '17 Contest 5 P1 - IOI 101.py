n = input()
ans = ""
for i in n:
    if i == "0":
        ans += "O"
    elif i == "1":
        ans += "l"
    elif i == "3":
        ans += "E"
    elif i == "4":
        ans += "A"
    elif i == "5":
        ans += "S"
    elif i == "6":
        ans += "G"
    elif i == "8":
        ans += "B"
    elif i == "9":
        ans += "g"
    else:
        ans += i


print(ans)
def numberConvert(n):
  num = ""
  i = 0
  while len(num)<12:
    if len(num) == 3 or len(num) == 7:
      num += "-"
    if n[i] == '1':
      num += "1"
    elif n[i] == "2" or n[i] == "A" or n[i] == "B" or n[i] == "C":
      num += "2"
    elif n[i] == "3" or n[i] == "D" or n[i] == "E" or n[i] == "F":
      num += "3"
    elif n[i] == "4" or n[i] == "G" or n[i] == "H" or n[i] == "I":
      num += "4"
    elif n[i] == "5" or n[i] == "J" or n[i] == "K" or n[i] == "L":
      num += "5"
    elif n[i] == "6" or n[i] == "M" or n[i] == "N" or n[i] == "O":
      num += "6"
    elif n[i] == "7" or n[i] == "P" or n[i] == "Q" or n[i] == "R" or n[i] == "S":
      num += "7"
    elif n[i] == "8" or n[i] == "T" or n[i] == "U" or n[i] == "V":
      num += "8"
    elif n[i] == "9" or n[i] == "W" or n[i] == "X" or n[i] == "Y" or n[i] == "Z":
      num += "9"
    elif n[i] == "0":
      num += "0"
    i+=1
  return num

n = int(input())
for i in range(n):
  ele = input()
  print(numberConvert(ele))
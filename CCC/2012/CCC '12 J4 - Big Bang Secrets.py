k = int(input())
code = input()
converted = []
ans = ""

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

pos = 0

for i in code:
  pos += 1
  shift = (3*pos+k)
  if shift < -26:
    shift += 26
  converted.append(letters[letters.index(i) - shift])

for i in converted:
  ans += i

print(ans)
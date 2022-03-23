x = int(input())
m = int(input())
a = True
for i in range(1,m):
  if x*i % m == 1:
    print(i)
    a = False
    break

if a:
  print("No such integer exists.")

t = int(input())
s = int(input())
h = int(input())

for i in range(t):
  print('*' + ' '*s + '*' + ' '*s + '*')

print('*'*(s*2 + 3))

for i in range(h):
  print(' '*(s+1) +'*')
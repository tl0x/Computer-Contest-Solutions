def monkey(input):
  while(('BAS' in input) or ('ANA' in input)):
    input = input.replace('ANA', 'A')
    input = input.replace('BAS', 'A')

  if input == 'A':
    return True
  else:
    return False

while True:
  word = input()
  if word == 'X':
    break
  if monkey(word):
    print("YES")
  else:
    print("NO")

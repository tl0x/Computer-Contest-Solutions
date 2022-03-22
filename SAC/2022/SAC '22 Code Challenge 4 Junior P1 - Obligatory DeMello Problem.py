# Easy

n = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
x = 0
for i in vowels:
    x += n.count(i)

if x >= 2:
    print("good")
else:
    print("bad")
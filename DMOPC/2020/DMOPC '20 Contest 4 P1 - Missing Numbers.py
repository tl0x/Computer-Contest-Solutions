t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    expectedTotal = ((n+1)*n)/2
    target = expectedTotal - s
    print(target)
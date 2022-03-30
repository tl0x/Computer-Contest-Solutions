n = int(input())
lst = list(map(int,input().split()))

def median(sortedlst):
    length = len(sortedlst)
    if length % 2 == 0:
        return int((sortedlst[(length // 2)-1] + sortedlst[(length//2)])/2)
    else:
        return int(sortedlst[(length//2)])

lst.sort()
print(median(lst))
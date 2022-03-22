import math
from sys import maxsize

npoints, angle = map(int, input().split())

point = [math.cos(math.radians(angle)), math.sin(math.radians(angle))]

def findangle(point):
    x = point[0]; y = point[1]
    angle = math.degrees(math.atan2(float(x), float(y)))
    return angle


ans = []
lstpoints = []
for i in range(npoints):
    x, y = map(int, input().split())
    lstpoints.append([x, y])

for i in range(len(lstpoints)):
    print(findangle(lstpoints[i]))



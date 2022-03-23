import math

npoints, angle = map(int, input().split())

point = [math.cos(math.radians(angle)), math.sin(math.radians(angle))]


def findangle(point):
    x = point[0];
    y = point[1]
    angle = math.degrees(math.atan2(float(y), float(x)))

    if angle < 0:
        return 360-abs(angle)
    return angle

ans = []
lstpoints = []
for i in range(npoints):
    x, y = map(int, input().split())
    lstpoints.append([x, y])

for i in range(len(lstpoints)):
    ang = findangle(lstpoints[i])
    ans.append(min(360-abs(angle-ang), abs(angle-ang)))

print(ans.index(min(ans))+1)
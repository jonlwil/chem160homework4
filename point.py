import math
def distance(x1,y1,x2,y2):
    dist = math.hypot((x2-x1)**2+ (y2-y1)**2)
    return dist
print distance(x1,y1,x2,y2)
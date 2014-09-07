#Programs implements a Hill Climbing Algorithm
import math

#Class holds x and y coordinates for point
#Provides method calls for movement of the point by .1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def leftmove(self):
        self.x -= .1
    def rightmove(self):
        self.x += .1
    def upmove(self):
        self.y += .1
    def downmove(self):
        self.y -= .1

#The function find the Euclidean distance for each point movement of .1
#It then takes the smallest of those sums and moves the point in that direction a distance of .1
#If all sums equal, the function returns zero, ending the points movement
def sum(p, a, b, c, d):
    upsum = downsum = leftsum = rightsum = 0

    print "(%.1f, %.1f)" % (p.x, p.y)

    p.upmove()
    upsum = round((math.hypot(p.x - a.x, p.y - a.y)**2) + \
                  (math.hypot(p.x - b.x, p.y - b.y)**2) + \
                  (math.hypot(p.x - c.x, p.y - c.y)**2) + \
                  (math.hypot(p.x - d.x, p.y - d.y)**2), 1)
    p.downmove()

    p.downmove()
    downsum = round((math.hypot(p.x - a.x, p.y - a.y)**2) + \
                    (math.hypot(p.x - b.x, p.y - b.y)**2) + \
                    (math.hypot(p.x - c.x, p.y - c.y)**2) + \
                    (math.hypot(p.x - d.x, p.y - d.y)**2), 1)
    p.upmove()

    p.leftmove()
    leftsum = round((math.hypot(p.x - a.x, p.y - a.y)**2) + \
                    (math.hypot(p.x - b.x, p.y - b.y)**2) + \
                    (math.hypot(p.x - c.x, p.y - c.y)**2) + \
                    (math.hypot(p.x - d.x, p.y - d.y)**2), 1)
    p.rightmove()

    p.rightmove()
    rightsum = round((math.hypot(p.x - a.x, p.y - a.y)**2) + \
                     (math.hypot(p.x - b.x, p.y - b.y)**2) + \
                     (math.hypot(p.x - c.x, p.y - c.y)**2) + \
                     (math.hypot(p.x - d.x, p.y - d.y)**2), 1)
    p.leftmove()
    minimum = min(upsum, downsum, rightsum, leftsum)

    if minimum == upsum:
        p.upmove()
    elif minimum == downsum:
        p.downmove()
    elif minimum == leftsum:
        p.leftmove()
    elif minimum == rightsum:
        p.rightmove()

    if upsum == downsum and downsum == rightsum and rightsum == leftsum :
        return True


point = Point(1, 1)
a = Point(1, 5)
b = Point(6, 4)
c = Point(5, 2)
d = Point(2, 1)
flag = False
while not flag:
    flag = sum(point, a, b, c, d)


# print "p to a", math.hypot(point.x - a.x, point.y - a.y)
# print "p to b", math.hypot(point.x - b.x, point.y - b.y)
# print "p to c", math.hypot(point.x - c.x, point.y - c.y)
# print "p to d", math.hypot(point.x - d.x, point.y - d.y)



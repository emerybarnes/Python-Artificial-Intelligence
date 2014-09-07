import Queue
import math

class Node:
    def __init__(self, val, opr):
        self.val = val
        self.opr = opr



GOAL = 6
START = 8
count1 = count2 = 0
node = Node(START, "%d)" % START)

q = Queue.Queue()

q.put(node)
check = node

while check.val != GOAL:

############  #Floor/Sqrt Processing  ###############
    try:
        node = Node(math.floor(math.sqrt(check.val)), "floor(sqrt(" + check.opr + ")")
    except OverflowError:
        pass
    if node.val == GOAL:
        print u"{0:s}".format(node.opr),
        #print (")" * count2),
        print "= %d" % GOAL
        break
    q.put(node)


############  #Factorial processing  ###############
    try:
        node = Node(math.factorial(check.val), "factorial(" + check.opr + ")")
    except OverflowError:
        pass
    if node.val == GOAL:
        print u"{0:s}".format(node.opr),
       # print (")" * count2),
        print "= %d" % GOAL
        break
    q.put(node)

    count2 += 1

    check = q.get()





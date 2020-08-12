
def createGraph(dict, e1, e2, km):
    if e1 in dict:
        list = dict[e1]
        ilist = []
        ilist.append(e2)
        ilist.append(km)
        list.append(ilist)
    else:
        ilist = [e2, km]
        list = []
        list.append(ilist)
        dict[e1] = list
    return True


class Stack():
    def __init__(self, n):
        self.n = n
        self.list = []

    def push(self, e):
        self.list.append(e)

    def pop(self):
        return self.list.pop()

    def printStack(self):
        print (self.n)
        print (self.list)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False

    def deep_copy(self, s1):
        # print "I am in deep copy s1 ", s1.printStack()
        list1 = []
        self.list = []
        while not s1.isEmpty():
            v = s1.pop()
            self.push(v)
            list1.append(v)

        # print "list1", list1
        for i in range((len(list1) - 1), -1, -1):
            s1.push(list1[i])
        # print "s1 in deep copy", s1.printStack()

    def reverse(self, s1):
        self.list = []
        while not s1.isEmpty():
            v = s1.pop()
            self.push(v)


def finding_path1(dict, start, end, s1, wt):
    global minsum
    global smin
    if start == end:
        if minsum == -1:
            minsum = wt
            smin.deep_copy(s1)
            # smin.printStack()
            # s1.printStack()
        elif wt < minsum:
            minsum = wt
            smin.deep_copy(s1)
            # smin.printStack()
            # s1.printStack()
        return True

    # print(start)
    if start in dict:
        list = dict[start]
    else:
        list = []
    # s1.push(start)
    for i in range(0, len(list)):
        newStartList = list[i]
        newStart = newStartList[0]
        newwt = newStartList[1]
        s1.push(newStart)
        fp = finding_path1(dict, newStart, end, s1, wt + newwt)
        # if fp == True:
        #     return True
        # else:
        s1.pop()

    return False


def finding_path_wrapper(dict, start, end, s1, wt):
    s1.push(start)
    finding_path1(dict, start, end, s1, wt)


# y = finding_path(dict, 'a', 'd', s1, 5)


dict = {}
createGraph(dict, 'a', 'b', 1)
createGraph(dict, 'b', 'c', 7)
createGraph(dict, 'c', 'd', 8)
createGraph(dict, 'b', 'e', 9)
createGraph(dict, 'e', 'd', 3)
# print(dict)

minsum = -1
smin = Stack("MinStack")

s1 = Stack("Stack1")
y = finding_path_wrapper(dict, 'a', 'd', s1, 0)
finalAnswerStack = Stack(" ")
finalAnswerStack.reverse(smin)
# print(y)hello I am a sid the sience kid bro ha ha cool qbro hi
print "shortest path to follow: "
finalAnswerStack.printStack()
print "and min sum of path is: ", minsum

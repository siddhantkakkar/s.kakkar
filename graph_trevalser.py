class Node:
    def __init__(self, data,n):
        self.data = data
        self.leftNode = None
        self.rightNode = None
        self.name = n

    def isLeft(self):
        if self.leftNode == None:
            return False
        return True

    def isRight(self):
        if self.rightNode == None:
            return False
        return True

    def addLeft(self, left):
        self.leftNode = left

    def addRight(self, right):
        self.rightNode = right
        # # def printTree(self):
        #
        # if self.leftNode!=None:
        #     self.leftNode.printTree()
        # print(self.data)
        # if self.rightNode!=None:
        #     self.rightNode.printTree()
    # def printTree(self):
    #   print(self.data)
    #   if self.leftNode!=None:
    #     self.leftNode.printTree()
    #   if self.rightNode!=None:
    #     self.rightNode.printTree()
    # def printTree(self):
    #     if self.leftNode != None:
    #         self.leftNode.printTree()
    #     if self.rightNode != None:
    #         self.rightNode.printTree()
    #     print(self.data)

    def searchTree(self, n):
        print self.data
        if self.data == n:
            print self.name
        elif n > self.data:
            if self.rightNode == None:
                print "ans not found"
            else:
                self.rightNode.searchTree(n)
        elif n < self.data:
            if self.leftNode == None:
                print "ans not found"
            else:
                self.leftNode.searchTree(n)


def calling():
    root = Node(5,"motu")
    rightnode = Node(9,"pinku")
    leftnode = Node(3,"chotu")
    rightnode1 = Node(4,"siddhant")
    rightnode2 = Node(50,"gogi")
    leftnode1 = Node(8,"faltu")
    leftnode2 = Node(2,"bholu")

    root.addLeft(leftnode)
    root.addRight(rightnode)
    leftnode.addRight(rightnode1)
    leftnode.addLeft(leftnode2)
    rightnode.addRight(rightnode2)
    rightnode.addLeft(leftnode1)
    root.searchTree(4)



calling()
import time


class Dictionary:

    def __init__(self):

        self.dict = {}

    def insert(self, key, value):

        self.dict[key] = value

        return self.dict

    def printTree(self):

        print(self.dict)

    def delete(self, key):

        if key in self.dict:
            del self.dict[key]

    def search(self, key):

        val = ''

        if key in self.dict:

            val = self.dict[key]

        else:

            print ("ans not found")

        return val


class List:

    def __init__(self):

        self.list = []

    def insert(self, rolno, n):

        self.list.append((rolno, n))

    def printTree(self):

        print(self.list)

    def search(self, rolno):

        for i in range(0, len(self.list)):

            if self.list[i][0] == rolno:

                return self.list[i][1]

            else:

                print("ans not found")

                return False

    def delete(self, n):

        flag = False

        print len(self.list)

        for i in range(0, len(self.list) + 1):

            print 'i', i

            print len(self.list)

            if i >= len(self.list):
                print 'I have enter the stop condition'

                return

            print 'I have enterd the for'

            if (self.list[i][0]) - 1 == n:
                print len(self.list)

                print ' I a have enterd the if and the for loop'

                flag = True

                print "I did not "

            if flag:

                print 'printing the flag', flag

                if i + 1 < len(self.list):
                    self.list[i] = self.list[i + 1]

                del self.list[len(self.list) - 1]

                print self.list


class Node:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self.leftNode = None
        self.rightNode = None
        self.left = None
        self.right = None

    def isleaf(self):

        if self.leftNode is None and self.rightNode is None:
            return True
        return False

    def isLeftNodeChild(self):

        if self.leftNode is not None:
            return True
        return False

    def isRightNodeChild(self):
        if self.rightNode is not None:
            return True
        return False

    def isTwoChildren(self):

        if self.leftNode is not None and self.rightNode is not None:
            return True

        return False

    def isLeft(self):
        if self.leftNode is None:
            return False

        return True

    def isRight(self):

        if self.rightNode is not None:
            return False

        return True

    def addLeft(self, left):

        self.leftNode = left

    def addRight(self, right):

        self.rightNode = right

    def createBst(self, data, name):

        if data > self.data:

            if self.rightNode is not None:

                self.rightNode.createBst(data, name)

            else:

                n1 = Node(data, name)

                self.addRight(n1)

        elif data < self.data:

            if self.leftNode is not None:

                self.leftNode.createBst(data, name)
            else:

                n1 = Node(data, name)

                self.addLeft(n1)

    def printTree(self):

        print(self.data, self.name)

        if self.leftNode is not None:
            self.leftNode.printTree()

        if self.rightNode is not None:
            self.rightNode.printTree()

    def delete_internal(self, key, pnode):

        # print 'self.data', self.data

        if self.data == key:

            # print 'key', key

            # print 'I am in first if'

            # print 'pnode', pnode

            if pnode is None:
                print "delete the root"

                return None

            if self.isleaf():

                if pnode.leftNode == self:

                    pnode.leftNode = None

                elif (pnode.rightNode == self):

                    pnode.rightNode = None

            elif self.isRightNodeChild():

                if (pnode.leftNode == self):

                    pnode.leftNode = self.rightNode

                elif (pnode.rightNode == self):

                    pnode.rightNode = self.rightNode

            elif self.isLeftNodeChild():

                # print 'I have entered the elif'

                if (pnode.leftNode == self):

                    pnode.leftNode = self.leftNode

                elif (pnode.rightNode == self):

                    pnode.rightNode = self.leftNode

            elif self.isTwoChildren():

                # print 'self', self

                # print 'I have entered the elif'

                if pnode.leftNode == self:

                    # print 'I have enter the if'

                    pnode.leftNode = self.rightNode

                    self.rightNode.leftNode = self.leftNode

                    self.rightNode = self.rightNode.leftNode

                elif pnode.rightNode == self:

                    # print 'I have enter the if'

                    pnode.rightNode = self.rightNode

            else:

                print "Case not handled"





        elif key > self.data:
            if self.rightNode is None:
                print("ans not found")
            else:
                self.rightNode.delete_internal(key, self)
        elif key < self.data:
            if self.leftNode is None:
                print("ans not found")
            else:
                self.leftNode.delete_internal(key, self)

    def delete(self, key):
        self.delete_internal(key, None)

    def searchTree(self, n):
        print(self.data)
        if self.data == n:
            print (self.name)
        elif n > self.data:
            if self.rightNode is None:
                print("ans not found")
            else:
                self.rightNode.searchTree(n)
        elif n < self.data:
            if self.leftNode is None:
                print("ans not found")
            else:
                self.leftNode.searchTree(n)


# n1 = Node(5, "saina")

# n1.createBst(6, "siddhant")

# starttime = time.time()

# for i in range(0, 700):
#     n1.searchTree(i)
# endtime = time.time()
# print("toal time taken", endtime - starttime)
#
# n1 = Node(5,"saina")
# start_time = time.time()
# for i in range(0,10000):
#     n1.searchTree(i)
# end_time = time.time()
# num = end_time - start_time
# output = f"{num:.9f}"
# print ("total time taken", output)


n1 = List()

n1.insert(22, "siddhant")

print '\n'

n1.insert(21, "saina")

# n1.printTree()

# n1.delete(22)
# v = n1.search(22)

#
# print(v)
#
# n1.delete(22)
#
# n1.printTree()
#
# pnode = Node
#
# pnode.createBst(5, "siddhant")
#
# pnode.createBst()
#
    # pnode.delete(pnode, pnode.createBst(5, "siddhant"))

pnode = Node(5, "siddhant")

pnode.createBst(9, "saina")

pnode.createBst(7, "sid")

pnode.createBst(3, "sai")

pnode.createBst(4, "sahir")

pnode.printTree()

print '\n'

print 'time to delete'

# print "deleting 7"
# pnode.delete(7)

# pnode.printTree()
# print "deleting 9"
# pnode.delete(9)
# pnode.printTree()

start_time = time.time()

print '\n'

print "deleting 3"

pnode.delete(3)

pnode.printTree()

end_time = time.time()

print 'total time taken', end_time - start_time

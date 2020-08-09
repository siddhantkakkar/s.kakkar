class Rn:

    def __init__(self, name):

        self.name = name

        self.dauter = None

        self.son = None


        self.left = None

        self.right = None



    def printRn(self):

        print self.name

        if self.dauter is not None:

            self.dauter.printRn()

        elif self.son is not None:

            self.son.printRn()

        elif self.dauter2 is not None:

            self.dauter2.printRn()

        elif self.son1 is not None:

            self.son1.printRn()

        else:

            print "sorry pls try again"








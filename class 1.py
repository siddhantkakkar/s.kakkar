class Animal:
    def __init__(self, name=' ', size=0):
        self.name = name
        self.size = size

        def _lt_(self, other):
            if self > other:
                return True
            else:
                return False

        def __gt__(self, other):
            if other> self:
                return False
            else:
                return True

        def __eq__(self, other):
            if self == other:
                return True
            else:
                return False


class Dog(Animal):
    def __init__(self,name=' ',size=0):
        self.name = name
        self.size = size

        def __lt__(self, other):
            if self > other:
                return True
            else:
                return False

        def __gt__(self, other):
            if other > self:
                return False
            else:
                return True

        def __eq__(self, other):
            if self== other:
                return True
            else:
                return False


class Cat(Animal):
    def __init__(self, name=' ', size=0):
          self.name = name
          self.size = size

    def __lt__(self, other):
        if self > other:
            return True
        else:
            return False

    def __gt__(self, other):
        if other > self:
            return False
        else:
            return True

    def __eq__(self, other):
        if self == other:
            return True
        else:
            return False



class Mouse(Animal):
    def __init__(self, name=' ', size=0):
        self.name = name
        self.size = size

    def __lt__(self, other):
        if self > other:
            return False
        else:
            return True

    def __gt__(self, other):
        if other > self:
            return False
        else:
            return True

    def __eq__(self, other):
        if self == other:
            return True
        else:
            return False





d1=Animal('tiger',1)
c1=Animal('pussy',2)
m1=Animal('chotu',3)



if d1 > c1:
    print 'dog is bigger than cat'


if m1 < c1:

    print 'cat is bigger than mouse'

if m1 > c1:
    print 'mouse is bigger than cat'

if m1 > d1:
    print 'mouse is bigger than dog'

    if d1 > c1:
        print 'dog is bigger than cat'

if d1 > c1:
    print 'dog is bigger than cat'


if d1 == c1:
    print 'dog is same as cat'


if m1 == c1:
    print 'mouse is same as cat'

if d1 > c1:
    print 'dog is bigger than cat'

if d1 > c1:
    print 'dog is bigger than cat'


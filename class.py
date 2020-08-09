class superhero:

    count=0

    def __init__(self,name='', power=0, weapon = 0):
        self.name = name
        self.power = power
        self.weapon = weapon

        superhero.count += 1

    def display_count(self):
        print(superhero.count)

    def display_name(self):
        print (self.name)
        print ("after name")

    def display_power(self):
         print (self.power)

    def display_weapon(self):
         self.weapon.display_age()
         self.weapon.display_name()
         self.weapon.display_purpose()

    def display_superhero(self):
        self.display_name()
        self.display_power()
        self.display_weapon()

    def __eq__(self, other):
        if self.power == other.power:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.power > other.power:
            return True
    # s1is self and s2 is other
    def __gt__(self, other):
        if other.power > self.power:
                return False



class weapon:

    def __init__(self, age=0,name='',purpose=''):
        self.age=age
        self.name=name
        self.purpose=purpose


    def display_age(self):
        print (self.age)

    def display_name(self):
        print (self.name)


    def display_purpose(self):
         print (self.purpose)




import random

class Warrior:
    hitpoints = 100
    attack = 20
    name = ""
    def __init__(self):
        self.name = input()

def Fight(first,second):
    while (first.hitpoints >=1 and second.hitpoints>=1):
        how = random.randint(1, 2)
        if (how == 1):
            first.hitpoints -= second.attack
            print("Воин " + second.name + " бъёт воина " + first.name)
        else:
            second.hitpoints -= first.attack
            print("Воин " + first.name + " бъёт воина " + second.name)
    if (first.hitpoints == 0): print("Воин "+second.name+" победил")
    else: print("Воин "+first.name+" победил")

random.seed()
first = Warrior()
second = Warrior()
Fight(first,second)
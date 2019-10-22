import random

class Warrior:
    hitpoints = 100
    attack = 20
    name = ""
    is_alive = True
    def __init__(self):
        self.name = input()

    def Take_dmg(self,enemy):
        self.hitpoints -=enemy.attack
        if (self.hitpoints == 0): self.is_alive = False
        return self

    def Give_dmg(self,enemy):
        print("Воин " + self.name + " бъёт воина " + enemy.name)
        enemy = enemy.Take_dmg(self)
        if (enemy.is_alive == False):  print("Воин "+self.name+" победил")
        return enemy

def Fight(first,second):
    while (first.is_alive and second.is_alive):
        how = random.randint(1, 2)
        if (how == 1):
            second.Give_dmg(first)
        else:
           first.Give_dmg(second)

random.seed()
first = Warrior()
second = Warrior()
Fight(first,second)

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack (self):
        return self.strength
    def receiveDamage (self, damage):
        self.health = self.health - damage

# Viking
class Viking (Soldier):
    def __init__ (self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "{} has received {} points of damage".format(self.name, damage)
        else:
            return "{} has died in act of combat".format(self.name)
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon (Soldier):
    def receiveDamage (self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return "A Saxon has received {} points of damage".format(damage)
        else:
            return "A Saxon has died in combat"

# War
import random
class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking (self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon (self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        vikingo = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        resultado_vikingo = saxon.receiveDamage(vikingo.attack())
        self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health>0]
        return resultado_vikingo
    
    def saxonAttack (self):
        vikingo = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        resultado_saxon = vikingo.receiveDamage(saxon.attack())
        self.vikingArmy = [viking for viking in self.vikingArmy if viking.health>0]
        return resultado_saxon
   
    def showStatus (self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)>0 and len(self.vikingArmy)>0:
            return "Vikings and Saxons are still in the thick of battle."
    



 

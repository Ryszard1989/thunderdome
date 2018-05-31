

class Teacher:
  def __init__(self, name, health, weapon):
    self.name = name
    self.health = health
    self.weapon = weapon
    self.dead = False

  def print(self):
    print("Teacher: " + self.name
            + ", Health: " + str(self.health)
            + ", " + self.weapon.stringPrint())

  def attacked(self, weapon):
    self.health = self.health - weapon.weaponDamage
    if (self.health <= 0):
     self.dead = True
    print(self.name + " attacked by weapon " 
            + weapon.weaponName
            + " for " + str(weapon.weaponDamage) + " damage!")
    self.isDead()

  def attack(self, teacher):
    print(self.name + " attacks " + teacher.name)
    teacher.attacked(self.weapon)

  def isDead(self):
    if (self.dead == True):
      print(self.name + " is dead!")
    else:
      print(self.name + " has "
              + str(self.health) + " health remaining!\n")

class Weapon:
  def __init__(self, weaponName, weaponDamage):
    self.weaponName = weaponName
    self.weaponDamage = weaponDamage

  def print(self):
    print("Weapon: " + self.weaponName
            + ", Damage: " + str(self.weaponDamage))
  def stringPrint(self):
    return("Weapon: " + self.weaponName
            + ", Damage: " + str(self.weaponDamage))


print ("***WELCOME TO THE THUNDERDOME***\n")    
w = Weapon("Axe", 42)
t = Teacher("Claudine",69,w)
t.print()
w2 = Weapon("Minigun", 15)
t2 = Teacher("Ryszard", 50, w2)
t2.print()

print("")
t2.attack(t)
t.attack(t2)
t2.attack(t)
t.attack(t2)

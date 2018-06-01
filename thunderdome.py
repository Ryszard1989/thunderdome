

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

  def heal(self, health):
    print(self.name + " heals for " + str(health) + " health")
    self.health = self.health + health

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


#class GameManager:
#  def __init__(self):
#    player1Name = input("Enter Player name: ")
#    startWeapon = Weapon("unarmed",
#    self.player = Teacher(player1Name,100)
#    self.currentPlayerTurn = 0




def testTeachers():
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

def gameManager():
    print ("***WELCOME TO THE THUNDERDOME***\n")
    weapon1 = Weapon("Axe",42)
    weapon2 = Weapon("Minigun",15)
    weapon3 = Weapon("Baseball Bat",20)
    weapon4 = Weapon("Rubber Duck", 8)
    player1Name = input("Enter Player 1 name: ") 
    player2Name = input("Enter Player 2 name: ")
    weaponBox = [weapon1, weapon2, weapon3, weapon4]
    count = 1
    for i in weaponBox:
      print (str(count) + ") " + i.weaponName)
      count = count+1
    player1Weapon = int(input("Player 1 enter a number to pick a weapon: "))
    player2Weapon = int(input("Player 2 enter a number to pick a weapon: "))
    p1 = Teacher(player1Name, 100, weaponBox[player1Weapon-1])
    p2 = Teacher(player2Name, 100, weaponBox[player2Weapon-1])
    p1.print()
    p2.print()

    p2.attack(p1)
    p1.heal(30)
    p2.attack(p1)
    p1.attack(p2)


#testTeachers()
gameManager()










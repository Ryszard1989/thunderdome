from random import randint

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
    self.isDeadPrint()

  def attack(self, teacher):
    print(self.name + " attacks " + teacher.name)
    teacher.attacked(self.weapon)

  def heal(self, health):
    print(self.name + " heals for " + str(health) + " health")
    self.health = self.health + health

  def playerTurn(self, enemy):
    if(self.dead == False):
      action = input("Pick 1 to attack, 2 to heal")
      if (action == '1'):
        self.attack(enemy)
      elif (action == '2'):
        self.heal(10)

  def enemyTurn(self, enemy):
    action = randint(1,3)
    print("Enemy action: " + str(action))
    if(self.dead == False):
      if action in {1,2}:
        self.attack(enemy)
      elif action is 3:
        self.heal(10)

  def isDeadPrint(self):
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


def testGameLoop():
    print ("***WELCOME TO THE THUNDERDOME***\n")
    weapon1 = Weapon("Axe",42)
    weapon2 = Weapon("Minigun",15)
    weapon3 = Weapon("Baseball Bat",20)
    weapon4 = Weapon("Rubber Duck", 8)
    player1Name = "player 1"
    player2Name = "player 2"
    weaponBox = [weapon1, weapon2, weapon3, weapon4]
    count = 1
    for i in weaponBox:
      print (str(count) + ") " + i.weaponName)
      count = count+1
    player1Weapon = 1
    player2Weapon = 2
    p1 = Teacher(player1Name, 100, weaponBox[player1Weapon-1])
    p2 = Teacher(player2Name, 100, weaponBox[player2Weapon-1])
    p1.print()
    p2.print()

    playerTurn = 1
    count = 1
    allPlayersAlive = True
    while (allPlayersAlive):
      playerTurn = count%2
      if(playerTurn == 1):
        if(p1.dead == False):
          p1.attack(p2)
      elif(playerTurn == 0):
        if(p2.dead == False):
          p2.attack(p1)
      if(p1.dead):
        allPlayersAlive = False
        print(p1.name + " is dead. " + p2.name + "  wins!")
      elif (p2.dead):
        allPlayersAlive = False
        print(p2.name + " is dead. " + p1.name + "  wins!")
      count = count + 1


def testUserInput():
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

    playerTurn = 1
    count = 1
    allPlayersAlive = True
    while (allPlayersAlive):
      playerTurn = count%2
      if(playerTurn == 1):
        p1.playerTurn(p2)
      elif(playerTurn == 0):
        p2.enemyTurn(p1)
      if(p1.dead):
        allPlayersAlive = False
        print(p1.name + " is dead. " + p2.name + "  wins!")
      elif (p2.dead):
        allPlayersAlive = False
        print(p2.name + " is dead. " + p1.name + "  wins!")
      count = count + 1



#testTeachers()
#testGameLoop()
testUserInput()









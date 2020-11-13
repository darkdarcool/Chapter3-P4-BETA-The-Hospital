player_damage1 = 30
import os, random
import time, sys
os.system('clear')
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
bold = '\033[1m'
END = '\033[0m'
def swapPositions(list, pos1, pos2):
    """this swaps the elements of the list"""
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


#types of speed


def spslo(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        if ((i != "\n") or (i != ":") or (i != ".")):
            time.sleep(0.1)
        else:
            time.sleep(0.6)


def spmod(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        if ((i != "\n") or (i != ":") or (i != ".")):
            time.sleep(0.06)
        else:
            time.sleep(0.6)


def spfas(message):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        if ((i != "\n") or (i != ":") or (i != ".")):
            time.sleep(0.03)
        else:
            time.sleep(0.02)


spfas(green + "Please choose one from the following text speeds:\n")
#speed manager

time.sleep(1)
spslo(bwhite + "a)This is slow.\n")
time.sleep(0.07)
spmod("b)This is moderate.\n")
time.sleep(0.04)
spfas("c)This is fast.\n")
time.sleep(0.02)
print(green + "Enter the letter [a/b/c]")
spc = input(":")
spc = spc.lower()
if spc == "a":
    time.sleep(0.07)
    os.system("clear")
    sp = spslo
    sp("Thank you!!\n")
elif spc == "b":
    time.sleep(0.04)
    os.system("clear")
    sp = spmod
    sp("Thank you!!\n")
elif spc == "c":
    time.sleep(0.02)
    os.system("clear")
    sp = spfas
    spslo("Thank you!!\n")
time.sleep(1)
os.system("clear")
#Title Typer

print()
print()

#The story
time.sleep(3)
os.system('clear')
print(yellow + """             
						Chapter 3 Part 4""")
print('                    The Hospital')

print(blue + "              PRESS ENTER")

blank = ''
inpt = input('')
if inpt == blank:
    os.system("clear")
elif input != blank:
    print(red + ' press Enter to continue')
else:
    print(red + 'An Error occured.\nPress Enter')
time.sleep(1)
os.system('clear')

sp('▀█▀ █░█ █▀▀   █░█ █▀█ █▀ █▀█ █ ▀█▀ ▄▀█ █░░\n')
sp('░█░ █▀█ ██▄   █▀█ █▄█ ▄█ █▀▀ █ ░█░ █▀█ █▄▄\n\n')
time.sleep(1)
os.system('clear')
score = 2
sp(magenta + 'Welcome to the last part of the chapter! (hopefully). This is going to lead off the last one, so it will be long like the last one. See ya soon!\n- Darkdarcool and ConorTseng ')
time.sleep(1)
os.system('clear')
sp(bwhite + ' They walked over to the only door that they could see. They noticed a few more doors, and one that said \'AUTHORIZED PERSONEL ONLY\' It looked like the one that had the security cams in it. But then they saw that it neeeded a keycard. Should Rachel try to jam up the slot or should they try to find the keycard.')
time.sleep(1)
os.system('clear')
sp(' "It must be in the employee lounge" Rachel said. "But that\'s like 5 floors up! " James said. "I know" Rachel said back. "No one wants do this, but we need to find the elevator. " "Ok then, let\'s get searching. " William said.   ')
time.sleep(1)
os.system('clear')
sp('"I remember... when I was here,when I broke my leg, the elevator was through that door. " Rachel said.\n They walk over to the door. "This one?" James said. "That one" Rachel said back. So they go into the door and now they are at the elevator, "Which floor" says James "duh I already told you the 4th floor" exclaims Rachel They see two shady people walking twords them.')
time.sleep(1)
os.system('clear')
sp('You walk up to them. "Hello?" Rachel said. The two guys look at them. "Hey, survivors!". "Hello, can you direct us to the elevator?". "HEY, we\'ll give you the scematics,  OVER MY DEAD BODY. DIE NOW!!!!!"')
time.sleep(2)
os.system('clear')
print(yellow + """             
						Battle!!!""")

print(blue + "              PRESS ENTER")

blank = ''
inpt = input('')
if inpt == blank:
    os.system("clear")
elif input != blank:
    print(red + 'Please press Enter')
else:
    print(red + 'An Error occured.\nPress Enter')
time.sleep(2)
os.system('clear')

## Now, the game
enemies = [
    'Scar slave', 'scar follower', 'scar leader', 'scar fighter', 'scar spy'
]

enemy_name = random.choice(enemies)
enemy_health = 120
enemy_accuracy = 0.4
enemy_damage = 15

player_health = 80
player_accuracy = 0.8
player_damage = player_damage1
heals_left = 3
heal_amount = 10


def heal_player(amount):
    global player_health

    player_health += amount
    player_health = player_health + amount


def attack_enemy(amount):
    global enemy_health
    enemy_health -= amount
    print('You hit the enemy with your bat!!!')


def attack_player(amount):
    global player_health
    player_health -= amount
    print('You were hit by the enemies bat! ')


print('A ' + enemy_name + ' has challenged you to a fight! ')
print()
while player_health > 0:
    print(enemy_name + ' HP: ' + str(enemy_health))
    print('Your HP: ' + str(player_health))
    print('Bandages left: ' + str(heals_left))
    print()
    action = input('Attack or heal? ')
    print()

    if action == "attack":
        player_roll = random.randint(1, 10)

        if player_roll < player_accuracy * 10:
            attack_enemy(player_damage)

            if enemy_health <= 0:
                print('You win, you beat (a) (the) ' + enemy_name +
                      '. You have received the potion!!!')
                break

        else:
            print('You missed your shot!')

    elif action == 'heal':
        if player_health == 80:
            print('You have full health, you cannot use a bandage.')
        else:
            if heals_left:
                heal_player(heal_amount)
                heals_left -= 1
            else:
                print('You are out of bandages!!')

    time.sleep(1)
    enemy_roll = random.randint(1, 10)
    if enemy_roll < enemy_accuracy * 10:
        attack_player(enemy_damage)

        if player_health <= 0:
            print('You got pummeled by the enemies bat.... :( ')
            break

    else:
        print(enemy_name + ' missed! ')

    print()
    print('******************')
    print()

if player_health <= 0:
    sp('You sadly lost against the ' + enemy_name + ', would you like to restart the battle?'
       )
    time.sleep(1)
    sp('Y/N')
    toy = input('      >>>>>>>  ').upper()
    toy = toy.upper()
    if toy == 'Y':
      sp('TOO BAD')

    elif toy == 'N':
      sp('Your loss')
      sys.exit()
elif enemy_health <= 0:
  print('You won!')
  time.sleep(2)
  os.system('clear')
  pass
  



    #Fix, set player to line to 276
time.sleep(1)
os.system('clear')
sp(red + 'One down, another to go!!!')
print(yellow + """             
						Battle!!!""")

print(blue + "              PRESS ENTER")

blank = ''
inpt = input('')
if inpt == blank:
    os.system("clear")
elif input != blank:
    print(red + 'Please press Enter')
else:
    print(red + 'An Error occured.\nPress Enter')
time.sleep(2)
os.system('clear')

## Now, the game
enemies = [
    'Scar slave', 'scar follower', 'scar leader', 'scar fighter', 'scar spy'
]

enemy_name = random.choice(enemies)
enemy_health = 120
enemy_accuracy = 0.4
enemy_damage = 15

player_health = 80
player_accuracy = 0.8
player_damage = player_damage1
heals_left = 3
heal_amount = 10


def heal_player(amount):
    global player_health

    player_health += amount
    player_health = player_health + amount


def attack_enemy(amount):
    global enemy_health
    enemy_health -= amount
    print('You hit the enemy with your bat!!!')


def attack_player(amount):
    global player_health
    player_health -= amount
    print('You were hit by the enemies bat! ')


print('A ' + enemy_name + ' has challenged you to a fight! ')
print()
while player_health > 0:
    print(enemy_name + ' HP: ' + str(enemy_health))
    print('Your HP: ' + str(player_health))
    print('Bandages left: ' + str(heals_left))
    print()
    action = input('Attack or heal? ')
    print()

    if action == "attack":
        player_roll = random.randint(1, 10)

        if player_roll < player_accuracy * 10:
            attack_enemy(player_damage)

            if enemy_health <= 0:
                print('You win, you beat (a) (the) ' + enemy_name +
                      '. You have received the potion!!!')
                break

        else:
            print('You missed your shot!')

    elif action == 'heal':
        if player_health == 80:
            print('You have full health, you cannot use a bandage.')
        else:
            if heals_left:
                heal_player(heal_amount)
                heals_left -= 1
            else:
                print('You are out of bandages!!')

    time.sleep(1)
    enemy_roll = random.randint(1, 10)
    if enemy_roll < enemy_accuracy * 10:
        attack_player(enemy_damage)

        if player_health <= 0:
            print('You got pummeled by the enemies bat.... :( ')
            break

    else:
        print(enemy_name + ' missed! ')

    print()
    print('******************')
    print()

if player_health <= 0:
    sp('You sadly lost against the ' + enemy_name + ', would you like to restart the battle?'
       )
    time.sleep(1)
    sp('Y/N')
    toy = input('      >>>>>>>  ').upper()
    toy = toy.upper()
    if toy == 'Y':
      sp('TOO BAD')
      sys.exit()
    elif toy == 'N':
      sp('Your loss')
      sys.exit()
elif enemy_health <= 0:
  print('You won!')
  time.sleep(2)
  os.system('clear')
  pass
  



    #Fix, set player to line to 276
os.system('clear')
sp('You got to live!!')
time.sleep(2)
os.system('clear')
sp('After searching the enemy\'s body\'s, you find bullets, and engrave them into your bat!')
time.sleep(0.5)
print(red + '\nDamage + 5 ')
player_damage1 + 5
time.sleep(2)
os.system('clear')
sp('"Who were those guys??" Rachel said in shock. "I think that was out first encounter with scars!" William said. "My dad told me about them. " "There could be tons in this building!!" James said. "We can\'t wast time and ponder that, lets get going. "')
time.sleep(2)
os.system('clear')
sp('You grab the scamatics and go')
sp('When you get in the elevator, you hit floor 4')
sp('"SOOOOO, what do we talk about in here?" James said trying to make conversation. Just then, a huge crash happend. Then the doors opened. ')
time.sleep(2)
os.system('clear')
sp(yellow + 'Then they looked at a big sign.\n"HEY!! This isn\'t floor 4! This is floor 2!" James said. "I guess the scar know were coming and cut the cables. But I garuntee there are move elevators, each going up one more floor, now lets get going, and no doubt there will be tons of scars in the way! ')
time.sleep(2)
os.system('clear')
sp(blue + '[They walked out of the elevator to floor 2]\n"Hmmmm, acording to they scematics, we have to go over there, the hallway that leads to the emergency care" James said')
time.sleep(2)
os.system('clear')
sp('They walk to the hallway and they see 4 scars coming twords them "There they are! GET THEM!!!!!" one of the scar said.')
time.sleep(2)
os.system('clear')



print(yellow + """             
						Battle!!!""")

print(blue + "              PRESS ENTER")

blank = ''
inpt = input('')
if inpt == blank:
    os.system("clear")
elif input != blank:
    print(red + 'Please press Enter')
else:
    print(red + 'An Error occured.\nPress Enter')
time.sleep(2)
os.system('clear')

## Now, the game
enemies = [
    'Scar slave', 'scar follower', 'scar leader', 'scar fighter', 'scar spy'
]

enemy_name = random.choice(enemies)
enemy_health = 120
enemy_accuracy = 0.4
enemy_damage = 15

player_health = 80
player_accuracy = 0.8
player_damage = player_damage1
heals_left = 3
heal_amount = 10


def heal_player(amount):
    global player_health

    player_health += amount
    player_health = player_health + amount


def attack_enemy(amount):
    global enemy_health
    enemy_health -= amount
    print('You hit the enemy with your bat!!!')


def attack_player(amount):
    global player_health
    player_health -= amount
    print('You were hit by the enemies bat! ')


print('A ' + enemy_name + ' has challenged you to a fight! ')
print()
while player_health > 0:
    print(enemy_name + ' HP: ' + str(enemy_health))
    print('Your HP: ' + str(player_health))
    print('Bandages left: ' + str(heals_left))
    print()
    action = input('Attack or heal? ')
    print()

    if action == "attack":
        player_roll = random.randint(1, 10)

        if player_roll < player_accuracy * 10:
            attack_enemy(player_damage)

            if enemy_health <= 0:
                print('You win, you beat (a) (the) ' + enemy_name +
                      '. You have received the potion!!!')
                break

        else:
            print('You missed your shot!')

    elif action == 'heal':
        if player_health == 80:
            print('You have full health, you cannot use a bandage.')
        else:
            if heals_left:
                heal_player(heal_amount)
                heals_left -= 1
            else:
                print('You are out of bandages!!')

    time.sleep(1)
    enemy_roll = random.randint(1, 10)
    if enemy_roll < enemy_accuracy * 10:
        attack_player(enemy_damage)

        if player_health <= 0:
            print('You got pummeled by the enemies bat.... :( ')
            break

    else:
        print(enemy_name + ' missed! ')

    print()
    print('******************')
    print()

if player_health <= 0:
    sp('You sadly lost against the ' + enemy_name + ', would you like to restart the battle?'
       )
    time.sleep(1)
    sp('Y/N')
    toy = input('      >>>>>>>  ').upper()
    toy = toy.upper()
    if toy == 'Y':
      sp('TOO BAD')

    elif toy == 'N':
      sp('Your loss')
      sys.exit()
elif enemy_health <= 0:
  print('You won!')
  time.sleep(2)
  os.system('clear')
  pass
  



    #Fix, set player to line to 276

sp('You got to live!!')
sp('One down, 3 to go!')
time.sleep(2)
os.system('clear')


print(yellow + """             
						Battle!!!""")

print(blue + "              PRESS ENTER")

blank = ''
inpt = input('')
if inpt == blank:
    os.system("clear")
elif input != blank:
    print(red + 'Please press Enter')
else:
    print(red + 'An Error occured.\nPress Enter')
time.sleep(2)
os.system('clear')

## Now, the game
enemies = [
    'Scar slave', 'scar follower', 'scar leader', 'scar fighter', 'scar spy'
]

enemy_name = random.choice(enemies)
enemy_health = 120
enemy_accuracy = 0.4
enemy_damage = 15

player_health = 80
player_accuracy = 0.8
player_damage = player_damage1
heals_left = 3
heal_amount = 10


def heal_player(amount):
    global player_health

    player_health += amount
    player_health = player_health + amount


def attack_enemy(amount):
    global enemy_health
    enemy_health -= amount
    print('You hit the enemy with your bat!!!')


def attack_player(amount):
    global player_health
    player_health -= amount
    print('You were hit by the enemies bat! ')


print('A ' + enemy_name + ' has challenged you to a fight! ')
print()
while player_health > 0:
    print(enemy_name + ' HP: ' + str(enemy_health))
    print('Your HP: ' + str(player_health))
    print('Bandages left: ' + str(heals_left))
    print()
    action = input('Attack or heal? ')
    print()

    if action == "attack":
        player_roll = random.randint(1, 10)

        if player_roll < player_accuracy * 10:
            attack_enemy(player_damage)

            if enemy_health <= 0:
                print('You win, you beat (a) (the) ' + enemy_name +
                      '. You have received the potion!!!')
                break

        else:
            print('You missed your shot!')

    elif action == 'heal':
        if player_health == 80:
            print('You have full health, you cannot use a bandage.')
        else:
            if heals_left:
                heal_player(heal_amount)
                heals_left -= 1
            else:
                print('You are out of bandages!!')

    time.sleep(1)
    enemy_roll = random.randint(1, 10)
    if enemy_roll < enemy_accuracy * 10:
        attack_player(enemy_damage)

        if player_health <= 0:
            print('You got pummeled by the enemies bat.... :( ')
            break

    else:
        print(enemy_name + ' missed! ')

    print()
    print('******************')
    print()

if player_health <= 0:
    sp('You sadly lost against the ' + enemy_name + ', would you like to restart the battle?'
       )
    time.sleep(1)
    sp('Y/N')
    toy = input('      >>>>>>>  ').upper()
    toy = toy.upper()
    if toy == 'Y':
      sp('TOO BAD')

    elif toy == 'N':
      sp('Your loss')
      sys.exit()
elif enemy_health <= 0:
  print('You won!')
  time.sleep(2)
  os.system('clear')
  pass
  



    #Fix, set player to line to 276

sp('You got to live!!')
sp('2 Down, 2 to go!')
time.sleep(2)
os.system('clear')



print(yellow + """             
						Battle!!!""")

print(blue + "              PRESS ENTER")

blank = ''
inpt = input('')
if inpt == blank:
    os.system("clear")
elif input != blank:
    print(red + 'Please press Enter')
else:
    print(red + 'An Error occured.\nPress Enter')
time.sleep(2)
os.system('clear')

## Now, the game
enemies = [
    'Scar slave', 'scar follower', 'scar leader', 'scar fighter', 'scar spy'
]

enemy_name = random.choice(enemies)
enemy_health = 120
enemy_accuracy = 0.4
enemy_damage = 15

player_health = 80
player_accuracy = 0.8
player_damage = player_damage1
heals_left = 3
heal_amount = 10


def heal_player(amount):
    global player_health

    player_health += amount
    player_health = player_health + amount


def attack_enemy(amount):
    global enemy_health
    enemy_health -= amount
    print('You hit the enemy with your bat!!!')


def attack_player(amount):
    global player_health
    player_health -= amount
    print('You were hit by the enemies bat! ')


print('A ' + enemy_name + ' has challenged you to a fight! ')
print()
while player_health > 0:
    print(enemy_name + ' HP: ' + str(enemy_health))
    print('Your HP: ' + str(player_health))
    print('Bandages left: ' + str(heals_left))
    print()
    action = input('Attack or heal? ')
    print()

    if action == "attack":
        player_roll = random.randint(1, 10)

        if player_roll < player_accuracy * 10:
            attack_enemy(player_damage)

            if enemy_health <= 0:
                print('You win, you beat (a) (the) ' + enemy_name +
                      '. You have received the potion!!!')
                break

        else:
            print('You missed your shot!')

    elif action == 'heal':
        if player_health == 80:
            print('You have full health, you cannot use a bandage.')
        else:
            if heals_left:
                heal_player(heal_amount)
                heals_left -= 1
            else:
                print('You are out of bandages!!')

    time.sleep(1)
    enemy_roll = random.randint(1, 10)
    if enemy_roll < enemy_accuracy * 10:
        attack_player(enemy_damage)

        if player_health <= 0:
            print('You got pummeled by the enemies bat.... :( ')
            break

    else:
        print(enemy_name + ' missed! ')

    print()
    print('******************')
    print()

if player_health <= 0:
    sp('You sadly lost against the ' + enemy_name + ', would you like to restart the battle?'
       )
    time.sleep(1)
    sp('Y/N')
    toy = input('      >>>>>>>  ').upper()
    toy = toy.upper()
    if toy == 'Y':
      sp('TOO BAD')

    elif toy == 'N':
      sp('Your loss')
      sys.exit()
elif enemy_health <= 0:
  print('You won!')
  time.sleep(2)
  os.system('clear')
  pass
  



    #Fix, set player to line to 276

sp('You got to live!!')
sp('3 down, 1 to go!!')
time.sleep(2)
os.system('clear')



print(yellow + """             
						Battle!!!""")

print(blue + "              PRESS ENTER")

blank = ''
inpt = input('')
if inpt == blank:
    os.system("clear")
elif input != blank:
    print(red + 'Please press Enter')
else:
    print(red + 'An Error occured.\nPress Enter')
time.sleep(2)
os.system('clear')

## Now, the game
enemies = [
    'Scar slave', 'scar follower', 'scar leader', 'scar fighter', 'scar spy'
]

enemy_name = random.choice(enemies)
enemy_health = 120
enemy_accuracy = 0.4
enemy_damage = 15

player_health = 80
player_accuracy = 0.8
player_damage = player_damage1
heals_left = 3
heal_amount = 10


def heal_player(amount):
    global player_health

    player_health += amount
    player_health = player_health + amount


def attack_enemy(amount):
    global enemy_health
    enemy_health -= amount
    print('You hit the enemy with your bat!!!')


def attack_player(amount):
    global player_health
    player_health -= amount
    print('You were hit by the enemies bat! ')


print('A ' + enemy_name + ' has challenged you to a fight! ')
print()
while player_health > 0:
    print(enemy_name + ' HP: ' + str(enemy_health))
    print('Your HP: ' + str(player_health))
    print('Bandages left: ' + str(heals_left))
    print()
    action = input('Attack or heal? ')
    print()

    if action == "attack":
        player_roll = random.randint(1, 10)

        if player_roll < player_accuracy * 10:
            attack_enemy(player_damage)

            if enemy_health <= 0:
                print('You win, you beat (a) (the) ' + enemy_name +
                      '. You have received the potion!!!')
                break

        else:
            print('You missed your shot!')

    elif action == 'heal':
        if player_health == 80:
            print('You have full health, you cannot use a bandage.')
        else:
            if heals_left:
                heal_player(heal_amount)
                heals_left -= 1
            else:
                print('You are out of bandages!!')

    time.sleep(1)
    enemy_roll = random.randint(1, 10)
    if enemy_roll < enemy_accuracy * 10:
        attack_player(enemy_damage)

        if player_health <= 0:
            print('You got pummeled by the enemies bat.... :( ')
            break

    else:
        print(enemy_name + ' missed! ')

    print()
    print('******************')
    print()

if player_health <= 0:
    sp('You sadly lost against the ' + enemy_name + ', would you like to restart the battle?'
       )
    time.sleep(1)
    sp('Y/N')
    toy = input('      >>>>>>>  ').upper()
    toy = toy.upper()
    if toy == 'Y':
      sp('TOO BAD')

    elif toy == 'N':
      sp('Your loss')
      sys.exit()
elif enemy_health <= 0:
  print('You won!')
  time.sleep(2)
  os.system('clear')
  pass
  



    #Fix, set player to line to 276

sp('You got to live!!')
sp('You beat them!!!!')
time.sleep(2)
os.system('clear')
sp('"Fhew, that was a lot." Rachel said. " Yeah, and there is probably more coming." William said.  ')
time.sleep(2)
os.system('clear')
sp('They continue to walk down the hallway. ')


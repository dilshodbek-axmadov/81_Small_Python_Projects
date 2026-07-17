import random
import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

print("""
This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
""")

input("Press Enter to begin...")

player1 = input('Human player 1, enter your name: ')
player2 = input('Human player 2, enter your name: ')
player_names = player1[:11].center(11).title() + '   ' + player2[:11].center(11).title()

print('''Here are two boxes:

  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
''')
print()
print(player_names)
print(f"{player1.title()}, you have RED box in front of you")
print(f"{player2.title()}, you have GOLD box in front of you")
print()
print(f"{player1.title()}, you will get to look into your box.")
print(f"{player2.upper()}, close your eyes and don't look!!!")
input(f"When {player2.title()} has closed their eyes, press Enter...")
print()

print(f"{player1}, here is the inside of your box: ")
# Randomly initiate carrot to boxes
if random.randint(1,2)==1:
    carrot_in_first_box = True
else:
    carrot_in_first_box = False

if carrot_in_first_box:
    print('''
        ___VV____
       |   VV    |
       |   VV    |
       |___||____|    __________
      /    ||   /|   /         /|
     +---------+ |  +---------+ |
     |   RED   | |  |   GOLD  | |
     |   BOX   | /  |   BOX   | /
     +---------+/   +---------+/
      (carrot!)''')
    print(player_names)
else:
    print('''
        _________
       |         |
       |         |
       |_________|    __________
      /         /|   /         /|
     +---------+ |  +---------+ |
     |   RED   | |  |   GOLD  | |
     |   BOX   | /  |   BOX   | /
     +---------+/   +---------+/
     (no carrot!)''')
    print(player_names)

input("Press enter to continue...")
clear_screen() # clear the screen
print(f"{player1.title()} tell {player2.title()} to open their eyes")
input("Press Enter to continue...")

print()
print(f"{player1.title()}, say one of the following sentences to {player2.title()}.")
print('   1) There is a carrot in my box')
print('   2) There is not a carrot in my box')
print()
input("Press Enter to continue...")

print()
print(f"{player2.title()}, do you want to swap boxes with {player1.title()}? YES/NO")
while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(f"{player2.title()}, please enter YES or NO")
    else:
        break

first_box = 'RED '
second_box = 'GOLD'

if response.startswith('Y'):
    carrot_in_first_box = not carrot_in_first_box
    first_box, second_box = second_box, first_box

print('''HERE ARE THE TWO BOXES:
   __________     __________
  /         /|   /         /|
 +---------+ |  +---------+ |
 |   {}  | |  |   {}  | |
 |   BOX   | /  |   BOX   | /
 +---------+/   +---------+/'''.format(first_box, second_box))
print(player_names)

input("Press Enter to continue...")
print()

if carrot_in_first_box:
    print('''
       ___VV____      _________
      |   VV    |    |         |
      |   VV    |    |         |
      |___||____|    |_________|
     /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   {}  | |  |   {}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/'''.format(first_box, second_box))
else:
    print('''
        _________      ___VV____
       |         |    |   VV    |
       |         |    |   VV    |
       |_________|    |___||____|
      /         /|   /    ||   /|
     +---------+ |  +---------+ |
     |   {}  | |  |   {}  | |
     |   BOX   | /  |   BOX   | /
     +---------+/   +---------+/'''.format(first_box, second_box))

if carrot_in_first_box:
    print(f"{player1.title()} is the winner!")
else:
    print(f"{player2.title()} is the winner!")

print("Thanks for playing")
from random import randint
from room import Room
from item import Item
from character import Enemy
from character import Friend

# Set up Rooms
masterbr = Room('Master bedroom', 10, 10, 'blue')
masterbr.set_description('A rectangular room that is 2/3rds full of one giant bed.')

battle_room = Room('Battle Room', 20, 15, 'orange')
battle_room.set_description('It has a ring where you fight, and some stands for the people to sit and watch.')

kitchen = Room('Kitchen', 20, 15, 'yellow')
kitchen.set_description('It\'s an HGTV-fan\'s dream.')

dining_hall = Room('Dining Hall', 20, 25, 'blue')
dining_hall.set_description('Your typical college mess.')

ballroom = Room('Ballroom', 50, 25, 'gold')
ballroom.set_description('Cinderella would be in awe.')

masterbr.link_room(kitchen, "west")
kitchen.link_room(masterbr, "east")
kitchen.link_room(ballroom, "magic")
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(battle_room, "south")
dining_hall.link_room(ballroom, "west")
battle_room.link_room(dining_hall, "north")
battle_room.link_room(ballroom, "magic")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(kitchen, "magic")

kong = Item('Kong', 'Red')
kong.set_description( 'Cone-like rubber dog toy' )
kitchen.set_item(kong)

# Set up enemies
weakness1 = 'butter pecan ice cream'
weakness2 = 'flame thrower'
weakness3 = 'stethoscope'

lameweapons = ['wheel of brie', 'plate', 'peach', 'light-rail ticket', 'ladybug', 'mackerel']

evilapple = Enemy('Arnold the Apple', 'doctor-hating fruit')
evilapple.set_conversation('Eat doctors or I\'ll stay!')
evilapple.set_weakness(weakness3)
dining_hall.set_character(evilapple)

bbear = Enemy('Bombardier Bear', 'giant gummy bear')
bbear.set_conversation('Bomb\'s away!')
bbear.set_weakness(weakness2)
battle_room.set_character(bbear)

dave = Enemy('Dave', 'smelly zombie')
dave.set_conversation('UAhrhhjwblehajrkewaablhchshhghhrhrhw')
dave.set_weakness(weakness1)
kitchen.set_character(dave)

# Set up friends
apollo = Friend('Apollo', 'a young dog')
apollo.set_conversation('Arf!')
masterbr.set_character(apollo)

gil = Friend('Gil', 'leprechaun')
gil.set_conversation('Top \'o the mornin\' to ye!')
gil.set_superpower(weakness2)
ballroom.set_character(gil)

artemis = Friend('Artemis', 'sparkly UniKitty')
artemis.set_conversation('Hiiiiii!!!!!!! I am SO glad to see you.')
artemis.set_superpower(weakness1)
ballroom.set_character(artemis)

# Set up starting conditions
current_room = kitchen
alive = True

# Define functions

def challenge_to_fight():
    if inhabitant is None or isinstance(inhabitant, Friend):
        print('There are no enemies here.')
        print('\n')
    else:
        index = randint(0, len(lameweapons)-1)
        option_b = lameweapons[index]
        command = input("""
What do you want to fight %s with?

    a) A %s
    b) A %s

Choose: """ % (inhabitant.name, inhabitant.weakness, option_b))
        if command == 'a':
            weapon = inhabitant.weakness
        elif command == 'b':
            weapon = option_b
        player_wins = inhabitant.fight(weapon)
        if player_wins == True:
            global current_room
            current_room.set_character(None)
        elif player_wins == False:
            global alive
            alive = False
            print( '   --- GAME OVER ---\n' )
 
# Play the game

print('\n')
print("""
Welcome to the Herberts\' Great Adventure!

_________________________ ô,ô ___________________________

Object of the game: Laugh and smile.

How to play:
1. Move from room to room: north, south, east, or west
2. Interact with characters: talk, hug, gift, or fight

Have fun!
""")

while alive == True:

    print('\n')
    current_room.get_details()
    inhabitant = current_room.get_character()
    
    command = input('What do you want to do? ')

    print ('\n')

    if command in ['north', 'south', 'east', 'west', 'magic']:
        # Move in direction entered
        current_room = current_room.move(command)

    elif command == 'talk':
        if inhabitant is not None:
            print ('\n')
            inhabitant.talk()
            print ('\n')
        else:
            print( 'Sorry, there is no one else here. Guess you have to talk to yourself.')
            print('\n')

    elif command == 'fight':
        challenge_to_fight()

    elif command == 'hug':
        if inhabitant is not None and isinstance(inhabitant, Friend):
            print ('\n')
            inhabitant.hug()
            print ('\n')
        elif inhabitant is not None and isinstance(inhabitant, Enemy):
            print ('\n')
            print ('You hugged %s the %s! You are far too friendly for your own good.' % (inhabitant.name, inhabitant.description))
            print ('\n')
            inhabitant.set_conversation(None)
        else:
            print('There is no one here to hug.')
            print('\n')

    elif command == 'gift':
        if inhabitant is not None:
            print ('\n')
            inhabitant.gift()
            print ('\n')
            inhabitant.set_conversation(None)
        else:
            print('There is no one here to receive your gift.')
            print('\n')

    else:
        print( """
    I don\'t understand that request. 
    
    Here are your options.

    1. Move from room to room: north, south, east, or west
    2. Interact with characters: talk, hug, gift, or fight
        """)

from room import Room
from item import Item
from character import Enemy
from character import Friend

# Set up Rooms
kitchen = Room('Kitchen', 20, 15, 'yellow')
kitchen.set_description('It\'s an HGTV-fan\'s dream')

dining_hall = Room('Dining Hall', 20, 25, 'blue')
dining_hall.set_description('Your typical college mess')

ballroom = Room('Ballroom', 50, 25, 'gold')
ballroom.set_description('Cinderella would be in awe')

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

kong = Item('Kong', 'Red')
kong.set_description( 'Cone-like rubber dog toy.' )

# Set up enemies and friends
dave = Enemy('Dave', 'smelly zombie')
dave.set_conversation('UAhrhhjwblehajrkewaablhchshhghhrhrhw')
dave.set_weakness('cricket bat')
kitchen.set_character(dave)

artemis = Friend('Artemis', 'sparkly unikitty')
artemis.set_conversation('Hiiiiii!!!!!!! I am SO glad to see you.')
artemis.set_superpower('cricket bat')
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
        command = input("""
What do you want to fight %s with?
a) A cricket bat
b) A wedge of parmesan
> """ % (inhabitant.name))
        if command == 'a':
            weapon = 'cricket bat'
        elif command == 'b':
            weapon = 'cheese'
        if inhabitant.fight(weapon) == True:
            print('\n')
            print( '(¯`·._.·(¯`·._.· Hooray! You live to fight another day. ·._.·´¯)·._.·´¯)')
            print('\n')
            global current_room
            current_room.set_character(None)
        elif inhabitant.fight(weapon) == False:
            global alive
            alive = False
            print( 'Game Over' )
 
# Play the game

print('\n')
print("""
Welcome to the Herberts\' Great Adventure!

_________________________ ô,ô ___________________________

Object of the game: Have fun!

How to play:
1. Move from room to room by entering \'north\', \'south\', \'east\', or \'west\'
2. To hear what the character in the current room has to say, enter \'talk\'
3. When you meet an enemy, enter \'fight\'

""")

while alive == True:

    print('********')
    print('\n')
    current_room.get_details()
    inhabitant = current_room.get_character()
    
    command = input('What do you want to do? ')

    print ('\n')

    if command in ['north', 'south', 'east', 'west']:
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

    else:
        print( 'I don\'t understand that request.' )
        print ('\n')

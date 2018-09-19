from room import Room
from item import Item
from character import Enemy

# Set up Rooms
kitchen = Room('Kitchen', 20, 15, 'yellow')
kitchen.set_description('An HGTV-fan\'s dream')

dining_hall = Room('Dining Hall', 20, 25, 'blue')
dining_hall.set_description('Your typical college mess.')

ballroom = Room('Ballroom', 50, 25, 'gold')
ballroom.set_description('Cinderella would be in awe')

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

kong = Item('Kong', 'Red')
kong.set_description( 'Cone-like rubber dog toy.' )

# Set up enemy Dave
dave = Enemy('Dave', 'smelly zombie')

dave.set_conversation('UAhrhhjwblehajrkewaablhchshhghhrhrhw')
dave.set_weakness('cricket bat')

kitchen.set_character(dave)

# Define functions

def challenge_to_fight():
    command = input('What do you want to fight %s with: a) A cricket bat? b) A wedge of parmesan? > ' % (inhabitant.name) )
    if command == 'a':
        weapon = 'cricket bat'
    elif command == 'b':
        weapon = 'cheese'
    if inhabitant.fight(weapon) == True:
        print( 'Hooray! You live to fight another day. ')
        dead = False
    elif inhabitant.fight(weapon) == False:
        print( 'Game Over' )
        return True    

dead = False

# Play the game

current_room = kitchen

while dead == False:

    current_room.get_details()
    inhabitant = current_room.get_character()

    command = input('You can talk; fight; or enter a direction to move rooms. What do you want to do? ')

    print ('\n')

    if command in ['north', 'south', 'east', 'west']:
        # Move in direction entered
        current_room = current_room.move(command)

    elif command == 'fight':
        challenge_to_fight()
        if challenge_to_fight() == True:
            dead = True
    
    elif command == 'talk':
        if inhabitant is not None:
            print ('\n')
            inhabitant.talk()
            print ('\n')
            
        else:
            print( 'Sorry, there is no one else here. Guess you have to talk to yourself.')
    else:
        print( 'I don\'t understand that request.' )
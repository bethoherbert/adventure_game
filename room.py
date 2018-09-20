class Room():
    # Create a room
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = []
        self.item = []

    # Set room attributes
    def set_description(self, room_description):
        self.description = room_description

    def set_item(self, item_name):
        self.item.append(item_name)

    def set_character(self, char_name):
        self.character.append(char_name)

    def set_name(self, room_name):
        self.name = room_name

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    # Get room attributes
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    # Print room details
    def get_details(self):
        print('You are here: %s' % (self.name.upper()))
        print('------------------------')
        print(self.description)
        for direction in self.linked_rooms:
            if direction is not 'magic':
                room = self.linked_rooms[direction]
                direction = direction.title()
                print('The %s is to the %s.' % (room.get_name(), direction))

        if self.get_item is not None:
            for i in range(0, len(self.item)):
                self.item[i].describe()
        
        else:
            print('')
        if self.character is not None:
            for i in range(0, len(self.character)):
                self.character[i].describe()
            print('\n')
        else:
            print('No one else is in here with you.')
            print('------------------------')
            print('\n')

    # Move to another room    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print( 'You can\'t go that way' )
            return self
    
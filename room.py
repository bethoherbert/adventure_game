class Room():
    # Create a room
    def __init__(self, room_name, length, width, room_color):
        self.name = room_name
        self.length = length
        self.width = width
        self.color = room_color
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    # Set room attributes
    def set_description(self, room_description):
        self.description = room_description

    def set_item(self, item_name):
        self.item = item_name

    def set_character(self, char_name):
        self.character = char_name

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
        item = self.get_item()
        if item is not None:
            item.describe()
        else:
            print('')
        inhabitant = self.get_character()
        if inhabitant is not None:
            inhabitant.describe()
            print('\n')
        else:
            print('------------------------')
            print('\n')

    # Move to another room    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print( 'You can\'t go that way' )
            return self
    
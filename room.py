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

    # Set room attributes
    def set_description(self, room_description):
        self.description = room_description

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

    # Print room details
    def get_details(self):
        print( 'You\'re now in the %s: %s.' % (self.name, self.description) )
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            direction = direction.title()
            print( 'To the %s is the %s.' % (direction, room.get_name()))
        inhabitant = self.get_character()
        if inhabitant is not None:
            inhabitant.describe()
            return inhabitant
    
        
    # Move to another room    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print( 'You can\'t go that way'  )
    
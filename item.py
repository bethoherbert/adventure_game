class Item():
    # Create an item
    def __init__(self, item_name, item_color):
        self.name = item_name
        self.color = item_color
        self.description = None
        self.contents =[]
    
    # Set item attributes
    def set_description(self, item_description):
        self.description = item_description

    def set_contents(self, item):
        self.contents.append(item)

    def set_color(self, item_color):
        self.color = item_color

    # Get item attributes
    def describe(self):
        print( '\n /o/ In this room, there is a %s %s.' % (self.color, self.name) )

    def get_description(self):
        return self.description
    
    def get_name(self):
        return self.name
    
    def get_contents(self):
        return self.contents    

    # Grab backpack
    def grab(self, room):
        room.item.remove(self)
        print('The backpack is all yours! You can now collect items as you go.')

    # Collect items
    def collect(self, room):
        room.item.remove(self)
        backpack.contents.append(self)
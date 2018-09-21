class Item():
    # Create an item
    def __init__(self, item_name, item_color):
        self.name = item_name
        self.color = item_color
        self.description = None
    
    # Set item attributes
    def set_description(self, item_description):
        self.description = item_description

    def set_color(self, item_color):
        self.color = item_color

    # Get item attributes
    def describe(self):
        print( '\n /o/ In this room, there is a %s %s.' % (self.color, self.name) )

    def get_description(self):
        return self.description
    
    def get_name(self):
        return self.name
    
    # Grab backpack
    def grab(self, room):
        room.items.remove(self)
        print('The backpack is all yours! You can now collect items as you go.')

    # Collect items

class Backpack(Item):

    # Create a backpack; set and get contents
    def __init__(self, item_name, item_color):

        super().__init__(item_name, item_color)
        self.contents = []

    def set_contents(self, item):
        self.contents.append(item)

    def get_contents(self):
        return self.contents    

    def describe_contents(self):
        for i in range(0, len(self.contents)):
            print(self.contents[i])

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

    def set_name(self, item_name):
        self.name = item_name

    # Get item attributes
    def get_description(self):
        return self.description    
    
    def get_name(self):
        return self.name
    
    # Print item details
    def get_details(self):
        print ( self.color )
        print ( self.name )
        print ( self.description )


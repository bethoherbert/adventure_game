class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( 'There\'s a %s named %s in here!' % (self.description, self.name) )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print(self.name + ' says: ' + self.conversation)
        else:
            print(self.name + 'is speechless.')

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Friend(Character):

    # Create a friend
    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.superpower = None

   # Set friend attributes
    def set_superpower(self, weakness):
        self.superpower = weakness

    # Get friend attributes
    def get_superpower(self):
        return self.superpower

class Enemy(Character):

    # Create an enemy
    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.weakness = None

    # Set enemy attributes
    def set_weakness(self, weakness):
        self.weakness = weakness

    # Get enemy attributes
    def get_weakness(self):
        return self.weakness
    
    # Fight with this enemy
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print('\n')
            print("You fend %s off with the %s!" % (self.name, self.weakness))
            return True
        else:
            print('%s crushes you, you puny adventurer!' % (self.name))
            return False


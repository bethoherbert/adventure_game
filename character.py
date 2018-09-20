class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( '\n /o/ There\'s a %s named %s in here!' % (self.description, self.name) )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print(self.name + ' says: ' + self.conversation)
        else:
            print(self.name + ' is speechless.')

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    # Give this character a gift
    def gift(self):
        print('%s says thank you!' % (self.name) )

class Friend(Character):

    # Create a friend
    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.superpower = None

   # Set friend attributes
    def set_superpower(self, power):
        self.superpower = power

    # Get friend attributes
    def get_superpower(self):
        return self.superpower
    
    # Hug your friend
    def hug(self):
        print('(っO ^ O)っ %s hugs you back! (っO ^ O)っ' % (self.name) )

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
            print( '(¯`·._.·(¯`·._.· Hooray! ·._.·´¯)·._.·´¯)')
            print('\n')
            print("You vanquished %s with the %s!" % (self.name, self.weakness))
            return True
        else:
            print('\n')
            print( '_.·._.·*^*·. BOOM! .·*^*·._.·._')
            print('\n')
            print('%s is no match for a %s! %s crushes you, you puny adventurer!' % (combat_item.title(), self.description, self.name))
            print('\n')
            return False


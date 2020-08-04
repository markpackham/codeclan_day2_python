from person import *


class Agent(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)

    def talk(self):
        return "The names Bond, James Bond"


new_agent = Agent("Agent", "X")
print(new_agent.talk())
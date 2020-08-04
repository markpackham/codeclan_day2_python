from person import *


class Agent(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)

    # This will get overidden by the one below
    def talk(self):
        return "The names Bond, James Bond"

    # The bottom one takes overrides the top
    def talk(self):
        return f"The names {self.last_name}, {self.first_name} {self.last_name}"


new_agent = Agent("Agent", "X")
print(new_agent.talk())

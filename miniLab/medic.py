from person import *

class Medic(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)

    def heal(self):
        return "You are healed"

new_medic = Medic("Dr","Doom")
print(new_medic.heal())
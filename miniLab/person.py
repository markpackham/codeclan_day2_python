class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def talk(self):
        return f"My name is {self.first_name} {self.last_name}"
    
new_person = Person("Bob","Smith")
print(new_person.talk())
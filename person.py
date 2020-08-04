class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        return f"Hi my name is {self.name} and I am {str(self.age)}!"

new_person = Person("Mark",19)
print(new_person.name)
print(new_person.age)
print(new_person.talk())
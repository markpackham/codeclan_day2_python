class Car:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed
    def start(self):
        return "Vrooom vroom!"

new_car = Car("Racey","Ford",300)
print(new_car.start())
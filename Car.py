# dependencia (mi clase auto depende de la clase persona)
from Person import Person


class Car:

    color = str
    owner = Person

    def __init__(self, owner: Person, color: str):
        self.owner = owner
        self.color = color

    def paint(self, color):
        self.color = color

    def transfer(self, new_owner: Person):
        if new_owner.return_age() >= 18:
            self.owner = new_owner
            # de esta manera se puede manejar un metodo dentro de otro metodo.
            self.print_attributes()
        else:
            print("You need 18 years or more")

    def print_attributes(self):
        print(f"This car is from {self.owner.return_name()} and your city is {self.owner.return_city()}")


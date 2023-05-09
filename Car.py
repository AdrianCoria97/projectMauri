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
            print("Transfer Realized")
        else:
            print("You need 18 years or more")

    def print_attributes(self):
        print(f'This car is from {self.owner.return_name()} and your city is {self.owner.return_city()}.')


# >>>>>HERENCIA<<<<

class Ambulance(Car):

    is_available: bool = True

    def ambulance_type(self, ambulance_type):
        return f'The ambulance is of type: {ambulance_type}, and the color is {self.color}'

    # sobre escritura de metodo (se vuelve a definir tode el metodo)
    # con el super se utiliza el metodo de la clase padre "sobre carga de metodo"
    def print_attributes(self):
        super().print_attributes()
        print("This ambulance is available ? " + str(self.is_available))

    def transfer(self, new_owner): # Person <<<<<<<<<
        if new_owner.return_age() >= 18 and new_owner.has_license():
            self.owner = new_owner
            self.print_attributes()
            print("Transfer Realized")
        elif new_owner.return_age() < 18:
            print("You need to be over 18, thanks")
        else:
            print("You need professional license and need to be over 18")






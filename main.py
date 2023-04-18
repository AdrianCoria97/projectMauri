from Car import Car
from Person import Person

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    name = input("name of person: ")
    city = input("city of person: ")
    identification = input("number of the identification: ")
    age = input("your age: ")
    color_car = input("Color car is: ")

    # parametros posicionales y parametros nombrados
    doctor = Person(name=name, city=city, identification_number=identification, age=age)
    fiat = Car(color=color_car, owner=doctor)
    new_proprietary = Person("Adrian", "Junin", 511951, 18)

    fiat.print_attributes()
    fiat.transfer(new_proprietary)

    print(doctor.return_name())
    print(doctor.return_city())



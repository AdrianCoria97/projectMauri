from Car import Car, Ambulance
from Person import Person

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    #
    name = input("name of person: ")
    city = input("city of person: ")
    identification = input("number of the identification: ")
    age = input("your age: ")
    professional_license = input("Do you have a professional license?")
    color_car = input("Color car is: ")
    
    # >>>>>>>OBJETOS<<<<<<<<<<< 
    # parametros posicionales y parametros nombrados
    doctor = Person(name=name, city=city, identification_number=identification, age=age, professional_license=professional_license)
    fiat = Car(color=color_car, owner=doctor)
    new_proprietary = Person("Adrian", "Junin", 511951, 18, True)

    fiat.print_attributes()
    fiat.transfer(new_proprietary)
    
    """
    # >>>>>>>>OBJETOS DE HERENCIA<<<<<<<<<<

    conductor = Person(name="Juan", city="NY", identification_number=15406423, age=23, professional_license=False)
    ambulance = Ambulance(color="red and white", owner=conductor)

    # metodos de Car (sobre escritura y sobrecarga con super)
    ambulance.print_attributes()
    # metodos de Ambulance
    print(ambulance.ambulance_type("van"))

    new_proprietary_ambulance = Person(name="Mauri", city="San Martin", identification_number=2634557788, age=18, professional_license=True)
    new_car = Ambulance(color="red and white", owner=new_proprietary_ambulance)
    new_car.transfer(new_proprietary_ambulance)

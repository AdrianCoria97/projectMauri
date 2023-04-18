
class Person:

    # Este es un atributo privado
    __name = str
    city = str
    identification_number = int
    __age = int

    def __init__(self, name, city, identification_number, age):
        self.city = city
        self.__name = name
        self.identification_number = identification_number
        self.__age = age

    # getter
    def return_age(self) -> int:
        return self.__age

    # principios de encasulamiento(este metodo no puede ser llamado desde otra clase) __
    def return_name(self):
        return self.__name

    def return_city(self):
        return self.city

    # de esta manera se puede desencapsular
    # def test(self):
        # self.__return_name()

class Car:
    def __init__(self, brand, model, color):
        self.__brand = brand
        self.model = model
        self._color = color

    def get_details(self):
        return f"""brand: {self.__brand}
model: {self.model}
color: {self._color}"""

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def __private_method(self):
        pass

    def _protected_method(self):
        pass


car1 = Car("maruthi", "alto", "red")
print(car1.get_details())

car1.set_brand("maruthi suzuki")

print(car1.get_details())
#print(car1.__brand)
print(car1._color)

# object._class__variable
print(car1._Car__brand)
car1._protected_method()
#car1.__private_method()



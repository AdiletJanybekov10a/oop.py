#Encapsulation

class Kettle:
    
    def turn_on(self):
        print('Нажали кнопку')
        self.__boil()
        self.__check_temperature()
        self.__beep()
        self.__turn_off()

    def __boil(self):
        print("разогревание воды")

    def __check_temperature(self):
        print("Проверям температуры воды")
    
    def __beep(self):
        print("Подаем звуковой сигнал")
    
    def __turn_off(self):
        print("Автомотическое выключение")
    
my_kettle = Kettle()
my_kettle.turn_on()

#__init__ 
#__new__

#Polymorphism

class Animal:
    
    legs = 4
    tail = 1 

    def voice(self):
        print("Какой-то звук")


class Cat(Animal):

    def voice(self):
        print("Мяу-мяу")


class Dog(Animal):

    def voice(self):
        print("Гав-гав")


class Bull(Animal):

    def voice(self):
        print("Мууу")


cat1, cat2 = Cat(), Cat()
dog1, dog2 = Dog(), Dog()
bull1, bull2 = Bull(), Bull()

farm_band = [cat1, cat2, dog1, dog2, bull1, bull2]

for i in farm_band:
    i.voice()
    


#Inheritance

class Person:

    def can_breathe(self):
        print("Я могу дышать")

    def can_walk(self):
        print("Я могу ходить")

class Doctor(Person):
    
    def can_cure(self):
        print("Я могу лечить")
    
class Architect(Person):

    def can_build(self):
        print("Я могу постороить здание")

d = Doctor()
d.can_cure()
d.can_walk()
d.can_breathe()

a = Architect()
a.can_build()
a.can_walk()
d.can_breathe()









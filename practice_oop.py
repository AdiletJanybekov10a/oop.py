# class Person:

#     def __init__(self, name, age ):
#         self.name = name 
#         self.age = age 

#     def __str__(self):
#         return f"{self.name}, {self.age}"

#     def say_my_name(self):
#         return f"Hello, {self.name}"

# class Student(Person):
#     def __init__(self, grades):
#         self.__grades = grades
    
#     def __str__(self):
#         return self.grades 

#     def show_grades(self):
#         return self.grades

# person = Person('beks', 16)
# student 
    
#Task_1
class Group:
    def __init__(self, Vadim, Marat, Maksat):
        self.Vadim = Vadim
        self.Marat = Marat
        self.Maksat = Maksat

    def __str__(self):
        return f"{self.Vadim}, {self.Marat}, {self.Maksat}"

dodicks = Group("Korean", "Harry Potter", "Ulukmanapo")
print(dodicks)
        

#Task_2
class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
	    print('I am climbing the tree')

first = Monkey()
first.climb()
print(Monkey.max_age)
print(Monkey.loves_bananas)

second = Monkey()
second.climb()
print(Monkey.max_age)
print(Monkey.loves_bananas)

#Task_3
# Создайте класс Person. 
# При создании экземпляра данного класса мы должны вводить 3 парамметра name, age, gender.
# Напишите метод calculate_age к этому классу,
# этот метод должен принимать в себя число и возвращать
# в каком возрасте будет человек через это число лет.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def calculate_age(self, A):
        self.A = A

    def __str__(self):
        return f"age of {self.name} will be {self.A + self.age}"

a = Person("Adilet", 18, "male")
a.calculate_age(10)
print(a)



        
        
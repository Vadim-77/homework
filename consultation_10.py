1# from unicodedata import name


# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

# person = Person('Vadim', 'Nyu', 17)

# print(f'Имя: {person.name}, Фамилия: {person.surname}, Возраст: {person.age}')





2# class Monkey:
#     max_age = 12
#     loves_bananas = True

#     def climb(self):
#         print('I am climbing the tree')

# monkey = Monkey()
# print(monkey.max_age)
# print(monkey.loves_bananas)
        
# a = Monkey()
# a.climb()

# b = Monkey()
# b.climb()





3# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def calculate_age(self, number):
#         self.number = number

#     def __str__(self):
#         return f'Через {self.number} года будет {self.age + self.number} лет'
    
# a = Person('vadim', 17, 'male')
# a.calculate_age(3)
# print(a)





import unittest
from rectangles import Rectangle



class TestCubes (unittest.Testcase):
    def test_init(self):
        c = Rectangle(5, 3, 10)
        self.assertEqual (c.length, 5) 
        self.assertEqual(c.width, 3) 
        self.assertEqual(c.height, 10)

    def test_init_raise(self):
        with self.assertRaises(ValueError):
            c = Rectangle('length', (1, 2, 3), {4: 5})

    def test_negative_value (self):
        with self.assertRaises(ValueError) as context:
            c = Rectangle(-1, 2, 6)

    def test_volume_calculation(self):
        c = Rectangle(5, 4, 7)
        self.assertEqual(c.calculate_volume(), 140)

class Rectangle:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_valume(self):
        return self.length * self.width * self.height

a = Rectangle(5, 4, 7)
print(a.calculate_valume())


unittest.main()

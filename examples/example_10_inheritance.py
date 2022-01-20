from math import pi
from operator import le
from turtle import shape

class Shape(object):
    def area(self):
        raise NotImplemented

    def circumference(self):
        raise NotImplemented
    
    def __str__(self):
        return type(self).__name__


class Circule(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return pi * self.r ** 2

    def circumference(self):
        return 2 * pi * self.r

class Rectangle(Shape):
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def area(self):
        return self.l * self.w

    def circumference(self):
        return 2 * self.l + 2 * self.w    

class Square(Rectangle):
    def __init__(self, length):
        super().__ini__(length, length)


if __name__ == '__main__':
    shapes = [Square(10), Circule(20), Rectangle(3.4, 1.5)]

    for shape in shapes:
        print(f'{shape} area is {shape.area()}')

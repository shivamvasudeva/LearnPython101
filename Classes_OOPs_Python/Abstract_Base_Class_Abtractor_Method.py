#if i want to make sure that no one can make class with having area as method
#ABC is a module
#ABC MetaClass : if we use this it will give child class instructions that it must have metioned methods

from abc import ABCMeta, abstractmethod #python --version 3.6
from abc import ABC, abstractmethod #:  We can use this as well above 3.5 pythn version
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
class Rect(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.len  = 100
        self.bre = 200
    def printarea(self):
        return self.len *self.bre

rec1 = Rect()
print(rec1.printarea())
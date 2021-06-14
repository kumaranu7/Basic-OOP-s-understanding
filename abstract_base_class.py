#An abstract base class is a class which doesn't have defination on its own, it has abstract methods which forces the implementation in its
#derived classes

#here abstract base class is shape, now in order to make this class as abstract base class you need to make this as an instance of another class which
#called ABCMeta

#abc class won't have defination, it will only contain abstract methods

from abc import ABCMeta, abstractmethod
class Shape(metaclass=ABCMeta):
    @abstractmethod   #this decorator makes area as abstract method
    def area(self):
        return 0

#if area will not be defined in the below two classes it will throw an error, so in other words it makes us sure to implement are 

class square(Shape):
    side = 4
    def area(self):
        print("Area of square:", self.side * self.side)
class Rectangle(Shape):
    width = 5
    length = 10
    def area(self):
        print('Area of rectangle:', self.width * self.length)
    
Square = square()
Rect = Rectangle()
Square.area()
Rect.area()
    
#An abstract class cannot instantiate object for itself, an abstract class can only be inherited in its derived classes

        
        
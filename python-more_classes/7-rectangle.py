#!/usr/bin/python3
""" 2-rectangle module """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value:
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            self.__width = 0

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height < 1 or self.__width < 1:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        a = self.print_symbol * self.width
        for h in range(0, self.height - 1):
            for w in range(0, self.width):
                print(self.print_symbol, end="")
            print()
        return a

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        del(self)

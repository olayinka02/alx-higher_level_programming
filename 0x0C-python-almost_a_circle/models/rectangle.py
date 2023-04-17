#!/usr/bin/python3
"""
Contains the "Rectangle" class
"""

from models.base import Base


class Rectangle(Base):
    """A representation of a rectangle"""
    def __init__(self, width, height, p=0, q=0, id=None):
        """Initialing the parameters for rectangle"""
        self.width = width
        self.height = height
        self.p = p
        self.q = q
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @property
    def p(self):
        """getter for p"""
        return self.__p

    @property
    def q(self):
        """getter for q"""
        return self.__q

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @p.setter
    def p(self, value):
        """setter for p"""
        if type(value) is not int:
            raise TypeError("value of p must be an integer")
        if value < 0:
            raise ValueError("value of p must be >= 0")
        self.__p = value

    @q.setter
    def q(self, value):
        """setter for q"""
        if type(value) is not int:
            raise TypeError("value of q must be an integer")
        if value < 0:
            raise ValueError("value of q must be >= 0")
        self.__q = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print a display of the rectangle"""
        print(("\n" * self.__q) +
              "\n".join(((" " * self.__p) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__p,
                                                                 self.__q,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 2:
                    self.height = j
                elif i == 3:
                    self.p = j
                elif i == 4:
                    self.q = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "p" in kwargs:
                self.p = kwargs["p"]
            if "q" in kwargs:
                self.q = kwargs["q"]

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["p"] = self.p
        d["q"] = self.q
        return d

#!/usr/bin/python3
"""
This module contains the "Square" class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a square"""
    def __init__(self, size, p=0, q=0, id=None):
        """initializes the square"""
        super().__init__(size, size, p, q, id)
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """informal string representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.p,
                                                         self.q, self.width)

    def update(self, *args, **kwargs):
        """update attributes"""
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.p = kwargs["p"]
            if "y" in kwargs:
                self.q = kwargs["q"]

    def to_dictionary(self):
        """dictionary representation of a Square"""
        dResult = {}
        dResult["id"] = self.id
        dResult["size"] = self.size
        dResult["p"] = self.p
        dResult["q"] = self.q
        return d

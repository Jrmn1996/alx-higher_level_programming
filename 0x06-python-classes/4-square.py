#!/usr/bin/python3
"""square module"""

class Square:
    """define a square"""
    
    def __init__(self, size=0):
        """constructor
        arguments:
            size: length of square's side
        """
        self.size = size
    @property
    def size(self):
        """property for the len of a side of the square
        raises:
        TypeError: if size isn't an integer
        ValueError: if size < 0
        """
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    def area(self):
        """area of square
        return:
        size squared
        """
        return self.__size ** 2

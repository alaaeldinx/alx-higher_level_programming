#!/usr/bin/python3
"""
Defining a Square class
"""


class Square:
    """
    Defining a self call
    Args:
        size: length of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initailizing for square
        Args:
            size: length of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 1):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """
        A function to find area of Square
        Return: the size squared
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        a function to return square size
        Return: size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        a function to set property of Square
        Args: size => length of square
        Raise:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        a function to retreive position
        Return: position of square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        function to set value for position
        Args: value => position for square
        Raise: TypeError("position must be a tuple of 2 positive integers")
        """
        if ((not isinstance(value, tuple))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not (isinstance(value[0], int) and isinstance(value[1], int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        function that prints in stdout the square with the character #
        """
        if (self.__size == 0):
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(end=" ")
                print("#"*self.__size)

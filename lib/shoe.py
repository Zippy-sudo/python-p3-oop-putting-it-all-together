#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand="Ngucci", size=1000000):
        self.brand = brand
        self.size = size

    @property
    def brand(self):
        """Get the Brand Name"""
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        """Get the Shoe Size"""
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"
    
    @property
    def condition(self):
        """Get the shoe condition"""
        return self._condition
    
    @condition.setter
    def condition(self, condition):
        self._condition = condition

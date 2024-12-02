#!/usr/bin/env python3
import ipdb

class Book:
    
    def __init__(self, title="New Book", page_count = 0):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        """Get Book Title"""
        return self._title
    
    @title.setter
    def title(self, title):
        """"Set Book Title"""
        self._title = title

    @property
    def page_count(self):
        """Get Book Page Count"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        """Set Book Page Count"""
        if type(page_count) == type(int()):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        


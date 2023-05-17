#!/usr/bin/env python3
"""BaseCaching module

This module provides the base caching functionality
for other caching classes.
It defines the `BaseCaching` class which serves as
the parent class for caching systems.

Classes:
- BaseCaching: Parent class for caching systems.

"""

from base_caching import BaseCaching
"""import parent file"""


class BasicCache(BaseCaching):
    # BasiccCache Object
    """ BasicCache inherits the BaseChaching blueprint
    Methods:
         __init__(self) initialize  self
         print_cache(self) print values
    """
    def __init__(self):
        """ define an __init__ method,
        this __init__ method is called when a new object
        of the class BasicCache is created """
        self.cache_data = {}
        """ initialized cache_data variable,
        which is an empty dictionary used to
        store data in the cache (a smaller and faster storage)
        """

    def print_cache(self):
        """ define a print_cache funtion of the object cache_data"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ defines a put function that allows items
        be put in the dictionary

        Args:
            key (str): Description of key.
            item (str): Description of item

        Returns:
            Nothing: if key not in dictionary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ define a funtion to allow items be gotten
         Args:
            key (str): Description of key.
            item (str): Description of item

        Returns:
            None: if key not in dictionary
            value: if key in dicitionary
        """
        if key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]

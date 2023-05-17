#!/usr/bin/env python3

"""caching """
from base_caching import BaseCaching
"""import parent file"""


class BasicCache(BaseCaching):
    """ BasicCache inherits the BaseChaching blueprint """
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
        """ define a put function that allows items
        be put in the dictionary """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ define a funtion to allow items be gotten """
        if key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]

#!/usr/bin/env python3
"""LIFO Cache module

This module provides the LIFO (Last-In-First-Out) caching functionality.
It defines the `LIFOCache` class that inherits from `BaseCaching`.

Classes:
- LIFOCache: Caching system that uses the LIFO algorithm.

"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class"""

    def __init__(self):
        """Initializes a new instance of LIFOCache"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache"""
        # Implementation goes here

    def get(self, key):
        """Retrieves an item from the cache"""
        # Implementation goes here

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(last_key)
            print("DISCARD:", last_key)

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]

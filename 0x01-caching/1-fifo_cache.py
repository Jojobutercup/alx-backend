#!/usr/bin/env python3
"""FIFO Cache module

This module provides the FIFO (First-In-First-Out) caching functionality.
It defines the `FIFOCache` class that inherits from `BaseCaching`.

Classes:
- FIFOCache: Caching system that uses the FIFO algorithm.

"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache class"""

    def __init__(self):
        """Initializes a new instance of FIFOCache"""
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
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print("DISCARD:", first_key)

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]

#!/usr/bin/env python3
"""3-lru_cache

This module implements the LRUCache class,
which is a caching system based on the LRU algorithm.

"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class

    Inherits from BaseCaching and implements
    a caching system using the LRU algorithm.

    """

    def __init__(self):
        """Initializes the LRUCache instance"""
        super().__init__()
        self.lru_list = []

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                discard_key = self.lru_list[0]
                self.cache_data.pop(discard_key)
                self.lru_list.pop(0)
                print("DISCARD:", discard_key)

        if key in self.lru_list:
            self.lru_list.remove(key)

        self.lru_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        if key in self.lru_list:
            self.lru_list.remove(key)

        self.lru_list.append(key)
        return self.cache_data[key]

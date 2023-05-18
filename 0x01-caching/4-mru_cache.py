#!/usr/bin/env python3
"""
MRU Cache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU Cache class
    """

    def __init__(self):
        """
        Initializes the MRU Cache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = max(self.cache_data, key=self.cache_data.get)
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]

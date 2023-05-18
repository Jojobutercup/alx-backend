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
        self.recently_used_keys = []

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.recently_used_keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.recently_used_keys.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.recently_used_keys.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.recently_used_keys.remove(key)
        self.recently_used_keys.append(key)

        return self.cache_data[key]

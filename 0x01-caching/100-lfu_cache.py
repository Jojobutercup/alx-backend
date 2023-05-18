#!/usr/bin/env python3
"""
LFU Cache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Cache class
    """

    def __init__(self):
        """
        Initializes the LFU Cache instance
        """
        super().__init__()
        self.frequency = {}
        self.min_frequency = 1

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq_keys = [
                    k for k, v in self.frequency.items()
                    if v == self.min_frequency
                ]
                if min_freq_keys:
                    lru_key = min_freq_keys.pop(0)
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD:", lru_key)
                else:
                    lru_key = min(self.frequency, key=self.frequency.get)
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.min_frequency = 1

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1

        return self.cache_data[key]

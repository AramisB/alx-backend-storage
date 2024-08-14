#!/usr/bin/env python3
"""
A Cache class.
"""

import redis
import uuid


class Cache:
    """
    A class Cache that takes no arguments.
   """
    def __init__(self):
        """
        stores an instance of the Redis client
        as a private variable named _redis (using redis.Redis())
        and flush the instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """
        A store method that takes a data argument and returns a string.
        Generates a random key (e.g. using uuid),
        store the input data in Redis using the random key
        and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

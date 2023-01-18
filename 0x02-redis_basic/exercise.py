#!/usr/bin/env python3

'''
A class that stores an instance of redis client
as a private variable and stores data in redis.
'''

import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Calls a method that stores the history of inputs and outputs
       for a particular function.
    """
    qualified_name = method.__qualname__
    input_key = qualified_name + ":inputs"
    output_key = qualified_name + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Stores the data in a redis db"""
        self._redis.rpush(input_key, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(output_key, str(data))
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ counts how many times methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapped function that increments the key"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def replay(method: Callable) -> None:
    """displays the history of calls of a particular function."""
    redis = method.__self__._redis
    qualified_name = method.__qualname__
    num_of_calls = redis.get(qualified_name).decode("utf-8")
    print("{} was called {} times:".format(qualified_name, num_of_calls))
    input_key = qualified_name + ":inputs"
    output_key = qualified_name + ":outputs"
    input_list = redis.lrange(input_key, 0, -1)
    output_list = redis.lrange(output_key, 0, -1)
    r_zipped = list(zip(input_list, output_list))
    for key, value in r_zipped:
        key = key.decode("utf-8")
        value = value.decode("utf-8")
        print("{}(*{}) -> {}".format(qualified_name, key, value))


class Cache:
    """defines methods that perform few common redis-py operations
       on redis
    """
    def __init__(self):
        """Instantiates a redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the data in redis"""
        r_key = str(uuid4())
        self._redis.set(r_key, data)
        return r_key

    def get(self, key: str, fn: Callable = None):
        """Calls a method that Converts redis data back to desired format"""
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Parametises Cache.get to str"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Parametises Cache.get to int"""
        try:
            data = int(value.decode("utf-8"))
        except Exception:
            data = 0
        return

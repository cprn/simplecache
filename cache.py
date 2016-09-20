#!/usr/bin/python3
import os
import pickle
import time


class PickleCache:

    def __init__(self, jar_path, timeout):
        self.__timeout = timeout
        self.__cachejar = os.path.expanduser(jar_path)
        self.__cache = {}
        self.__load()

    def add(self, id, data):
        self.__cache[id] = {**data, **{'__date': time.time()}}

    def get(self, appid):
        cache = self.__cache[appid]
        if cache['__date'] < time.time() - self.__timeout:
            raise KeyError
        return cache

    def save(self):
        with open(self.__cachejar, "wb") as file:
            pickle.dump(self.__cache, file)

    def __load(self):
        try:
            with open(self.__cachejar, "rb") as file:
                self.__cache = pickle.load(file)
            print("Cache loaded...")
        except IOError:
            print("Cache empty...")

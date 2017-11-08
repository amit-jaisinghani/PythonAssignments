__author__ = 'zjb'
from collections import namedtuple
import re

Entry = namedtuple('Entry', ('key', 'value'))

'''
Author: Amit Shyam Jaisinghani

To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''


class _delobj: pass
DELETED = Entry(_delobj(),None)

INBUILT = 1
ORD = 2
UNIQUE_ASCII = 3


class Hashmap:

    __slots__ = 'table','numkeys','cap','maxload','probe','collision','hashfunction'

    def __init__(self, initsz=100, maxload=0.7, hashfunction=INBUILT):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.probe = 0
        self.collision = 0
        self.hashfunction = hashfunction

    def put(self, key, value):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''

        index = self.get_hash_key(key)

        is_collision_counted = False
        self.probe += 1
        while self.table[index] is not None and \
                        self.table[index] != DELETED and \
                        self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
            self.probe += 1
            if not is_collision_counted:
                self.collision += 1
                is_collision_counted = True
        if self.table[index] is None:
            self.numkeys += 1
        self.table[index] = Entry(key, value)
        if self.numkeys / self.cap > self.maxload:
            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None:
                    self.put(entry[0], entry[1])

    def remove(self, key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.get_hash_key(key)

        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED

    def get(self, key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.get_hash_key(key)

        self.probe += 1
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == self.cap:
                index = 0
            self.probe += 1
        if self.table[index] is not None:
            return self.table[index].value
        else:
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self, key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.get_hash_key(key)

        self.probe += 1
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == self.cap:
                index = 0
            self.probe += 1
        return self.table[index] is not None

    def get_hash_key(self, key):
        if self.hashfunction == INBUILT:
            index = self.hash_func(key) % self.cap
        elif self.hashfunction == ORD:
            index = self.hash_func_ord(key) % self.cap
        else:
            index = self.hash_func_unique_ascii(key) % self.cap
        return index

    def hash_func(self, key):
        '''
        Using Python's built in hash function here
        :param key: Key to store
        :return: Hash value for that key
        '''
        return hash(key)

    def hash_func_ord(self, key):
        '''
        calculates hash value using ascii value of every character
        and multiplied by a factor.
        :param key: Key to store
        :return: Hash value for that key
        '''

        hash_value = 0
        count = 1
        for x in key:
            hash_value = hash_value + ord(x)*count
            count = count + 1
        return hash_value

    def hash_func_unique_ascii(self, key):
        '''
        calculates hash value based on every unique ascii value in the word.
        :param key: Key to store
        :return: Hash value for that key
        '''

        list_characters = []
        list_value = []
        for ch in key:
            try:
                index = list_characters.index(ch)
                list_value[index] += 1
            except ValueError:
                list_characters.append(ch)
                list_value.append(ord(ch))

        value = 0
        for ascii_frequency_value in list_value:
            value += ascii_frequency_value

        return value


def printMap(map):
    for i in range(map.cap):
        print(str(i) + ": " + str(map.table[i]))


def testMap():
    map = Hashmap(5)
    map.put('apple', 1)
    map.put('banana', 2)
    map.put('orange', 15)
    printMap(map)
    print("#Probe: ", map.probe)
    print("#Collision: ", map.collision)
    print()
    print("Contains apple: ", map.contains('apple'))
    print("#Probe: ", map.probe)
    print("#Collision: ", map.collision)
    print()
    print("Contains grape: ", map.contains('grape'))
    print("#Probe: ", map.probe)
    print("#Collision: ", map.collision)
    print()
    print("Get Orange: ", map.get('orange'))
    print("#Probe: ", map.probe)
    print("#Collision: ", map.collision)

    print('--------- adding one more to force table resize ')
    map.put('grape', 7)
    printMap(map)
    print("#Probe: ", map.probe)
    print("#Collision: ", map.collision)
    print()

    print('--------- testing remove')
    map.remove('apple')
    printMap(map)
    print("#Probe: ", map.probe)
    print("#Collision: ", map.collision)
    print()

    print('--------- testing add to a DELETED location')
    map.put('peach', 16)
    printMap(map)
    print("#Probe: ", map.probe)
    print("#Collision: ", map.collision)
    print()
    print(map.get('grape'))
    print("#Probe: ", map.probe)
    print("#Collision: ", map.collision)


if __name__ == '__main__':
    testMap()
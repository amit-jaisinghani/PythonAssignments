import re
from collections import namedtuple
__author__ = 'asj8139,ass7436'

"""
Assignment 7: Hashing
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This program is a testing environment for  testing the
two hash functions as well as Python's built-in
hashfunction over three different maximum loadfactors
and over three different files.
"""

Entry = namedtuple('Entry', ('key', 'value'))


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
        calculates hash value using ascii value of every character and left shift operation
        :param key: Key to store
        :return: Hash value for that key
        '''

        hash_value = 0
        for x in key:
            ascii_value = ord(x)
            hash_value = ascii_value + (hash_value << 16) - hash_value
        return hash_value

    def hash_func_unique_ascii(self, key):
        '''
        calculates hash value based on every unique ascii value in the word and left,
         right and XOR operation.
        :param key: Key to store
        :return: Hash value for that key
        '''

        hash_value = 0
        for x in key:
            hash_value = ((hash_value << 13) ^ (hash_value >> 7)) ^ ord(x)
        return hash_value


def printMap(map):
    for i in range(map.cap):
        print(str(i) + ": " + str(map.table[i]))


def add_word(hash_map, word):
    '''
    adds new word to the hash_map
    if the word already exists in the hash_map,
    then its value is increased.
    :param hash_map: in which the words are to be added.
    :param word: which is to be added to the hash_map
    :return: None
    '''
    if word == '':
        return
    try:
        value = hash_map.get(word)
        hash_map.put(word, value + 1)
    except KeyError:
        hash_map.put(word, 1)


def find_max_repeating_word(hash_map):
    '''
    finds word in hash_map which has repeated maximum number of times.
    :param hash_map: from which maximum repeating word is to be found.
    :return: word and word_count
    '''
    word = None
    max = 0
    for entry in hash_map.table:
        if entry is not None:
            if entry.value > max:
                word = entry.key
                max = entry.value
    return word, max


def get_stats(file_name, max_load, hash_function_choice):
    '''

    :param file_name: in which the word with maximum frequency is to be found
    :param max_load: capacity of hashmap
    :param hash_function_choice: which hashing function is to be used
    :return: None
    '''
    try:
        file = open(file_name)
    except FileNotFoundError:
        print("File not found. Please check file name and path.")
        return
    hash_map = Hashmap(100000, max_load, hash_function_choice)
    for line in file:
        words = re.split('\W+', line)
        for word in words:
            word = word.lower()
            add_word(hash_map, word)
    word, max = find_max_repeating_word(hash_map)
    print("Word ", word, " has max occurrence of ", max)
    print("#Probe - ", hash_map.probe, "#Collision - ", hash_map.collision)
    return


def generate_stats(file_name):
    '''
    generates statistics for different hashing functions and load values
    :param file_name: on which statistics is to be performed
    :return: None
    '''
    loads = [0.7, 0.8, 0.9]

    for hash_algo in range(1, 4):
        for load in loads:
            print("File - ", file_name, " max load - ", load, " algo - ", hash_algo)
            get_stats(file_name, load, hash_algo)


def main():
    """
    The main function.

    tests the file using different hash function and max loads.

    :return: None
    """
    # generate_stats("The beginnings of nature control.txt")

    generate_stats("The Family on Wheels.txt")

    # generate_stats("dictionary.txt")
    pass


if __name__ == '__main__':
    main()
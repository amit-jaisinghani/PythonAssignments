__author__ = 'asj8139'

"""
Author: Amit Shyam Jaisinghani

This is a program 
"""


def generate_hash(string):
    sum = 0
    factor = 1
    for ch in string:
        sum += ord(ch) * factor
        factor *= 31
    return sum


def main():
    print(generate_hash("BLAB"))
    pass


if __name__ == '__main__':
    main()

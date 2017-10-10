__author__ = 'asj8139,ass7436'

"""
Assignment 4: Secret Messages 
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This program encodes and decodes secret messages in a file.

"""

import sys

STATUS_ENCRYPT = 'encrypt'
STATUS_DECRYPT = 'decrypt'


def init_file():
    """
        Takes user input for file name. Reads and handles file operations.
        :return: messages_file, transformation_file
    """

    # messages_file_name = input("Please enter messages file name: ")
    # transformation_file_name = input("Please enter transformation file name: ")

    messages_file_name = "messages.txt"
    transformation_file_name = "codes.txt"

    messages_file = open(messages_file_name)
    transformation_file = open(transformation_file_name)

    return messages_file, transformation_file


def user_data():
    """
        Takes user input regarding status. exits if the input is not proper.
        :return: status
    """

    status = input("Do you want to encrypt or decrypt?").lower()
    if status != STATUS_ENCRYPT and status != STATUS_DECRYPT:
        print("Usage: You need to enter only encrypt or decrypt : ")
        sys.exit(1)
    return status


def rotate(string, exponent):
    """
        rotates the string to right. It shifts number of exponent times.
        For negative exponent the string shits left.
        :return: result
    """

    length = len(string)
    if exponent >= 0:
        if exponent == 0:
            exponent = 1
        for x in range(exponent):
            string = string[length - 1] + string[0:length - 1]
    else:
        for x in range(exponent,0):
            string = string[1:length] + string[0]
    return string


def rotate_decrypt(string, exponent):
    """
        rotates the string to left. It shifts number of exponent times.
        For negative exponent the string shits right.
        :return: result
    """

    length = len(string)
    if exponent >= 0:
        for x in range(exponent):
            string = string[1:length] + string[0]
    else:
        for x in range(exponent,0):
            string = string[length - 1] + string[0:length - 1]
    return string


def shift_char(string, index, exponent):
    """
        shifts the letter at index forward one letter in the alphabet if the exponent is positive.
        shifts the letter at index backward one letter in the alphabet if the exponent is negative.
        :return: result
    """

    c = string[index]
    ascii_value = ord(c)

    if exponent >=0:
        for x in range(exponent):
            ascii_value = ascii_value+1
            if ascii_value == 91:
                ascii_value = 65
    else:
        for x in range(exponent,0):
            ascii_value = ascii_value - 1
            if ascii_value == 64:
                ascii_value = 90
    result = string[0: index] + chr(ascii_value) + string [index + 1: len(string)]
    return result


def shift_char_decrypt(string, index, exponent):
    """
        shifts the letter at index backward one letter in the alphabet if the exponent is positive.
        shifts the letter at index forward one letter in the alphabet if the exponent is negative.
        :return: result
    """
    c = string.find(index)
    ascii_value = ord(c)
    if exponent >=0:
        for x in range(exponent):
            ascii_value = ascii_value - 1
            if ascii_value == 64:
                ascii_value = 90
    else:
        for x in range(exponent,0):
            ascii_value = ascii_value + 1
            if ascii_value == 90:
                ascii_value = 64
    result = string[0: index] + chr(ascii_value) + string [index + 1: len(string)]
    return result


def duplicate(string, index, exponent):
    """
        duplicates the letter at index if the exponent is positive.
        :return: result
    """
    result = string
    if exponent >= 0:
        result = string[0: index] + (string[index] * exponent) + string [index: len(string)]
    return result


def swap_letters(string, i, j):
    """
        Swaps the letters at index i and index j if i < j.
        :return: result
    """

    result = string
    if i < j :
        result = ""
        for x in range(len(string)):
            if x == i:
                result = result + string[j]
            elif x == j:
                result = result + string[i]
            else:
                result = result + string[x]
    return result


def swap_group_of_letters(string, i, j, g):
    """
        Divides the string into g equal-sized groups of letters,
        and then swaps the groups at index i and index j if i < j.
        :return: result
    """

    result = string
    length = int(len(string))
    if length % g == 0:
        n = length // g
        result = ""
        result_list = [string[i:i + n] for i in range(0, len(string), n)]
        result_list[i], result_list[j] = result_list[j], result_list[i]
        for x in range(len(result_list)):
            result = result+result_list[x]

    return result


def transform(messages_file, transformation_file, status):
    """
        Breaks the lines in transformation_file to get
        operations and transformation list for every operation.
        :return: None
    """

    for line in transformation_file:
        operation = line.strip()
        if len(operation)>1 and operation[1] == '(':
            transformation_list = [operation[2], operation[4],operation[6]]
            pass
        else :
            transformation_list = operation[1: len(operation)].split(',')
        select_function(messages_file.readline().upper().strip() , status, line[0] ,transformation_list)

        print(transformation_list)
    pass


def select_function(message, status, operation, transformation_list):
    """
        Assigns values to index, exponent, group from transformation list.
        Calls appropriate function based on operation value and status.
        :return: None
    """

    result = ""
    if len(transformation_list) == 1 and transformation_list[0] !='':
        index = int(transformation_list[0])
        exponent = 1
        group = 0
    elif (len(transformation_list) == 2):
        index = int(transformation_list[0])
        exponent = int(transformation_list[1])
        group = 0
    elif (len(transformation_list) == 3):
        group = int(transformation_list[0])
        index = int(transformation_list[1])
        exponent = int(transformation_list[2])
    else :
        index = 0
        exponent = 1
        group = 0
    if status == STATUS_ENCRYPT and operation == 'S':
        result = shift_char(message, index, exponent)
    elif status == STATUS_DECRYPT and operation == 'S':
        result = shift_char_decrypt(message, index, exponent)
    elif status == STATUS_ENCRYPT and operation == 'R':
        result = rotate(message, index)
    elif status == STATUS_DECRYPT and operation == 'R':
        result = rotate_decrypt(message, index, exponent)
    elif operation == 'D':
        result = duplicate(message, index, exponent)
    elif operation == 'T':
        if group == 0:
            result = swap_letters(message, index, exponent)
        else :
            result = swap_group_of_letters(message, index, exponent, group)

    print(result)

    pass


def main():
    """
        The main function.
        Takes user input.
        Reads file.
        Transform file according to status.
        :return: None
    """

    messages_file, transformation_file = init_file()
    status = user_data()
    transform(messages_file, transformation_file, status)
    pass


if __name__ == '__main__':
    main()
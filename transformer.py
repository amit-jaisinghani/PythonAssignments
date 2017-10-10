__author__ = 'asj8139,ass7436'

"""
Assignment 4: Secret Messages 
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This program 

"""

import sys

STATUS_ENCRYPT = 'encrypt'
STATUS_DECRYPT = 'decrypt'


def user_data():
    status = input("Do you want to encrypt or decrypt?").lower()
    if status != STATUS_ENCRYPT and status != STATUS_DECRYPT:
        print("Usage: You need to enter only encrypt or decrypt : ")
        sys.exit(1)
    return status


def rotate(string, exponent):
    length = len(string)
    if exponent >= 0:
        if exponent == 0:
            exponent = 1
        for x in range(exponent):
            string = string[length - 1] + string[0:length - 1]
    else:
        for x in range(exponent, 0):
            string = string[1:length] + string[0]
    return string


def rotate_decrypt(string, exponent):
    length = len(string)
    if exponent >= 0:
        for x in range(exponent):
            string = string[1:length] + string[0]
    else:
        for x in range(exponent, 0):
            string = string[length - 1] + string[0:length - 1]
    return string


def shift_char(string, index, exponent):
    c = string[index]
    ascii_value = ord(c)

    if exponent >= 0:
        for x in range(exponent):
            ascii_value = ascii_value + 1
            if ascii_value == 91:
                ascii_value = 65
    else:
        for x in range(exponent, 0):
            ascii_value = ascii_value - 1
            if ascii_value == 64:
                ascii_value = 90
    result = string[0: index] + chr(ascii_value) + string[index + 1: len(string)]
    return result


def shift_char_decrypt(string, index, exponent):
    c = string.find(index)
    ascii_value = ord(c)
    if exponent >= 0:
        for x in range(exponent):
            ascii_value = ascii_value - 1
            if ascii_value == 64:
                ascii_value = 90
    else:
        for x in range(exponent, 0):
            ascii_value = ascii_value + 1
            if ascii_value == 90:
                ascii_value = 64
    result = string[0: index] + chr(ascii_value) + string[index + 1: len(string)]
    return result


def duplicate(string, index, exponent):
    result = string
    if exponent >= 0:
        result = string[0: index] + (string[index] * exponent) + string[index: len(string)]
    return result


def swap_letters(string, i, j):
    result = string
    if i < j:
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
    result = string
    length = int(len(string))
    if length % g == 0:
        n = length // g
        result = ""
        result_list = [string[i:i + n] for i in range(0, len(string), n)]
        result_list[i], result_list[j] = result_list[j], result_list[i]
        for x in range(len(result_list)):
            result = result + result_list[x]

    return result


def transform(messages_file, transformation_file, status):
    for transformation in transformation_file:
        message = messages_file.readline().strip().upper()

        if message is None or message == '':
            sys.exit(-1)

        operation = transformation.strip().upper()
        if len(operation) > 1 and operation[1] == '(':
            transformation_list = [operation[2], operation[4], operation[6]]
            pass
        else:
            transformation_list = operation[1: len(operation)].split(',')
        select_function(message, status, transformation[0], transformation_list)

        print(transformation_list)
    pass


def select_function(message, status, operation, transformation_list):
    result = ""
    if len(transformation_list) == 1 and transformation_list[0] != '':
        index = int(transformation_list[0])
        exponent = 1
        group = 0
    elif len(transformation_list) == 2:
        index = int(transformation_list[0])
        exponent = int(transformation_list[1])
        group = 0
    elif len(transformation_list) == 3:
        group = int(transformation_list[0])
        index = int(transformation_list[1])
        exponent = int(transformation_list[2])
    else:
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
        else:
            result = swap_group_of_letters(message, index, exponent, group)

    print(result)

    pass


def main():
    messages_file = None
    transformation_file = None
    try:
        # messages_file_name = input("Please enter messages file name: ")
        # transformation_file_name = input("Please enter transformation file name: ")
        # status = user_data()
        messages_file_name = "messages.txt"
        transformation_file_name = "codes.txt"
        status = "encrypt"

        messages_file = open(messages_file_name)
        transformation_file = open(transformation_file_name)

        transform(messages_file, transformation_file, status)

    except FileNotFoundError:
        print("File not found. Please enter filename properly.")

    except IOError:
        print("Error in reading files. Please check the files.")

    except:
        print("Error while executing.")

    finally:
        if messages_file is not None:
            messages_file.close()
        if transformation_file is not None:
            transformation_file.close()
    pass


if __name__ == '__main__':
    main()

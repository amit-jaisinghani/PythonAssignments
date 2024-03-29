__author__ = 'asj8139,ass7436'

"""
Assignment 4: Secret Messages 
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This program encodes and decodes secret messages in a file.

"""

import sys

STATUS_ENCRYPT = 'encrypt'
STATUS_DECRYPT = 'decrypt'


def user_data():
    """
        Takes user input regarding status. exits if the input is not proper.
        :return: status
    """

    status = input("Do you want to encrypt or decrypt? ").lower()
    if status != STATUS_ENCRYPT and status != STATUS_DECRYPT:
        print("Usage: You need to enter only encrypt or decrypt : ")
        sys.exit(1)
    return status


def rotate(string, exponent):
    """
        rotates the string to right. It shifts number of exponent times.
        For negative exponent the string shits left.
        :param string: on which the operation is to be performed.
        :param exponent: number of times string is to be rotated.
        :return: result of the operation.
    """

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


def shift_char(string, index, exponent):
    """
        shifts the letter at index forward one letter in the alphabet if the exponent is positive.
        shifts the letter at index backward one letter in the alphabet if the exponent is negative.
        :param string: on which the operation is to be performed.
        :param index: position of character which is to be shifted.
        :param exponent: number of times ascii value of character is to be increased.
        :return: result of the operation
    """

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


def duplicate(string, index, exponent):
    """
        duplicates the letter at index if the exponent is positive.
        :param string: on which the operation is to be performed.
        :param index: position of character which is to be duplicated.
        :param exponent: number of time character is to be duplicated.
        :return: result of the operation
    """
    result = string
    if exponent >= 0:
        result = string[0: index] + (string[index] * exponent) + string[index: len(string)]
    return result


def decrypt_duplicate(string, index, exponent):
    """
        removes duplicate letter at index if the exponent is positive.
        :param string: on which the operation is to be performed.
        :param index: position of character which is to be non-duplicated.
        :param exponent: number of time character is to be non-duplicated.
        :return: result of the operation
    """
    result = string
    if exponent >= 0:
        result = string[0: index] + string[index + exponent: len(string)]
    return result


def swap_letters(string, i, j):
    """
        Swaps the letters at index i and index j if i < j.
        :param string: on which the operation is to be performed.
        :param i: index one which is to be swapped.
        :param j: index two which is to be swapped.
        :return: result of the operation.
    """

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
    """
        Divides the string into g equal-sized groups of letters,
        and then swaps the groups at index i and index j if i < j.

        :param string: on which the operation is to be performed.
        :param i: index one which is to be swapped.
        :param j: index two which is to be swapped.
        :param g: number of equal-sized groups of letters.
        :return: result of the operation.
    """

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


def key_encryption(message, factor):
    """
        Encrypts the message with the key, each character is encoded with key value in increment order.
        If key is exhausted, it is used from start again. And key can be changed,
        but it should remain constant for both encryption and decryption.
        Operation String: K
        Example: For string "MAX" encryption with key [2,3,4] is "ODB"

        :param message: on which the operation is to be performed.
        :param factor: used for encryption and decryption. 1 for encryption and -1 for decryption.
        :return: result of the operation
    """
    key = [2, 3, 4]
    key_index = 0
    result = ""
    for ch in message:
        ascii_value = ord(ch) + (key[key_index] * factor)
        if factor == 1 and ascii_value > 90:
            ascii_value -= 26
        if factor == -1 and ascii_value < 65:
            ascii_value += 26
        result += chr(ascii_value)
        key_index += 1
        if key_index == len(key):
            key_index = 0
    return result


def transform(messages_file, transformation_file, status):
    """
        Breaks the lines in transformation_file to get
        operations and transformation list for every operation.

        :param messages_file: file containing messages.
        :param transformation_file: file containing transformations.
        :param status: user choice amongst encrypt and decrypt.

        :return: None
    """

    for transformation in transformation_file:
        message = messages_file.readline().strip().upper()

        if message is None or message == '':
            sys.exit(-1)

        if status == STATUS_ENCRYPT:
            operation_list = transformation.strip().upper().split(";")
        else:
            operation_list = reversed(transformation.strip().upper().split(";"))

        for operation in operation_list:
            if len(operation) > 1 and operation[1] == '(':
                transformation_list = [operation[2], operation[4], operation[6]]
            else:
                transformation_list = operation[1: len(operation)].split(',')
            message = select_function(message, status, operation[0], transformation_list)

        print(message)
    pass


def select_function(message, status, operation, transformation_list):

    """

        Assigns values to index, exponent, group from transformation list.
        Calls appropriate function based on operation value and status.

        :param message: String which is to be encrypted or decrypted.
        :param status: user choice amongst encrypt and decrypt.
        :param operation: character indicating operation to be performed on message.
        :param transformation_list: parameter list of operation.

        :return: encrypted/decrypted message
    """

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
        index = 1
        exponent = 1
        group = 0
    if status == STATUS_ENCRYPT and operation == 'S':
        result = shift_char(message, index, exponent)
    elif status == STATUS_DECRYPT and operation == 'S':
        result = shift_char(message, index, exponent * -1)
    elif status == STATUS_ENCRYPT and operation == 'R':
        result = rotate(message, index)
    elif status == STATUS_DECRYPT and operation == 'R':
        result = rotate(message, index * -1)
    elif status == STATUS_ENCRYPT and operation == 'D':
        result = duplicate(message, index, exponent)
    elif status == STATUS_DECRYPT and operation == 'D':
        result = decrypt_duplicate(message, index, exponent)
    elif status == STATUS_ENCRYPT and operation == 'K':
        result = key_encryption(message, 1)
    elif status == STATUS_DECRYPT and operation == 'K':
        result = key_encryption(message, -1)
    elif operation == 'T':
        if group == 0:
            result = swap_letters(message, index, exponent)
        else:
            result = swap_group_of_letters(message, index, exponent, group)

    return result


def main():
    """
        The main function.
        Takes user input.
        Reads file.
        Transform file according to status.
        :return: None
    """
    messages_file = None
    transformation_file = None
    try:
        messages_file_name = input("Please enter messages file name: ")
        transformation_file_name = input("Please enter transformation file name: ")
        status = user_data()

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

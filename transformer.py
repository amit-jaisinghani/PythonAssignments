__author__ = 'asj8139,ass7436'

"""
Assignment 4: Secret Messages 
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This program 

"""


def transformation():
    messages_file_name = input("Please enter messages file name: ")
    transformation_file_name = input("Please enter transformation file name: ")
    print(messages_file_name)
    print(transformation_file_name)
    messages_file = open(messages_file_name)
    # transformation_file = open(transformation_file_name)
    print(messages_file.readline())
    print(messages_file.readline())
    pass


def main():
    transformation()
    pass


if __name__ == '__main__':
    main()

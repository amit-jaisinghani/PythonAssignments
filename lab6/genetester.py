__author__ = 'asj8139','ass7436'

"""
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This is a program executes test cases for dnaList
"""
from dnalist import DNAList


def test_init():
    """
    We have handled scenarios for init where
    if data is None, nothing is passed.
    if empty constructor is given, string is passed.
    :return: None
    """
    dna = DNAList(None)
    print(dna)
    dna = DNAList("")
    print(dna)

    dna = DNAList("AMit")
    print(dna)

    dna = DNAList("A")
    print(dna)

    dna = DNAList("@")
    print(dna)

    dna = DNAList()
    print(dna)

    # dna = DNAList("YOUTUBE")
    # print(dna)


def test_append():
    """
    Allows only character to be appended at the end of the string.
    If String is tried to be appended it will give an assertion.
    If the list is empty, a blank list is created.
    :return: None
    """
    dnaAppend = DNAList()
    print(dnaAppend)
    dnaAppend.append("A")
    print(dnaAppend)
    # dnaAppend.append("Aditi")
    # print(dnaAppend)
    dnaAppend.append(8)
    print(dnaAppend)
    dnaAppend.append('@')
    print(dnaAppend)
    dnaAppend.append(None)
    print(dnaAppend)


def test_join():
    """
    Another list is appended to the current list.
    It is added to the end of the list.
    If another list is empty, nothing is added.
    if the current list is empty, another list still can be added to it.

    :return:None
    """
    dna_list = DNAList("JOINTEST")
    dna_list.join(DNAList("I AM Joining"))
    print(dna_list)
    dna_list.join(DNAList(""))
    print(dna_list)


def test_splice():
    """
    checks if the index is valid in the list.
    If other list is empty, nothing is added in the index.
    If the index is greater than the list size, Index out of Bounds assetion is thrown.
    :return: None
    """
    dna_list = DNAList("SPLICETEST")
    other = DNAList(" Yayy ")
    dna_list.splice(5, other)
    print(dna_list)
    pass

def test_snip():
    """
    checks if the start and end index lies within the range of list.
    If the index is greater than the list size, Index out of Bounds assetion is thrown.
    :return: None
    """
    dna_list = DNAList("SNIPTEST")
    dna_list.snip(0, 4)
    print(dna_list)
    pass


def test_replace():
    """
    If the other list is empty, nothing is replaced.
    If repstr String is not found, nothing is replaced.
    If The String is found, it is replaced.
    :return: None
    """
    dna_list = DNAList("HIIAMAAMIT")
    other = DNAList("ADITI")
    dna_list.replace("Jaisinghani", other)
    print(dna_list)
    dna_list.replace("AMIT", other)
    print(dna_list)
    pass


def test_copy():
    """
    checks if another copy is made or not.
    If the original List is empty, copy of empty String will be returned.
    :return:
    """
    dna_list = DNAList("COPYTEST")
    print(dna_list.copy())
    pass


def test_str():
    "Prints List value."
    dna_list = DNAList("PRINTTEST")
    print(dna_list)
    pass


def test():
    test_init()
    test_append()
    test_join()
    test_splice()
    test_snip()
    test_replace()
    test_copy()
    test_str()

if __name__ == "__main__":
    test()
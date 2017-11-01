__author__ = 'asj8139','ass7436'

"""
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This is a program represnts a DNA strand as a linked list 
on which the following operations like splicing, snipping and joining can be performed.
"""

"""
A module that represents "DNA" in the dnalist.
"""
class DNA:
    __slots__ = "gene", "link"

    def __init__(self, gene, link=None):
        self.gene = gene
        self.link = link
        pass

    def __str__(self):
        return self.gene


class DNAList:

    __slots__ = "front", "rear", "size"

    def __init__(self, gene=''):
        self.front = None
        self.rear = None
        self.size = 0
        for x in gene:
            self.append(x)
        pass

    def append(self, ch):
        node = DNA(ch)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node
        self.size += 1
        pass

    def join(self, dna_list):
        if self.is_empty():
            self.front = dna_list.front
            self.rear = dna_list.rear
        else:
            self.rear.link = dna_list.front
            self.rear = dna_list.rear
        self.size += dna_list.size

    def splice(self, ind, other):
        assert ind >= 0, "Index out of bounds"
        n = self.front
        for x in range(ind):
            assert n is not None, "Index out of bounds"
            n = n.link
        assert n is not None, "Index out of bounds"
        other.rear.link = n.link
        n.link = other.front
        if ind == self.size-1:
            self.rear = other.rear
        self.size += other.size

    # def snip(self, i1, i2):
    #     assert i1 >= 0 and i2 < self.size, "Index out of bounds"
    #     count = 0
    #     cursor = self.front

    def copy(self):
        copy_list = DNAList()
        cursor = self.front
        while cursor is not None:
            copy_list.append(cursor.gene)
            cursor = cursor.link
        return copy_list

    def is_empty(self):
        return self.front is None

    def __str__(self):
        value = ""
        cursor = self.front
        while cursor is not None:
            value += cursor.gene
            cursor = cursor.link
        return value


# empty = DNAList()
# empty.snip(0, 0)

# dna = DNAList("Hl")
# other = DNAList("el")
# dna.splice(0, other)
# dna.splice(3, DNAList("Raiser"))
# dna.append("x")
# print(dna.size)
# print(dna)
# print(dna.copy())
# dna.join(DNAList("Raiser"))

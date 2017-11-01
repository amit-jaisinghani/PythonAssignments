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
        assert len(str(gene)) == 1, "More than 1 character"
        self.gene = str(gene)
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
        if gene is None:
            return
        for x in gene:
            self.append(x)
        pass

    def append(self, ch):
        if ch is None:
            return
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

    def snip(self, i1, i2):
        assert i1 >= 0 and i2 <= self.size, "Index out of bounds"
        count = 0
        cursor = self.front
        start = cursor
        while cursor is not None:
            if count < i1:
                start = cursor
            else:
                if i1 == 0:
                    self.front = self.front.link
                else:
                    start.link = cursor.link
                self.size -= 1
            count += 1
            if count == i2:
                break
            cursor = cursor.link
        if self.front is None:
            self.rear = None
        elif i2 == self.size:
            self.rear = start

    def replace(self, repstr, other):
        node = self.front
        if node is not None:
            firstNode = None
            lastNode = None
            count = 0
            found = False
            while count < len(repstr):
                if node is None:
                    break
                if node.gene == repstr[count]:
                    if count == 0:
                        firstNode = node
                    count = count + 1
                    found = True
                    node = node.link
                    if count == (len(repstr) - 1):
                        lastNode = node
                        break;
                if not (node.gene == repstr[count]):
                    if count>0:
                        count = 0
                        found = False
                        continue
                    else:
                        found = False
                        node = node.link
        if found:
            prevNode = None
            currentNode = self.front
            while currentNode != firstNode:
                prevNode = currentNode
                currentNode = currentNode.link
            self.size += (other.size - len(repstr))
            other.rear.link = lastNode.link
            prevNode.link = other.front
            if lastNode == self.rear:
                self.rear = other.rear


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
import sys
import os.path
from Graph import Graph
from Cow import Cow
from Color import Color

__author__ = 'asj8139'

"""
Author: Amit Shyam Jaisinghani

This is a program 
"""


class Holicow:

    __slots__ = "graph"
    
    def __init__(self):
        self.graph = Graph()
        pass

    def buildGraph(self, fileName):

        with open(fileName) as f:
            for line in f:
                line = line.strip()
                if line.startswith("cow"):
                    self.graph.addVertex(Cow(line.split()[1]))
                else:
                    self.graph.addVertex(Color(line.split()[1]))
        pass
    
    def addVertex(self, vertex):
        
    
    def printGraph(self):
        print(self.graph)


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 holicow.py {filename}')
        return

    if not os.path.exists(sys.argv[1]):
        print('File not found ' + sys.argv[1])
        return

    holicow = Holicow()
    holicow.buildGraph(sys.argv[1])
    holicow.printGraph()
    pass


if __name__ == '__main__':
    main()

__author__ = 'asj8139,ass7436'

"""
Assignment 9: Holi Cow!
Author: Amit Shyam Jaisinghani, Aditi Shailendra Singhai

This program reads all the information about all the details and location of each cow and paint ball in the field.
Each cow has a unique name and location. Each paint ball has a unique PaintBall, location, and splatter radius. When 
a paint ball will blast it will paint all cows in its blast radius and trigger other paint balls in range. This 
programs generates graph with information provided and computes which paint ball can lead to painting cows with 
max PaintBalls. And returns paint with max score and details about cows and paints that are painted on them.
"""

import sys
import os.path
from Graph import Graph
from Cow import Cow
from PaintBall import PaintBall
import math


class Holicow:
    """
        Represents scenario with graph. Calculates optimal paint ball to paint cows with max colors. Display
        the result.

        :slot: graph (Graph):  graph of scenario
    """
    __slots__ = "graph"

    def __init__(self):
        """
            Initializes Graph.
        """
        self.graph = Graph()
        pass

    def buildGraph(self, fileName):
        """
        Reads the file provided. Parses information.
        Add all vertexes for graph. Key can be Cow and PaintBall object based on information parsed.
        After all vertexes are added, connectGraph() is called to created edges.
        :param fileName:
                containing information about name, location of Cow and name, location, blas radius of
                Paint Ball
        :return: None
        """
        with open(fileName) as f:
            for line in f:
                line = line.strip()
                words = line.split()
                if words[0] == "cow":
                    self.graph.addVertex(Cow(words[1], words[2], words[3]))
                else:
                    self.graph.addVertex(PaintBall(words[1], words[2], words[3], words[4]))

        self.connectGraph()
        pass

    def connectGraph(self):
        """
        Connects all vertexes which are in blast radius of a paint ball vertex.
        :return: None
        """
        for src in self.graph.get_vertex_keys():
            if isinstance(src, PaintBall):
                for dest in self.graph.get_vertex_keys():
                    if src != dest and self.inRadius(src, dest):
                        self.graph.addEdge(src, dest)
        pass

    def inRadius(self, src, dest):
        """
        Calculates distance between src and dest graph points.
        :param src: Vertex
                    Paint ball with a location and blast radius
        :param dest: Vertex
                    Cow/Paint Ball with a location
        :return: True; if dest is in blast radius of src (paint ball)
                 False; if dest is not in blast radius of src (paint ball)
        """
        distance = math.sqrt(math.pow((src.getX() - dest.getX()), 2) + math.pow((src.getY() - dest.getY()), 2))
        return distance <= src.getBlastRadius()

    def printGraph(self):
        """
        Prints given scenario using Graph i.e. Vertexes and their adjacency list where each vertex indicates what
        neighboring vertices it is connected to.
        :return: None
        """
        print("Field of Dreams")
        print("---------------")
        for value in self.graph:
            print(value)
        print()
        pass

    def triggerPaintBalls(self):
        """
        Triggers all paint ball vertexes one by one as starting paint ball. The chain reaction of triggering
        other paint balls will paint cows with all colors within blast radius of paint balls. This simulation
        finds the optimal paint ball which colors the cows the most. In case of tie, chooses one.
        :return: None
        """
        print("Beginning simulation...")

        paintBall = None
        maxPoints = 0
        maxPaintedCows = dict()
        for startingPaintBall in self.graph.get_vertex_keys():
            if isinstance(startingPaintBall, PaintBall):
                print("Triggering ", startingPaintBall.name, " paint ball...")
                paintedCows = dict()
                points = self.__chainTrigger__(startingPaintBall, [], paintedCows)
                if points > maxPoints:
                    paintBall = startingPaintBall
                    maxPoints = points
                    maxPaintedCows = paintedCows
        self.printSimulationResult(paintBall, maxPoints, maxPaintedCows)
        pass

    def __chainTrigger__(self, paintBall, visited, paintedCows):
        """
        A recursive function which creates a chain reaction of triggering other paint balls in range. Cows in the
        range are painted with paintBall's color and for paintBall in range, recursive call is made with paintBall
        in range.
        :param paintBall:
                Triggered pain ball.
        :param visited:
                Keeps tracks of all triggered paintBalls from starting paint ball.
        :param paintedCows:
                Keeps tracks of painted cows and colors that are printed on each cow.
        :return: count
                number of cows painted by paintball in argument(including cows that are painted due to chain
                reaction).
        """
        vertex = self.graph.getVertex(paintBall)
        visited.append(vertex)
        count = 0
        for connection in vertex.get_connections():
            if connection in visited:
                continue
            if isinstance(connection.key, Cow):
                print(connection.key.name, "is painted", paintBall.name + "!")
                if connection.key.name not in paintedCows:
                    paintedCows[connection.key.name] = []
                paintedCows[connection.key.name].append(paintBall.name)
                count += 1
            else:
                print(connection.key.name, "paint ball is triggered by", paintBall.name, "paint ball")
                count += self.__chainTrigger__(connection.key, visited, paintedCows)
        return count

    def printSimulationResult(self, paintBall, maxPoints, maxPaintedCows):
        """
        Displays the optimal result. Displaying starting paint ball color which painted the cows the most. Also,
        the cows that are painted by the best paint ball along with the color/s they are painted with. In case,
        where no cows are painted, displays a message.
        :param paintBall:
                 starting paint ball color which painted the cows the most
        :param maxPoints:
                 Number of painted cows
        :param maxPaintedCows:
                 Cows painted with best paint ball color along with the color/s they are painted with
        :return: None
        """
        print()
        print("Results:")
        print("Triggering the", paintBall, "paint ball is the best choice with", maxPoints, "total points on the cows:")
        if maxPoints > 0:
            for keys in self.graph.get_vertex_keys():
                if isinstance(keys, PaintBall):
                    continue
                elif keys.name in maxPaintedCows.keys():
                    print(keys.name, maxPaintedCows[keys.name])
                else:
                    print(keys.name, [])
        else:
            print("No cows were painted by any starting paint ball!")


def main():
    """
        The main function.
        Returns if file path is not given or file does not exits. Prints user friendly message before returning.
        If file is proper, builds graph and beings simulation.
        :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 holicow.py {filename}')
        return

    if not os.path.exists(sys.argv[1]):
        print('File not found ' + sys.argv[1])
        return

    holicow = Holicow()
    # Building Graph
    holicow.buildGraph(sys.argv[1])

    # Printing Graph
    holicow.printGraph()

    # Triggering each starting paint ball vertexes
    holicow.triggerPaintBalls()
    pass


if __name__ == '__main__':
    main()

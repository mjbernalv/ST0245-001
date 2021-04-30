import numpy as np

class GraphAM():

    def __init__(self, size):
        self.size = size
        self.graph =np.zeros((size,size))

    def getWeight(self, source, destination):
        return self.graph[source][destination]

    def addArc(self, source, destination, weight):
        self.graph[source][destination] = weight

    def getSuccessors(self, vertex):
        sucessors = []
        for i in range(len(self.graph[vertex])):
            if self.graph[vertex][i]!=0:
                sucessors.append(i)
        return sucessors

    def __str__(self):
        return f'{self.graph}'


graph = GraphAM(3)
graph.addArc(0, 1 , 15)
graph.addArc(0, 2 , 30)
graph.addArc(1, 1 , 7)
print(graph)
print(graph.getSuccessors(0))
print(graph.getWeight(1, 1))
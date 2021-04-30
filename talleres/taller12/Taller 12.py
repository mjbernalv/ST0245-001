import numpy as np
from GraphAL import GraphAL
from collections import deque

def DFS(graph, initial, final):
    visited = [0]*graph.size
    return __DFSAux(graph, initial, final, visited)

def __DFSAux(graph, current, final, visited):
    if current == final:
        return True
    for son in graph.getSuccessors(current):
        if visited[son] == 0:
            visited[son] = 1
            if __DFSAux(graph, son, final, visited):
                return True
    return False

def BFS(graph, initial, final):
    queue = deque()
    queue.appendleft(initial)
    visited = [0]*graph.size
    while len(queue)!=0:
        current = queue.pop()
        if current == final:
            return True
        for son in graph.getSuccessors(current):
            if visited[son] == 0:
                visited[son] = 1
                queue.appendleft(son)
    return False

graph = GraphAL(5)
graph.addArc(0, 4, 7)
graph.addArc(3, 4, 3)
graph.addArc(4, 2, 5)
graph.addArc(0, 1, 2)
graph.addArc(1, 2, 1)
graph.addArc(2, 0, 8)
print(graph)

print("DFS:")
print("From 0 to 2:", DFS(graph, 0, 2))
print("From 2 to 3:", DFS(graph, 2, 3))
print("From 3 to 0:", DFS(graph, 3, 0))
print("From 4 to 3:", DFS(graph, 4, 3))

print("")
print("BFS:")
print("From 0 to 2:", BFS(graph, 0, 2))
print("From 2 to 3:", BFS(graph, 2, 3))
print("From 3 to 0:", BFS(graph, 3, 0))
print("From 4 to 3:", BFS(graph, 4, 3))

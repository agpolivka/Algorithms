"""
name: Alex Polivka
This work abides by the JMU honor code.
Most of this code was implemented with help
from the psuedo code and references from the chapter
6 in the textbook.
"""
from collections import defaultdict


def main():
    # number of vertices
    n = int(input())

    # dictionary to hold vertices
    graph = defaultdict()

    # building graph
    for x in range(n):
        values = input().split()
        graph[values[0]] = values[1:]
    
    # graph to hold reversal of original graph
    revGraph = defaultdict(set)
    for vertex in graph:
        for vertices in graph[vertex]:
            revGraph[vertices].add(vertex)
        if vertex not in revGraph:
            revGraph[vertex] = set()

    # parent of vertices
    parents = {}

    # setting parents and prePost to empty values
    for vertex in revGraph:
        parents[vertex] = ()

    # set of visited vertices
    visited = set()

    # topological order list that with size of number of vertices
    topological_order = [None] * n        
    
    def DFS(vertex, revGraph, parents):
    
        # add new vertex to visited set
        visited.add(vertex)
        # DFS search
        for edge in revGraph[vertex]:
            if edge not in visited:
                parents[edge] = vertex
                DFS(edge, revGraph, parents)
        # building topological ordering
        for i in range(len(topological_order)):
            if topological_order[i] is None:
                topological_order[i] = vertex
                break
    
    def DFSAll(revGraph, parents):
        # goes through all unvisited vertices
        for vertex in revGraph:
            if vertex not in visited:
                DFS(vertex, revGraph, parents)

    DFSAll(revGraph, parents)

    # prints the topological order
    for i in range(len(topological_order)):
        if i >= len(topological_order)-1:
            print(topological_order[i])
        else:
            print(topological_order[i], end=" ")
    pass


if __name__ == "__main__":
    main()
"""
name: Alex Polivka & Devon Boldt
This work abides by the JMU honor code.
This code is based off the psuedo code
implementation in the textbook.
"""

from collections import defaultdict


def IsAcylicDFS(graph, visited, vertex):
    # assign vertice to active
    visited[vertex] = 1

    # go through all vertices in original graph
    for option in graph[vertex]:
        # check if vertice has already been seen
        if visited[option] == 1:
            return False
        # check if vertice is new
        elif visited[option] == 0:
            if IsAcylicDFS(graph, visited, option) == False:
                return False
    # update vertice to be finished
    visited[vertex] = 2
    return True

    
def IsAcyclic(graph):
    # graph that keeps track of visited vertices
    visited = defaultdict()

    # assigns every vertice to new
    for vertex in graph:
        visited[vertex] = 0

    # goes through each vertice in original graph
    for vertex in graph:
        # validates veritce is new
        if visited[vertex] == 0:
            # validates there is no cycle
            if IsAcylicDFS(graph, visited, vertex) == False:
                return False
    return True


def main():
    # number of inputs
    inputs = int(input())

    # dictionary to hold vertices
    graph = defaultdict(list)
    
    for x in range(inputs):
        values = input().split()
        graph[values[0]] = values[1:]
        
    # prints False if a cycle happens, True if one doesnt
    print(IsAcyclic(graph))
    

if __name__ == '__main__':
    main()
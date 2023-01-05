"""
name: Alex Polivka
This work abides by the JMU honor code.
Methods dfs_label and count_and_label were
created by John Bowers
This code was implemented based off the textbook
psuedo code for boruvka and addAllSafeEdges 
method in chapter 7.
"""
from collections import defaultdict
import math
from connected_components import count_and_label, dfs_label

# used for DFS search of total cost to lay rail
total = 0.0


def boruvka(graph, weights):
     # implemented based off textbook psuedo code
    f = defaultdict()
    for vertex in graph:
        f[vertex] = []
    count, labels = count_and_label(f)
    while count > 1:
        addAllSafeEdges(count, labels, f, weights)
        count, labels = count_and_label(f)
    return f


def addAllSafeEdges(count, labels, f, weights):
    # implemented based off textbook psuedo code
    safe = [None] * count
    for u, v in weights:
        if labels[u] != labels[v]:
            if safe[labels[u]] == None or weights[(u, v)] < weights[safe[labels[u]]]:
                safe[labels[u]] = (u, v)
            if safe[labels[v]] == None or weights[(u, v)] < weights[safe[labels[v]]]:
                safe[labels[v]] = (u, v)
    for u, v in safe:
        f[v].append(u)
        f[u].append(v)
    
# helper method to find the total
def DFS(vertex, visited, f, weights):
    global total
    visited[vertex] = True
    for e in f[vertex]:
        if not visited[e]:
            total += weights[(vertex, e)]
            DFS(e, visited, f, weights)


def main():
    n = int(input())
    # holds the location of the city x and y on a map
    locations = []

    graph = defaultdict()

    # adding the locations and creating empty graph
    for x in range(n):
        locX, locY = input().split()
        locations.append((locX, locY))
        graph[x] = []
    
    # creating graph 
    for x in range(len(locations)):
        for y in range(len(locations)):
            if x != y:
                graph[x].append(y)

    # finding the weights of each possible connection in the graph
    weights = defaultdict()
    for v in graph:
        for e in graph[v]:
            e0 = float(locations[e][0])
            v0 = float(locations[v][0])
            e1 = float(locations[e][1])
            v1 = float(locations[v][1])
            weights[(v, e)] = math.sqrt((e0-v0)**2 + (e1-v1)**2)

    # creating minimum spanning tree
    f = boruvka(graph, weights)

    # DFS to find total needed to lay rail
    visited = [False] * n
    DFS(0, visited, f, weights)

    # printing rail amount
    print("$" + str(round(total, 1)) + "M")

    pass


if __name__ == "__main__":
    main()
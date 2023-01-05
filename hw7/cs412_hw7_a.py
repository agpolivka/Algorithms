"""
name: Alex Polivka
This work abides by the JMU honor code.
Most of this code was implemented with help
from the psuedo code and references from the chapter
6 in the textbook, especially the helper methods to 
determine edges. The idea of a global variable for my 
clock was assisted by GeeksForGeeks in their 
"Printing pre and post visited times in DFS of a graph", 
as without using the global variable, my pre and post 
visit checks would update incorrectly.
"""

from collections import defaultdict

# global clock used in our DFS
clock = 0


# helper method to print tree edge or forward edge
def tree_or_forward_edge(start, goal, prePost, parents):
    if prePost[start][0] < prePost[goal][0] < prePost[goal][1] < prePost[start][1]:
        if parents[goal] == start:
            print("tree edge")
        else:
            print("forward edge")
    pass


# helper method to print back edge
def back_edge(start, goal, prePost):
    if prePost[goal][0] < prePost[start][0] < prePost[start][1] < prePost[goal][1]:
        print("back edge")
    pass


# helper method to print cross edge
def cross_edge(start, goal, prePost):
    if prePost[goal][1] < prePost[start][0]:
        print("cross edge")
    pass


def DFS(graph, visited, vertex, prePost, parents):
    global clock
    # add new vertex to visited set
    visited.add(vertex)
    # preVisit process
    clock = clock+1
    prePost[vertex][0] = clock

    # DFS search
    for edge in graph[vertex]:
        if edge not in visited:
            parents[edge] = vertex
            DFS(graph, visited, edge, prePost, parents)

    # postVisit process
    clock = clock+1
    prePost[vertex][1] += clock
    pass

    
def DFSAll(graph, vertex_order, prePost, parents):
    
    # holds visited vertexes from vertex_order
    visited = set()

    # goes through all unvisited vertices
    for vertex in vertex_order:
        if vertex not in visited:
            DFS(graph, visited, vertex, prePost, parents)

    # convert prePost list to tuples
    for vertex in prePost:
        prePost[vertex] = tuple(prePost[vertex])

    return parents, prePost


def main():
    
    # number of vertices
    n = int(input())

    # dictionary to hold vertices
    graph = defaultdict(list)
    
    # holds vertex ordering for outerloop of traversal
    vertex_order = []

    # building graph
    for x in range(n):
        values = input().split()
        graph[values[0]] = values[1:]
    
    # getting vertex order
    vertex_order = input().split()

    # the number of edge queries
    m = int(input())

    # parent of vertices
    parents = {}

    # tracks a vertices pre and post visit times
    prePost = {}

    # setting parents and prePost to empty values
    for vertex in graph:
        parents[vertex] = ()
        prePost[vertex] = [0, 0]

    # getting the updated parent and prePost dictionaries
    parents, prePost = DFSAll(graph, vertex_order, prePost, parents)

    # getting edge queries
    for x in range(m):

        # getting the start vertex and goal vertex
        start_vertex, goal_vertex = input().split()
        print(start_vertex, goal_vertex, end=" ")

        # checking if the goal vertex is in the graph at the start vertex
        # if not, print illegal edge
        if goal_vertex in graph[start_vertex]:
            # check if an edge is tree edge or forward edge
            tree_or_forward_edge(start_vertex, goal_vertex, prePost, parents)
            # checks if edge is a back edge
            back_edge(start_vertex, goal_vertex, prePost)
            # checks if edge is a gross edge
            cross_edge(start_vertex, goal_vertex, prePost)
        else:
            print("illegal edge")


if __name__ == '__main__':
    main()
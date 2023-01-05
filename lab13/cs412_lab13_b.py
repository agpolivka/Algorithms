"""Reference solution to MST lab.
Determine the minimum cost for a set of railroad lines to connect a
set of cities.
Author: Nathan Sprague & Alex Polivka
Dr. Sprague provide all methods besides dfs and main
"""
import math
#from connected_components import count_and_label

def dfs_label(graph, v, labels, current_label):
    """Version of the iterative dfs that takes as input a list of labels,
    one per vertex, and a starting vertex v and uses iterative
    depth-first-search to label each vertex with a given currentLabel
    Args:
        graph: an adjaceny list with vertices 0-(n-1)
        v (int): The vertex to DFS from
        labels (list): A list of length V which is -1 if the vertex is
            unvisited
        current_label (int): The label to set on every visited vertex
    labels is an out-parameter and will be modified during this
    operation.
    """
    bag = [v]
    while bag:  # while bag is not empty
        u = bag.pop()
        if labels[u] == -1:
            labels[u] = current_label
            for w in graph[u]:
                bag.append(w)
def count_and_label(graph):
    """Count the number of connected components in the graph and label
    each vertex with its connected component index.
    Args:
        graph:  given as an adjaceny list/set structure with vertices 0..(n-1)
    Returns:
        count, labels - where count is the number of connected
        components in the graph and labels is the labeling of each
        vertex's connected component starting from index 0.
    """
    labels = [-1 for _ in range(len(graph))]  # Initially all labels are 0
    count = -1
    for v in range(len(graph)):  # for each vertex
        if labels[v] == -1:  # if v is not visited
            count += 1
            dfs_label(graph, v, labels, count)
    return count+1, labels


def distance(point_a, point_b):
    return math.sqrt((point_a[0] - point_b[0])**2 +
                     (point_a[1] - point_b[1])**2)


def read_points():
    """Read a sequence of two-d points from stdin."""
    n = int(input())  # First line is the number of points.
    points = []
    for _ in range(n):
        points.append([float(i) for i in input().split(" ")])
    return points


def build_weight_matrix(points):
    """Construct a weight matrix from the provided 2d coordinates.
    Args:
        points: sequence of 2d points represented as lists or tuples.
    Returns:
        list of lists representing a weight matrix where entries correspond to
        Euclidean distances between points.
    """
    n = len(points)
    # Initialize all weight entries to ininity...
    weights = [[float('inf')] * n for _ in range(n)]
    # Build the weight matrix...
    for i in range(n):
        for j in range(i + 1, n):
            weights[i][j] = distance(points[i], points[j])
            weights[j][i] = weights[i][j]
    return weights


def add_all_safe_edges(weights, F, count, labels):
    # Initialize the list of safe edges.  We'll also keep track of the
    # weight associated with the best edge we've seen so far
    # (initialized to infinity). Saves us some checks in the inner
    # loop. Tuples contain (u, v, weight(uv)).
    safe = [(-1, -1, float('inf'))] * count
    for u in range(len(weights)):
        for v in range(u + 1, len(weights)):
            if labels[u] != labels[v]:
                weight = weights[u][v]
                if weight < safe[labels[u]][2]:
                    safe[labels[u]] = (u, v, weight)
                if weight < safe[labels[v]][2]:
                    safe[labels[v]] = (u, v, weight)
    for i in range(count):
        F[safe[i][0]].add(safe[i][1])
        F[safe[i][1]].add(safe[i][0])


def boruvka(weights):
    """Find the minimum spanning tree using Boruvka's algorithm.
    Args:
        weights: list of lists representing a weight matrix.
    Returns:
        A list of sets representing the spanning tree graph. Assumes
        vertices are numbered from 0-(v-1).
    """
    F = [set() for i in range(len(weights))]
    count, labels = count_and_label(F)
    while count > 1:
        add_all_safe_edges(weights, F, count, labels)
        count, labels = count_and_label(F)
    return F


def dfs(graph, visited, node, cheapest_path):
    if node not in visited:
        cheapest_path.append(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph, visited, neighbour, cheapest_path)


if __name__ == "__main__":
    points = read_points()
    weight_matrix = build_weight_matrix(points)
    graph = boruvka(weight_matrix)
    visited = []
    cheapest_path = []
    dfs(graph, visited, 0, cheapest_path)
    print(*cheapest_path)
    

"""
name: Alex Polivka and Devon Boldt
This work abides by the JMU honor code.
This work is based off psuedo code from 
chapter 8 in our textbook.
"""
from collections import defaultdict
import math
from queue import PriorityQueue

def init_sssp(start, vertices):
        dist = defaultdict()
        pred = defaultdict()
        dist[start] = 0
        pred[start] = None
        for vertex in vertices:
            if vertex != start:
                dist[vertex] = float('inf')
                pred[vertex] = None
        return dist, pred

def relax(dist, pred, u, v, weights):
        dist[v] = dist[u] + weights[(u, v)]
        pred[v] = u
        return dist, pred

def dijkstras(start, vertices, edges, weights):
    
    dist, pred = init_sssp(start, vertices)
    pq = PriorityQueue()
    for vertex in vertices:
        pq.put((vertex, dist[vertex]))

    while not pq.empty():
        get = pq.get()
        u = get[0]
        for v in edges[u]:
            if (u, v) in weights:
                if (dist[u] + weights[(u, v)]) < dist[v]:
                    dist, pred = relax(dist, pred, u, v, weights)
                    pq.put((v, dist[v]))
    return dist

def main():
    n, m, q = [int(x) for x in input().split()] 
    vertices = defaultdict()
    weights = {}
    edges = {}
    for x in range(n):
        vertices[x] = set()
        edges[x] = []

    for x in range(m):
        start, end, weight = [int(x) for x in input().split()] 
        vertices[start].add(end)
        weights[(start, end)] = weight

    for x in range(n):
        for y in range(n):
            if x != y:
                edges[x].append(y)

    for x in range(q):
        start, end = input().split()
        path_length = dijkstras(int(start), vertices, edges, weights)
        value = path_length[int(end)]
        if value == float('inf'):
            print("Impossible")
        else:
            print(value)
    pass


if __name__ == "__main__":
    main()
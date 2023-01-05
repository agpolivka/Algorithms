"""Max-Flow Min-Cut Implementation.

Author(s): Nathan Sprague, Alex Polivka, Devon Boldt
Honor Code Statement:
This code abides by the JMU Honor Code.
draw_graph, zero_flow, and demo_drawing were
provided by Dr. Sprague as helper/starter code.

"""
from collections import defaultdict, deque


def main():
    num_nodes, num_edges = [int(i) for i in input().split(" ")]
    connections = defaultdict(set)
    capacities = defaultdict()
    nodes = []

    for x in range(num_edges):
        start, end, total = [int(i) for i in input().split(" ")]
        connections[start].add(end)
        capacities[(start, end)] = [0, total]
        if start not in nodes:    
            nodes.append(start)
        if end not in nodes:
            nodes.append(end)
    
    def improvements():
        visited_nodes = set()
        queue = deque()
        queue.append((0,0))
        search = []
        nodes_reached = set()
        while queue:
            prev, curr = queue[0]
            visited_nodes.add(curr)
            search.append((prev, curr))
            if curr == nodes[-1]:
                path = []
                smallest = float('inf')
                first, last = search[-1]
                while first != nodes[0]:
                    for i in range(len(search)):
                        if search[i][1] == first:
                            if smallest > capacities[(first, last)][1]-capacities[(first, last)][0]:
                                smallest = capacities[(first, last)][1]-capacities[(first, last)][0]
                            path.append((first,last))
                            last = first
                            first = search[i][0]
                for i in path:
                    capacities[i][0] += smallest
                return nodes_reached
            queue.popleft()
            for node in connections[curr]:
                if capacities[(curr, node)][0] < capacities[(curr, node)][1]:
                    if node not in visited_nodes:
                        queue.append((curr, node))
                        nodes_reached.add(node)
        return nodes_reached
    
    reached = improvements()
    while len(reached) > len(nodes)-2:
        reached = improvements()
    
    flow = 0
    cuts = []
    for i in reached:
        for j in connections[i]:
            if j not in reached:
                cuts.append((i, j))
                num = capacities[(i, j)][0]
                flow += num
    print(flow)
    for cut in cuts:
        print(cut[0], cut[1])

if __name__ == "__main__":
    main()
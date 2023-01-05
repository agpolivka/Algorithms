"""
name: Alex Polivka
This work abides by the JMU honor code.
"""
from collections import deque
from collections import defaultdict

def route_finder(connections, goal):
    # queue for destinations we visit
    search = deque()
    # our visited nodes and path to reach the goal
    path = []
    # our final constructed shortest path to the goal
    final_path = []
    # holds the previous connection from the current one
    previous = defaultdict()

    
    search.append(goal[0])
    path.append(goal[0])
    previous[goal[0]] = goal[0]
    
    # BFS that goes through and finds
    # a path for each connection.
    # Finds shortest path to reach the 
    # goal as well
    while search:
        current_dest = search.pop()
        # check if we found our goal and
        # construct shortest path
        if current_dest == goal[1]:
            final_path.append(goal[1])
            while goal[1] is not goal[0]:
                goal[1] = previous[goal[1]]
                final_path.append(goal[1])
            break
        # build possible path
        for neighbor in connections[current_dest]:
            if neighbor not in path:
                search.append(neighbor)
                path.append(neighbor)
                previous[neighbor] = current_dest
    
    

    # checking if final goal is in the path and
    # printing based on that
    if goal[1] not in path:
        print("no route possible")
    else:
        final_path.reverse()
        for step in final_path:
            if step == final_path[-1]:
                print(step)
            else:
                print(step, end=" ")
    pass


def main():
    # dictionary that holds sets 
    connections = defaultdict(set)

    # loop counter
    num_connections = int(input())

    # loop that helps aquire all possible connections
    for x in range(num_connections):
        values = input().split()
        connections[values[0]].add(values[1])
        connections[values[1]].add(values[0])
    
    # array holding final trip destinations, use 0 to access
    # start of trip and 1 to access goal destination
    final_trip = input().split()

    #should print final path if one exists
    route_finder(connections, final_trip)

if __name__ == '__main__':
    main()
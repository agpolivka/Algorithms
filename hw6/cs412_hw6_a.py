"""
name: Alex Polivka
This work abides by the JMU honor code.
"""


def island_finder(map, row, col, found_islands):
    
    # checks if we are out of bounds
    if row < 0 or row == len(map) or col < 0 or col == len(map):
        return 0

    # checks if we are on an ocean tile
    if map[row][col] == "0":
        return 0
    
    # checks if we have already visited this island acre
    if (row, col) in found_islands:
        return 0
    
    # add the newly found acre of the island
    found_islands.add((row, col))

    # recursively go through the map and find more acres of the island
    # add 1 every time since we have found a new one
    return (island_finder(map, row+1, col, found_islands) +
            island_finder(map, row-1, col, found_islands) +
            island_finder(map, row, col+1, found_islands) +
            island_finder(map, row, col-1, found_islands) + 1)


def main():

    # loop counter
    map_size = int(input())

    # islands acres we have already seen
    found_islands = set()

    # map to hold the grid
    map = []

    # loop that helps acquire all possible connections
    for x in range(map_size):
        map.append(input().split())

    possible_acres = []
    # searching for island count
    for x in range(len(map)):
        for y in range(len(map)):
            possible_acres.append(island_finder(map, x, y, found_islands))
            found_islands = set()

    # print the highest area in the array
    print(max(possible_acres))

    
if __name__ == '__main__':
    main()
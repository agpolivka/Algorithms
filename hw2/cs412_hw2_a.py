"""
    name: Alex Polivka
    This work abides by the JMU honor code.
    Assistance: Looking at Lab3 work
    and the idea given by Dr. Sprague
    that this problem was similar to the 
    "Sub Set Sum" backtracking problem.
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
import re
import collections


def rocket_counter(values, target_length, index_o):
    
    # returns the empty list if we have found perfect values
    if target_length == 0:
        return []
    # checks if index value is still greater than or equal
    elif target_length - int(values[index_o]) >= 0:
        return [values[index_o]]+rocket_counter(values, target_length-int(values[index_o]), index_o)
    else:
        return rocket_counter(values, target_length, index_o-1)
    
    
def main():
    # possible rocket_count target_lengths
    values = re.split(' ', input())

    # goal target_length of rocket_count
    target_length = int(input())

    # the starting index option for possible valid options
    index_o = 0

    # list that holds all possible valid, length options 
    rocket_count = []

    # loop that goes through and allows each
    # index to be an option as the starting base value
    while index_o < len(values):
        rocket_count.append(rocket_counter(values, target_length, index_o))
        index_o += 1

    # sorting the list based on the length of each array
    rocket_count = sorted(rocket_count, key=len)

    # creating a collection that holds the number of instances of a value
    num_occurences = collections.Counter(rocket_count[0])

    # prints out the number of occurences of a certain rocket part
    for value in values:
        if value in num_occurences:
            print(num_occurences[value], 'of length', value)
        else:
            print('0 of length', value)
    
    # printing number of rocket_ccount pieces
    print(len(rocket_count[0]), "rocket sections minimum")

    pass


if __name__ == "__main__":
    main()


"""
    name:  Alex Polivka
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
from typing import OrderedDict


def main():
    # your code here
    # grabbing the animal noises and the number of other recorded animals
    sounds = input().split(" ")
    num_animals = int(input())
    # Make dictionary to store words and value
    dictionary = dict()
    # holds what the fox officially does say
    fox_says = ""
    # holds the animals we heard in the woods besides the fox
    other_animals_heard = []

    # adding sounds to animals in dictionary
    for x in range(num_animals):
        line = input().split(" ")
        if line[2] not in dictionary:
            dictionary[line[2]] = line[0]

    # adding to what fox says based on missing sounds
    for sound in sounds:
        if sound not in dictionary:
            fox_says += sound + " "
        else:
            other_animals_heard.append(dictionary[sound])

    # clearing duplicates from the list in the order they are found
    final_oah = list(OrderedDict.fromkeys(other_animals_heard))

    if fox_says == "":
        print("what the fox says: ")
    else:
        print("what the fox says: " + fox_says)
    if final_oah:
        print("also heard: " + " ".join(final_oah), end=" \n")
    else:
        print("also heard: ")
    pass

if __name__ == "__main__":
    main()

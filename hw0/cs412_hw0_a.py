"""
    name: Alex Polivka
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def main():
    # your code here
    # grabbing the animal noises and the number of other recorded animals
    sounds = input().split(" ")
    num_animals = int(input())
    # animals holds the type of known animals
    animals = []
    # holds the sounds of known animals
    animals_sounds = []
    # holds the animals we heard in the woods besides the fox
    oah = []
    # holds what the fox officially does say
    fox_says = ""
    # adding animals and sounds to arrays
    for x in range(num_animals):
        line = input().split(" ")
        animals.append(line[0])
        animals_sounds.append(line[2])

    # keeps track of what animal we are at
    counter = 0

    for sound in sounds:
        # grabs what the fox says
        if sound not in animals_sounds:
            fox_says += sound + " "
        # figures out what the other animal is since its not a fox noise
        else:
            for animal_sound in animals_sounds:
                # uses a continous counter that figures out what animal
                # we are on based off mod operation
                if sound == animal_sound:
                    if animals[counter % num_animals] not in oah:
                        oah.append(animals[counter % num_animals])
                counter += 1

    # printing the results
    if fox_says == "":
        print("what the fox says: ")
    else:
        print("what the fox says: " + fox_says)
    if oah:
        print("also heard: " + " ".join(oah), end=" \n")
    else:
        print("also heard: ")

    pass
if __name__ == "__main__":
    main()

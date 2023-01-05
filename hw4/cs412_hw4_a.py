"""
name: Alex Polivka
This work abides by the JMU honor code.
CS 412 HW2 Reference Solution used for structure
of HW3 which this code is modified from. Reference
solution from Dr. Sprague.

"""


def min_finder(sizes, target):
    
    # 2D List to hold number of parts needed
    parts_used = [[0 for x in range(target + 1)] for x in range(len(sizes) + 1)]

    # Initialize the array to worse case scenario
    # to check against. (worst case scenario is 
    # the smallest part size put in the max number
    # of times to reach target, plus one is incase of
    # odd number target)
    for i in range(1, target + 1):
        parts_used[0][i] = target//sizes[0]+1

    def min_sections(len_sizes):
        # Note: we dont need basic index checks
        # like in last project as the for loops
        # will deal with checks

        # Loop to find the solution by getting previous
        # num parts of sequence
        for i in range(1, len_sizes + 1):
            for test_t in range(1, target + 1):
                # check if current part is bigger than test target
                if (sizes[i - 1] > test_t):
                    # if its bigger, grab previous part number
                    # because it wont fit in the target size attempt
                    parts_used[i][test_t] = parts_used[i - 1][test_t]
                else:
                    # Current minimum possible based on previous
                    # minimum value of the sequence
                    if parts_used[i - 1][test_t] > parts_used[i][test_t - sizes[i - 1]] + 1:
                        parts_used[i][test_t] = parts_used[i][test_t - sizes[i - 1]] + 1
                    else:
                        parts_used[i][test_t] = parts_used[i - 1][test_t]
        # return minimum parts
        return parts_used[len_sizes][target]

    return min_sections(len(sizes))


def main():
    # grabs part lengths
    sizes = [int(i) for i in input().split()]
    # grabs target value
    target = int(input())
    # finds the number of rocket sections at a minimum needed
    num_sections = min_finder(sizes, target)
    print(f'{num_sections} rocket sections minimum')


if __name__ == '__main__':
    main()
 

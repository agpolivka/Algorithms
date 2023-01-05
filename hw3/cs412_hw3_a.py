"""
name: Nathan Sprague & Alex Polivka
This work abides by the JMU honor code.
CS 412 HW2 Reference Solution (partial credit version).
This solution is modeled after the SubsetSum algorithm on p. 78 of the
Erickson textbook.
The rest of this code is slightly altered from the
Reference Solution and adds a dictionary of tuples
to monitor if a value has happened before and returns
that value if it has to speed up the algorithm.

"""

def min_finder(sizes, target):
    # dictionary that will hold memoized part values
    values_dict = {}

    def min_sections(i, t):

        # tuple to check the index and target in the dictionary
        tuple = (i, t)

        # checks if dictionary contains a part value
        # at the given tuple
        if values_dict.get(tuple):
            return values_dict[(tuple)]

        # checks size of target for successful completion
        if t == 0:
            return 0
        elif i == -1:  # (t will never be negative.)
            return None

        # alogirthm to find number of rocket parts
        max_possible = t // sizes[i]
        best = float('inf')
        for n in range(max_possible + 1):
            cur = min_sections(i - 1, t - n * sizes[i])
            if cur is not None:
                if cur + n < best:
                    best = cur + n
        # updates dictionary with num part values
        values_dict[tuple] = best
        return best
    
    return min_sections(len(sizes)-1, target)


def main():
    # grabs part lengths
    sizes = [int(i) for i in input().split()]
    # grabs target value
    target = int(input())
    # finds the number of rocket sections at a minimum needed
    num_sections = min_finder(sizes, target)
    print(f'{num_sections} rocket sections minimum')

if __name__ == "__main__":
    main()
    
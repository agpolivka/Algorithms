"""
    name: Alex Polivka & Devon Boldt
    This work abides by the JMU Honor Code.
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts

# helper method to determine if an expression is a palindrome
def is_palindrome(expression):
    return expression == expression[::-1]


def backtrack_palindrome(expression, start, end):
    # holds number of palindrome partitions found
    counter = 0

    # checks the length of the palindrome and returns
    # a value of 1 if it is length 0 or 1. An empty string
    # is considered a palindrome in this example
    if len(expression) == 0 or len(expression) == 1:
        return 1
    
    # for loop that goes through each value and 
    # makes a partition on it and starts to check if
    # it is a palindrome
    for x in range(start+1, end):
        # partitioned substring to check for palindrome
        substring = expression[:x]

        # checks if the value is a palindrome, if it is 
        # keep checking for more, if its not ignore
        if is_palindrome(substring):
            # recursive call that counts how many more 
            # palandromes are found after the original palindrome 
            # is found. 
            counter += backtrack_palindrome(expression[x:], start, len(expression[x:])+1)
    return counter         


def main():
    # grabs the number of words we will check for partitioning
    num_lines = int(input())

    # goes through each lineand grabs the word
    # that will be checked
    for x in range(num_lines):
        # grabs word
        expression = input()
        # recursive call to count words
        num_palindromes = backtrack_palindrome(expression, 0, len(expression)+1)
        # prints return value
        print(num_palindromes)
    pass

if __name__ == "__main__":
    main()
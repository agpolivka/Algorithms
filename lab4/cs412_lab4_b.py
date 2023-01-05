"""CS 412 Lab 2: Counting Palindromic Partitions.
Author: Nathan Sprague, Alex Polivka, and Devon Boldt
This code abides by the JMU Honor Code.
Parts of this code were provided by Dr. Sprague, 
such as the main() and is_segment_palindrome(). 
Dr. Sprague also provided the idea of using 
nested functions.
"""

# Palindrome check parent function
def palindrome_check(input_string):
    # Holds palindrome partition values
    palindrome_list = [None] * (len(input_string) +1)

    # Nested function as required from the project specs
    def palindrome_counter(input_string, index):
        
        count = 0
        partitioned_string = ''

        # creates string to be checked
        for i in range(index, len(input_string), 1):
            if i < len(input_string):
                partitioned_string += input_string[i]

        # Return different palindrome partitions values if it exists 
        if palindrome_list[index]:
            return palindrome_list[index]

        # Single element case
        if len(partitioned_string) <= 1:
            return 1

        # Counting the various counts 
        for i in range(1, len(partitioned_string)+1):
            if is_segment_palindrome(partitioned_string, 0, i-1):
                count += palindrome_counter(input_string, i + index)
        palindrome_list[index] = count
        return count
    return palindrome_counter(input_string, 0)

# Function directly copied from Dr. Sprague's writ
def is_segment_palindrome(input_string, start, end):
    """Check if partitioned_string from start to end (inclusive) is a palindrome."""
    for i in range((end - start + 1) // 2):
        if input_string[i + start] != input_string[end - i]:
            return False
    return True

# Main function
def main():
    n = int(input())
    for _ in range(n):
        letters = input()
        print(palindrome_check(letters))

# Calls main 
if __name__ == "__main__":
    main()
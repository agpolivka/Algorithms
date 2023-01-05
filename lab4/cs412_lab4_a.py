"""CS 412 Lab 2: Counting Palindromic Partitions.
Author: Nathan Sprague, Alex Polivka, and Devon Boldt
This code abides by the JMU Honor Code.
The bulk of this code was provided by Dr. Sprague
as starter code that needed minimal changes so that
the code would run more efficiently with help of a dictionary.

"""
def is_palindrome(letters):
    return letters == letters[::-1]

def count_pal_parts(letters, dictionary):
    
    if len(letters) == 0:
        return 1
    if letters in dictionary:
        return dictionary[letters]
    else:
        count = 0
        for i in range(len(letters)):
            start = letters[:i+1]
            rest = letters[i+1:]
            if is_palindrome(start):
                count += count_pal_parts(rest, dictionary)
        dictionary[start] = count
        return count
def main():
    n = int(input())
    dictionary = dict()
    for _ in range(n):
        letters = input()
        print(count_pal_parts(letters, dictionary))

if __name__ == "__main__":
    main()
"""
    name: Alex Polivka
    This work abides by the JMU honor code.
    Assistance: I took the advice of Dr. Sprague to look at
    this problem in more of a tree form. This required rewriting
    my original code to more appropriately let every
    operand appear as the "root" of a tree and evaluate to
    the left and right of the "root" every time recursively by
    taking slices of the array. I recieved this help from both of his help videos
    that he posted in Canvas
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
import re


def min_max_expr(expression):
    # list that holds our results
    expr_results = []

    # Returning a list containing a single value
    # as that is the only value left in our expression
    # or was the only value in the original expression
    if len(expression) == 1:
        return [int(expression[0])]

    # A for loop that evaluates all operators in
    # the expression as the "root". It does this
    # by starting our x value at the first known
    # root which is expression[1]. Then continue
    # to increment by 2 as that will keep getting
    # the next operator
    for operator in range(1, len(expression), 2):

        # these list contain all of the possible values
        # to the left and right of our root. Allowing us
        # to evaluate where all the possible parenthesis could
        # be placed
        left_possible = min_max_expr(expression[:operator])
        right_possible = min_max_expr(expression[operator+1:])

        # these two for loops go through all of our possibilities
        # and perform the operator on the operands that were next to
        # it. then it keeps track of all results in a list
        for left_values in range(len(left_possible)):
            for right_values in range(len(right_possible)):
                if expression[operator] == '+':
                    expr_results += [left_possible[left_values] + right_possible[right_values]]
                if expression[operator] == '-':
                    expr_results += [left_possible[left_values] - right_possible[right_values]]
                if expression[operator] == '*':
                    expr_results += [left_possible[left_values] * right_possible[right_values]]

    # sorts our final list of options to make it
    # easier for our main method to find the min and
    # max
    expr_results.sort()
    return expr_results


def main():
    # getting input string
    expression = re.split('(\+|\*|\-)', input())
    # calling our recursive function and assigning final values
    values = min_max_expr(expression)
    # printing the results of highest and lowest value
    print(values[0], values[-1])
    pass


if __name__ == "__main__":
    main()

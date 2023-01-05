"""
name: Alex Polivka
This work abides by the JMU honor code.

The major operations in this code are the sort method
on line 22 and the for loop on line 30. The sort method runs
in O(nlgn) time and the for loop in O(n) time. We don't care 
about the O(n) time because we already have a higher run
time in the O(nlgn). That is to say the algorithm runs in 
O(nlgn) time anyways so the O(n) would not change that. You
could also take the for loop used in main, but it again
has O(n) run time

The greedy choice my algorithm makes is to sort the 
list of days by highest to lowest, and then choose
that highest value as the minimum number of days remaining
for Dr. Spragues party to be ready. The next greedy choice
is that it checks the number of days behind it to see if
it should be incrementing the number of days remaining
but you could easily get an incorret output.
"""


def min_days_finder(days):
    
    # sorts the number of days needed from highest to lowest
    days.sort(key=lambda day: day, reverse=True)
    
    # takes the most amount of possible days it could take
    days_remaining = days[0]
    
    # goes through all the days and checks if 
    # the number of days remaining needs to 
    # be incremented
    for x in range(1, len(days)):
        # if the number of days needed previously
        # is the same as the current number,
        # increment days remaining by 1
        if days[x-1] == days[x]:
            days_remaining += 1
        
    return days_remaining


def main():
    # grabs number of days and adds two to them to 
    # get total time it would take to grow
    days = [int(i)+2 for i in input().split()]
    
    # earliest number of days from today when the
    # party can be organized
    enod = min_days_finder(days)
    print(enod)


if __name__ == '__main__':
    main()
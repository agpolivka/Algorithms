"""CS 412 Lab 6: Greedy Algorithms.
Author: Alex Polivka and Devon Boldt

"""

# Palindrome check parent function
def fractional_knapsack(knapsack_w, valuables):
    knapsack_weight = float(knapsack_w)
    # holds the total amount of "money" we could ransack
    total_ransacked = 0.0

    # holds the result string that tells us type, value, and
    # weight of the item we ransacked
    results = ""
    # sorts our 2D array by best ratio 
    valuables.sort(key=lambda col: (float(col[1])/float(col[2])), reverse=True)
    
    # goes through values and asses if they can be
    # added to our knapsack or not
    for x in range(len(valuables)):
        if knapsack_weight > 0:
            # checks if we can add it to our ransack
            if float(valuables[x][2]) <= knapsack_weight:
                knapsack_weight -= float(valuables[x][2])
                total_ransacked += float(valuables[x][1])
            # finds the fraction of the item we can add
            # and puts it into ransack and updates the weight
            # and price values to the those ratios     
            else:
                total_ransacked += knapsack_weight/float(valuables[x][2]) * float(valuables[x][1])
                valuables[x][1] = knapsack_weight/float(valuables[x][2]) * float(valuables[x][1])
                valuables[x][2] = knapsack_weight
                knapsack_weight -= valuables[x][2]
            #print(valuables)
            # formats our resulting values of weight and price
            price_format = "{:.2f}".format(float(valuables[x][1]), 1)
            weight_format = "{:.2f}".format(float(valuables[x][2]), 1)
            if float(valuables[x][1]) > 0.0:
                results += str(valuables[x][0])+ "(" + price_format + ", " + weight_format + ") "

    print(results.strip())
    return total_ransacked


# Main function
def main():
    # gets the weight we can hold in knapsack
    knapsack_weight = int(input())

    # tells us how many things we can examine
    num_values = int(input())

    # holds our valuables, prices, and weights
    valuables = []
    for x in range(num_values):
        valuables.append(input().split()) 
    
    # grabs the amount we can ransack
    total = fractional_knapsack(knapsack_weight, valuables)
    print(total)
    pass
# Calls main 
if __name__ == "__main__":
    main()
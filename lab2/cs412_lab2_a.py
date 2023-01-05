"""
    name: Alex Polivka & Devon Boldt
"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def find_in_sorted(items, key):
    return find_in_sorted_recursive(items, 0, len(items), key)
def find_in_sorted_recursive(items, start, end, key):

    length = end - start

    # No items in array case
    if length <= 0:
        return -1
    # Key is the only element case
    elif length == 1:
        if items[end-1] != key:
            return -1
        else:
            return 0

    # index of the middle element
    if length % 2 == 1:
        middle_element = start + length // 2 +1
    else:
        middle_element = start + length // 2
    

     
    # checks the middle element first
    if items[middle_element] == key:
        return middle_element
    elif (items[end - 1] < key) and (items[middle_element] > key):
        return find_in_sorted_recursive(items, start, middle_element, key)
    else:
        return find_in_sorted_recursive(items, middle_element, end, key)


# your code here
# grabbing the numbers and the target number
line = input().split()
target = int(input())
num_list = []
for item in line:
    num_list.append(int(item))

#start = 0
#end = len(num_list)
print(find_in_sorted(num_list, target))
    



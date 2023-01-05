"""
Authors: Alex Polivka and Devon Boldt
This work abides by the JMU Honor Code
Problem 1: 2^3 = 8 clauses to make an unsatisfiable 
sentence.
(x1 V x2 V x3) ^ (x1 V x2 V -x3) ^ (x1 V -x2 V x3) ^ (-x1 V x2 V x3) ^
(x1 V -x2 V -x3) ^ (-x1 V -x2 V x3) ^ (-x1 V x2 V -x3) ^ (-x1 V -x2 V -x3) 

"""
from itertools import product

def all_bool_assignments(list):
    values = product([True, False], repeat=2)
    for value in values:
        holder = dict()
        holder[list[0]]=value[0]
        holder[list[1]]=value[1]
        yield holder
    pass


def is_satisfiable(arb_expr, list):
    
    dictionary = {}
    revdict = {}
    counter = len(list)-1
    for val in list:
        dictionary[val] = True
        revdict[counter] = val
        counter -= 1
    flag = 0
    newcount = 0
    for x in range(2**len(list)):
        
        if eval(arb_expr, {'__builtins__': None}, dictionary):
            for val in dictionary:
                print(val , "=" , dictionary[val])
                flag = 1
            break
        val = newcount%len(list)
        dictlookup_char = revdict[val]
        dictionary[dictlookup_char] = not dictionary[dictlookup_char]
        newcount += 1
    if flag == 0:
        print("NO") 

    
    
    pass


def main():
    
    arb_expr = input()
    char_list = []
    for val in input().split():
        char_list.append(val)
    is_satisfiable(arb_expr, char_list)

    # for value in all_bool_assignments(['x', 'y']):
    #     print(value)
    
    

    pass

if __name__ == "__main__":
    main()



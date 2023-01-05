"""
   MergeSort
   coded by Bowers from Jeff Erickson's pseudocode
   Finished by: Devon Boldt and Alex Polivka
"""


# Mergesort Function
def mergesort(A):

    # inv - The amount of inversions
    inv = 0
    if len(A) > 1:
        # Find the mid point
        m = len(A) // 2 
        # Get the left and right halves
        left, right = A[:m], A[m:]  
        # Sort the left and right halves
        inv += mergesort(left)
        inv += mergesort(right) 
        # Copy the sorted left and right halves back to A.
        for i in range(m):
            A[i] = left[i]
        for j in range(m, len(A)):
            A[j] = right[j - m] 
        # Run the merge operation on A
        inv += merge(A, m)
    return inv


# Merge function
def merge(A, m):
    # A contains two sorted sublists, 0..m-1 and m..end.  This function
    # will merge them so that A is entirely sorted.
    i, j = 0, m

    inv = 0

    n = len(A)
    B = [0 for _ in range(n)]  # List to merge into

    for k in range(n):

        if j >= n:          # Right sub-list is exhausted.
            B[k] = A[i]
            i += 1

        elif i >= m:        # Left sub-list is exhausted.
            B[k] = A[j]
            j += 1

        elif A[i] <= A[j]:  # Item from left sub-list "wins"
            B[k] = A[i]
            i += 1

        else:               # Item from right sub-list is smaller
            B[k] = A[j]
            j += 1
            inv += 1

    for k in range(n):      # Copy merged values back to original list.
        A[k] = B[k]
    return inv


def main():
    # Appending code, mostly used from part A
    lines = input().split()
    A = []

    for item in lines:
        A.append(int(item))
    print(mergesort(A))

# Unused for this project
if __name__ == "__main__":
    main()
"""Multiple algorithms for calculating Fibonacci numbers."""
def rec_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fibo(n - 1) + rec_fibo(n - 2)

    
def mem_fibo(n):
    F = [-1] * (n + 1)
    def mem_fibo_rec(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if F[n] == -1:
                F[n] = mem_fibo_rec(n - 1) + mem_fibo_rec(n - 2)
        return F[n]
    return mem_fibo_rec(n)


def iter_fibo(n):
    F = [-1] * (n + 1)
    F.append(0)
    F.append(1)
    for x in range(2, n+1):
        F[x] = F[x-1] + F[x-2]    
    return F


if __name__ == "__main__":
    print("Recursive")
    for i in range(35):
        print(rec_fibo(i), end=" ")
    print('\n\nMemoization')
    for i in range(35):
        print(mem_fibo(i), end=" ")
    print('\n\nIterative')
    for i in range(35):
        print(iter_fibo(i), end=" ")
    print('\n\nIterativeFibo')
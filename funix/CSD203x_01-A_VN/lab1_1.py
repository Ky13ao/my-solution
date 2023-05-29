# Uses python3
fib = [0,1]
def calc_fib(n):
    if (n <= len(fib)):
        if (n==len(fib)):
            fib.append(fib[n-1]+fib[n-2])
        return fib[n]
    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
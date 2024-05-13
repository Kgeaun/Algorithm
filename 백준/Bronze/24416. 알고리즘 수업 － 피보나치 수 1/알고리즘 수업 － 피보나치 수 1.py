import sys

n = int(sys.stdin.readline())
c1 = 0
c2 = 0

def fib(n):
    global c1
    if n == 1 or n == 2:
        c1 += 1
        return 1  # 코드1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global c2
    fibonacci = [0, 1, 1]
    for i in range(3, n+1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2]) # 코드2
        c2 += 1
    return fibonacci[n]
fib(n), fibonacci(n)
print(c1, c2)
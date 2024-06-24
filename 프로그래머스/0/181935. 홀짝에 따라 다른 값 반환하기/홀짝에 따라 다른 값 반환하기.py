def solution(n):
    sum = 0
    
    if n % 2 == 0:
        for i in range(n, 0, -2):
            sum += i*i
    elif n % 2 != 0:
        for i in range(n, 0, -2):
            sum += i

    return sum
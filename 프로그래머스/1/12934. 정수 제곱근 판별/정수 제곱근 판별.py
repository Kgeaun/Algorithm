def solution(n):
    answer = 0
    x = n ** (1/2)
    if x % 1 == 0:
        answer = (x + 1) ** 2
    else:
        answer = -1
    return answer
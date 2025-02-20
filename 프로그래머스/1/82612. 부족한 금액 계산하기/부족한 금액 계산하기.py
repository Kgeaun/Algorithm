def solution(price, money, count):
    answer = 0
    sum1 = 0
    for i in range(1, count+1):
        sum1 += price * i
    if sum1 > money:
        answer = sum1 - money
    else:
        answer = 0
    return answer
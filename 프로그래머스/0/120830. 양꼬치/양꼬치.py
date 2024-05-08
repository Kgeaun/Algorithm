'''
양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 

1인분 12000원, 음료 2000원
그러나 10인분 먹으면 서비스 음료 1개
n = 양꼬치, k = 음료
'''
def solution(n, k):
    sum = (n*12000) + (k*2000)
    if n >= 10:
        for _ in range(n):
            sum -= 2000
            n -= 10
            if n < 10:
                break
    return sum
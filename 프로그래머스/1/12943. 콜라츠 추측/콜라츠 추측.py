def solution(num):
    answer = 0
    while(1):
        if num % 2 == 0:
            num = num // 2
            answer = answer+1
        elif num == 1:
            break
        else:
            num = num * 3 +1
            answer = answer+1
        if answer >= 500:
            answer = -1
            break
    return answer
def solution(x):
    answer = True
    num = 0
    x = str(x)
    for i in range(len(x)):
        num += int(x[i])
    if int(x) % num == 0:
        answer = True
    else:
        answer = False
    return answer
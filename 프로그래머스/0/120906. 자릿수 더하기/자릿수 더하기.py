def solution(n):
    answer = 0
    str1 = str(n)
    for i in range(len(str1)):
        answer += int(str1[i])
    return answer
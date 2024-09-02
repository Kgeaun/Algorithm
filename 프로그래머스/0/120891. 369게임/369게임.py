def solution(order):
    answer = 0
    s = str(order)
    for i in range(len(s)):
        if s[i] == '3' or s[i] == '6' or s[i] == '9':
            answer += 1
    return answer
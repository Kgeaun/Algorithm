def solution(s):
    answer = ''
    num = 0
    if len(s) % 2 != 0:
        num += (len(s) // 2)
        answer += s[num]
    else:
        num += (len(s) // 2)
        answer += s[num-1] + s[num]
    return answer
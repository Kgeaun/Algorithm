def solution(n):
    answer = ''
    s = '수'
    b = '박'
    for i in range(n):
        if i % 2 == 0:
            answer += s
        else:
            answer += b
    return answer
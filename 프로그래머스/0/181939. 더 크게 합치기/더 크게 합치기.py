def solution(a, b):
    if a == b:
        answer = int(str(a)+str(b))
    else:
        n1 = int(str(a)+str(b))
        n2 = int(str(b)+str(a))
        answer = max(n1, n2)
    return answer
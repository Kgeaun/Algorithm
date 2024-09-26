def solution(myString):
    myString += 'x'
    answer = []
    c = 0
    for i in range(len(myString)):
        if myString[i] == 'x':
            answer.append(c)
            c = 0
        else:
            c += 1
    return answer
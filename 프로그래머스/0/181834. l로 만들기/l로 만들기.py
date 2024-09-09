def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if ord(myString[i]) > ord('l'):
            answer += myString[i]
        else:
            answer += 'l'
    return answer
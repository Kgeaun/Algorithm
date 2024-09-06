def solution(myString):
    answer = ''
    
    for modeep in myString:
        if modeep.lower() == 'a':
            answer += modeep.upper()
        else:
            answer += modeep.lower()
    return answer

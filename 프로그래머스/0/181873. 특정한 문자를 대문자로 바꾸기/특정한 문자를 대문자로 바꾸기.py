def solution(my_string, alp):
    answer = ''
    
    for i in range(len(my_string)):
        if my_string[i] in alp:
            answer += my_string[i].upper()
        else:
            answer += my_string[i]
    return answer
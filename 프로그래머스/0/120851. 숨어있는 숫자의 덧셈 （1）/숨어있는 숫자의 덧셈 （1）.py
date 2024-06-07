def solution(my_string):
    answer = 0
    
    for i in range(len(my_string)):
        if my_string[i].isdigit( ): # .isdigit( ) <- 문자가 정수인지 판별해줌
            answer += int(my_string[i])
    return answer

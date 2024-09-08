def solution(my_string, n):
    answer = ''
    num = len(my_string) - n
    for i in range(num, len(my_string)):
        answer += my_string[i]
    return answer
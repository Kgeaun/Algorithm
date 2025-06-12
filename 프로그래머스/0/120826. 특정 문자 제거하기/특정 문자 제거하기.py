def solution(my_string, letter):
    a = ''
    for i in range(len(my_string)):
        if my_string[i] != letter:
            a += my_string[i]
    return a
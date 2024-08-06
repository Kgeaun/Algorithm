import math

def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)
    elif len(num_list) <= 10:
        answer = math.prod(num_list)
    return answer
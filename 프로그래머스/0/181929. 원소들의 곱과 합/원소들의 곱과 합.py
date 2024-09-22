def solution(num_list):
    answer = 0
    sum1 = 0
    num = 1
    for i in range(len(num_list)):
        sum1 += num_list[i]
        num *= num_list[i]
    if num < (sum1*sum1):
        answer = 1
        
    return answer
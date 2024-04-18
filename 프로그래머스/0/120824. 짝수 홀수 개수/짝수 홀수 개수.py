def solution(num_list):
    answer = []
    sum1 = 0
    sum2 = 0
    
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            sum1 += 1
        else:
            sum2 += 1
    answer.append(sum1)
    answer.append(sum2)
    
    return answer
def solution(num_list):
    answer = 0
    sum1 = ""
    sum2 = ""
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            sum1 += str(num_list[i])
        else:
            sum2 += str(num_list[i])
    answer = int(sum1) + int(sum2)
    return answer
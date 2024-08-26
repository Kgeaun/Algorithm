def solution(num_list):
    answer = 0
    b1 = 0
    b2 = 0
    
    a1 = num_list[0::2]
    for i in range(len(a1)):
        b1 += a1[i]
    a2 = num_list[1::2]
    for j in range(len(a2)):
        b2 += a2[j]
    
    answer = max(b1, b2)
    return answer
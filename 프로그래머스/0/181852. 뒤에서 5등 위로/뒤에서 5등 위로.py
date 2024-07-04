def solution(num_list):
    for i in range(5):
        min1 = min(num_list)
        num_list.remove(min1)
        
    num_list.sort()
    return num_list
def solution(num_list):
    s = len(num_list)-1
    if num_list[s] > num_list[s-1]:
        num_list.append(num_list[s] - num_list[s-1])
    else:
        num_list.append(num_list[s] * 2)
    return num_list
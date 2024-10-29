def solution(num_list):
    num = 0
    count = 0
    for i in range(len(num_list)):
        while(1):
            if num_list[i] % 2 == 0:
                num_list[i] = num_list[i] // 2
                count += 1
            elif num_list[i] == 1:
                break
            else:
                num_list[i] = (num_list[i] -1) // 2
                count += 1
    return count
def solution(num_list):
    answer = []
    for _ in range(5):
        answer.append(min(num_list))
        num_list.remove(min(num_list))
        
    return answer
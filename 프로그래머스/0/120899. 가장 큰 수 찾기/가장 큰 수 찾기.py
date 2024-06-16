def solution(array):
    answer = []
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
        
    answer += (max, array.index(max))
    return answer
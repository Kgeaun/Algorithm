def solution(array):
    answer = 0
    array.sort()
    middle = len(array) // 2
    
    answer = array[middle]
    
    return answer
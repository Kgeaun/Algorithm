def solution(numbers):
    answer = 0
    
    answer += max(numbers)
    numbers.remove(max(numbers))
    answer *= max(numbers)
    
    return answer
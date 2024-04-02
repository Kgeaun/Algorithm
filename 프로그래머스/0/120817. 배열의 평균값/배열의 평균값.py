'''
numbers의 원소의 평균값을 return

numbers : 정수배열

1) 배열 안에 있는 수 더하기
2) 더한 값을 배열의 길이로 나누기
'''
def solution(numbers):
    r = sum(numbers)
    answer = (r/len(numbers))
    return answer
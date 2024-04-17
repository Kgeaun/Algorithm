def solution(array, height):
    answer = 0
    for i in range(len(array)):
        if array[i] > height:
            answer += 1
        elif array[i] < height:
            answer += 0
    return answer
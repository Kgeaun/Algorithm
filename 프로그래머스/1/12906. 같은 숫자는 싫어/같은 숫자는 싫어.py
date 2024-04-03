'''
return 공통 수가 제거된 후 남은 수들을 순서대로

연속해서 들어오는 것만 

arr = 배열 (숫자 0부터 9까 이루어짐)

1) answer에 먼저 arr[0]을 append

2) for문은 arr길이 만큼 돈다.
2-1 if arr[i]과 arr[i-1]이 다르면 answer에 arr[i]를 append한다.

'''
def solution(arr):
    answer = []
    
    answer.append(arr[0])
    for i in range (1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

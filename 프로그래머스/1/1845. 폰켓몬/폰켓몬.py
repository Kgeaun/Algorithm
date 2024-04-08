'''
그때의 폰켓몬 종류 번호의 개수를 return 

총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다.

종류 번호가 담긴 배열 = nums

1. hash에 숫자 넣기
2. nums와 p의 길이가 같은지 확인하기
2-1 if. 길이가 같으면 num/2
2-2 else. p/2

'''
def solution(nums):
    answer = 0
    
    p = {}
    
    for i in nums:
        p[i] = 1
    
    if len(nums)/2 < len(p):
        answer = len(nums)/2
    else:
        answer = len(p)
    
    return answer
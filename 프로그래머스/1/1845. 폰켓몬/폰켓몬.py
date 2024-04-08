'''
그때의 폰켓몬 종류 번호의 개수를 return 

총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다고 했습니다.
같은 종류의 폰켓몬은 같은 번호를 가지고 있습니다.

종류 번호가 담긴 배열 = nums

1. hash에 숫자 넣기
2. nums와 p의 길이가 같은지 확인하기
2-1 if.nums/2의 길이가 p의 길이보다 작으면 nums/2의 길이 출력(nums/2만 갖을 수 있으니까) 
-> 종류가 많아도 어차피 nums/2만 출력이 가능하니까
2-2 else. p의 길이 출력

ex | [3,1,2,3] => 2
| nums 길이 = 4
| nums/2 = 2
| 2 < 3(종류, p):
|    아무리 종류가 많아도 반 밖에 갖지 못하기 때문에 2개만 갖을 수 있음. return len(nums)/2
| 아니면:
|    종류만큼~
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

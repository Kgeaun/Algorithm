'''
완주하지 못한 선수의 이름을 return

선수들의 이름이 담긴 배열 = participant
완주한 선수들의 이름이 담긴 배열 = completion
 
1. 참여선수 이름 hash{}에 넣기
1-1 if.앞에 나온 이름과 같은 이름(동명이인)이 나오면 +1
1-2 else. 처음 나오는 이름일 경우 등록 1
2. 도착선수 이름 만큼 확인
2-1 도착선수 이름과 참여선수 이름이 같을 경우 -1
'''
def solution(participant, completion):
    
    hash = {}

    for i in participant:
        if i in hash:
            hash[i] += 1 # 동명이인이 나왔을 경우 (leo : 1 + 1)
        else:
            hash[i] = 1 #ex) 처음 나온 이름일 경우 (leo : 1)
    for i in completion:
        if hash[i] == 1: #hash 안의 값이 1이면 삭제 (1-1)
            del hash[i]
        else:
            hash[i] -= 1
    answer = list(hash.keys())[0]
    return answer
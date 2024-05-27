'''
strlist 각 원소의 길이 return

strlist = 원소 담아있는 배열
'''
def solution(strlist):
    answer = []
    for i in range(len(strlist)):
        answer.append(len(strlist[i]))
    return answer
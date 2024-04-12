'''
얻는 점수를 return

1. a, b 비교
1-1 if. a, b가 모두 홀수하면 return a^2 + b^2 
1-2 elif. a,b 중 하나만 홀수라면 return 2 × (a + b) 
1-3 else. a, b 모두 짝수라면 |a - b|

'''
def solution(a, b):
    answer = 0
    
    if a % 2 != 0 and b % 2 != 0:
        answer = (a*a) + (b*b)
    elif a % 2 != 0 or b % 2 != 0:
        answer = 2 * (a+b)
    else:
        answer = abs(a-b)
    return answer
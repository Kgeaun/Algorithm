'''
return -> 가격이 떨어지지 않은 기간은 몇 초인지 

prices : 주식 가격이 담긴 배열

1. prices를 큐에 넣는다.
2. while문에서 prices_q의 첫 번째 수를 pop하여 tmp변수에 넣는다.
3. 두 번째 for문에서 prices_q의 인덱스를 돈다.
3-1 if tmp와 j번째 값이 같거나 j번째 값이 더 크면 count를 +1한다.
3-2 elif a가 j번째 값 보다 크면 count를 안 한다.
4. for문을 나와 count 값을 answer에 넣어준다.
4-1 answer에 넣고나면 count를 다시 0으로 초기화 해준다.

'''
from collections import deque

def solution(prices):
    answer = []
    prices_q = deque(prices)

    while prices_q:
        tmp = prices_q.popleft()
        count = 0
        
        for p in prices_q:
            if tmp > p:
                count += 1
                break
            
            count += 1
        
        answer.append(count)
        
    return answer
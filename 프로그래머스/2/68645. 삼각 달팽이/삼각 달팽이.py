'''
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열 return
꼭짓점부터 반시계 방향으로 달팽이 채우기

1. 빈 2차원 배열을 만든다 ✅
2. 좌표의 패턴을 찾는다 ✅
   (첫 번째 for문 i를 n만큼 돈다) ✅
   (두 번째 for문은 첫 번째 for문 안에서 i부터 n만큼 돈다) ✅
2-1. 좌표 값에 순서개로 숫자를 저장한다 ✅
3. 배열에 저장된 숫자 순서대로 출력한다 ✅
'''
def solution(n):
    array = []
    x, y = -1, 0 
    tmp = 1
    arr = [ [0] * n for _ in range(n) ]
    
    for i in range(n):
        for j in range(i, n):
			
            if i % 3 == 0:
                x += 1
			
            elif i % 3 == 1:
                y += 1
			
            elif i % 3 == 2:
                x -= 1
                y -= 1
            
            arr[x][y] = tmp
            tmp += 1
        
    for i in range(n):
        for j in range(i+1):
            array.append(arr[i][j])
    
    return array

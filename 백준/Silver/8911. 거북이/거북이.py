T = int(input())

for _ in range(T):
    commands = input()
    
    # 북, 동, 남, 서 순서로 방향 설정
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x = 0
    y = 0
    dir = 0  # 초기 방향은 북쪽 (0)
    
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    
    for c in commands:
        if c == 'F':
            x += dx[dir]
            y += dy[dir]
        elif c == 'B':
            x -= dx[dir]
            y -= dy[dir]
        elif c == 'L':
            dir = (dir + 3) % 4  # 왼쪽 회전
        elif c == 'R':
            dir = (dir + 1) % 4  # 오른쪽 회전
        
        # 이동 후 위치 저장
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    width = max_x - min_x
    height = max_y - min_y
    print(width * height)
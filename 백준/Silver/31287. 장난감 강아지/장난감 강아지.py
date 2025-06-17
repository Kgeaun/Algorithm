# N (문자열 길이), K (반복 횟수) 입력
N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])

# 문자열 S 입력 받기
S = input()

# 현재 위치를 나타내는 변수 x, y. 시작점 = (0, 0)
x = 0
y = 0

# 문자열 S를 따라 움직이며, 중간 위치 저장할 리스트
visited = []

# 각 글자에 맞춰 좌표 이동을 계산
for i in range(N):
    if S[i] == 'U':
        y += 1
    elif S[i] == 'D':
        y -= 1
    elif S[i] == 'L':
        x -= 1
    elif S[i] == 'R':
        x += 1
    # 이동한 좌표 리스트에 저장
    visited.append([x, y])

# 최종적으로 S 한 번을 끝까지 수행했을 때 얼마나 이동했는지 계산
dx = x  # X방향 전체 이동량
dy = y  # Y방향 전체 이동량

# 방문했는지 여부
found = False

# visited에 있는 각 위치(p[0], p[1])가 반복되는 동안 원점에 도달할 수 있는지 검사
for i in range(len(visited)):
    px = visited[i][0]  # 특정 순간의 x좌표
    py = visited[i][1]  # 특정 순간의 y좌표

    # 현재 위치가 이미 원점인 경우
    if px == 0 and py == 0:
        found = True
        break

    # 반복 이동이 없으면, 처음 궤도만
    if dx == 0 and dy == 0:
        continue  # 반복해도 변화가 없으니 지금 위치만 확인

    # 반복되는 횟수를 정수 t라고 했을 때 다음 식을 만족하는 t가 있는지 검사
    # dx, dy가 모두 0이 아니면 -> (각각 나눠떨어지고, 몫이 같아야 함)
    if dx != 0 and dy != 0:
        if px % (-dx) == 0 and py % (-dy) == 0:
            tx = px // (-dx)
            ty = py // (-dy)
            if tx == ty and 0 <= tx < K:
                found = True
                break
    elif dx == 0:
        if px == 0 and py % (-dy) == 0:
            t = py // (-dy)
            if 0 <= t < K:
                found = True
                break
    elif dy == 0:
        if py == 0 and px % (-dx) == 0:
            t = px // (-dx)
            if 0 <= t < K:
                found = True
                break

if found:
    print("YES")
else:
    print("NO")
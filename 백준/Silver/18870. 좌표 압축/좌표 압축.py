n = int(input())
nums = list(map(int, input().split()))

# 중복 제거 후 정렬된 리스트 생성
sorted_unique = sorted(set(nums))

# 각 숫자에 대해 몇 번째로 작은 수인지 인덱스를 기록
coord_dict = {}
for i in range(len(sorted_unique)):
    coord_dict[sorted_unique[i]] = i

# 입력 순서대로 압축된 값 출력
for i in range(n):
    print(coord_dict[nums[i]], end=' ')
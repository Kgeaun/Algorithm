n = int(input())
end = 0
count = 0

l = [list(map(int, input().split()))for _ in range(n)]
l.sort(key=lambda x:(x[1], x[0]))

for i in l:
    if i[0] >= end:
        count += 1
        end = i[1]

print(count)
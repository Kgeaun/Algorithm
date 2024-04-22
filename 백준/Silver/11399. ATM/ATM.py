n = int(input())
p = list(map(int,input().split()))
sum = 0
tmp = 0

p.sort()

for i in range(n):
    sum += p[i]
    tmp += sum

print(tmp)
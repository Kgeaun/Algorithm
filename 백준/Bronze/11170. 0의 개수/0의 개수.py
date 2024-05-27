import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    c = 0
    m1,m2 = map(int, input().split())
    for j in range(m1, m2+1):
        a = str(j)
        c += a.count('0')

    print(c)
import sys

a, b = map(int, sys.stdin.readline().split())

n = list(map(int, input().split()))

for j in n:
    if j < b:
        print(j, end=' ')
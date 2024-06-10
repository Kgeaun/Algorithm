import sys

n = int(sys.stdin.readline())
a1 = list(map(int, input().split()))
a1.sort()

m = int(sys.stdin.readline())
a2 = list(map(int, input().split()))

for i in a2:
    start = 0
    result = False
    end = n-1
    while start <= end:
        mid = (start + end)//2
        if a1[mid] == i:
            result = True
            print(1)
            break
        elif a1[mid] < i:
            start = mid + 1
        else:
            end = mid -1
    if not result:
        print(0)
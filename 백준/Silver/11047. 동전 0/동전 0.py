n, k = map(int, input().split())

a = []

count = 0

for i in range(n):
    b = int(input())
    a.append(b)

a.sort(reverse=True)

for i in range(n):
    if a[i] <= k:
        count += k // a[i]
        k = k % a[i]

print(count)
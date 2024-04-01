import sys

a = int(sys.stdin.readline())

for _ in range(a):
    sum = sys.stdin.readline()
    stack = []
    flag = True
    for e in sum:
        if e == "(":
            stack.append(e)
        elif e == ")":
            if stack:
                stack.pop()
            else:
                flag = False
    if not flag:
        print("NO")
        continue
    else:
        if stack:
            print("NO")
        else:
            print("YES")
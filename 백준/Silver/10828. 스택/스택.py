import sys

a = int(sys.stdin.readline())

stack = []

for i in range(a):
    n1 = sys.stdin.readline().split()
    
    if n1[0] == "push":
        stack.append(n1[1])
    elif n1[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif n1[0] == "size":
        print(len(stack))
    elif n1[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif n1[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
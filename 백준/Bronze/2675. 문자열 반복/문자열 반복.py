n1 = int(input())

for i in range(n1):
    n2, string = input().split()
    
    print(''.join([i * int(n2) for i in string]))
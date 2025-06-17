a, b = 48, 18  
while b != 0:
    temp = b      
    b = a % b    
    a = temp    

T = int(input()) 

for _ in range(T):
    A, B, X = map(int, input().split())

    a = A
    b = B

    while b != 0:
        temp = b
        b = a % b
        a = temp
    print(X // a)

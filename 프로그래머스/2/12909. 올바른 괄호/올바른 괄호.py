'''
return 올바른 괄호이면 true, 올바르지 않은 괄호이면 false

1. "("이 나오면 append 
2. ")"가 나오면 pop
2-1 if. stack 안에 아무것도 없으면 true
2-2 else. false

'''
def solution(s):
    
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack == []:
                return False
            else:
                stack.pop()
        
    return stack == []
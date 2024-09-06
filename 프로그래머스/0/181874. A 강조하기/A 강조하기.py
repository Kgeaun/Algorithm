def solution(myString):
    answer = ''
    
    for char in myString:
        if char.lower() == 'a':  # 'A'도 처리하기 위해 lower() 사용
            answer += char.upper()
        else:
            answer += char.lower()
    return answer

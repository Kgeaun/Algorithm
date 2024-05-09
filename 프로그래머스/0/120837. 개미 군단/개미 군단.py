'''
최소한의 병력을 구성하려면 몇 마리의 개미 필요

장군개미 5
병정개미 3
일개미 1
'''
def solution(hp):
    
    ant = (hp//5) + (hp%5)//3 + (hp%5)%3
    
    return ant
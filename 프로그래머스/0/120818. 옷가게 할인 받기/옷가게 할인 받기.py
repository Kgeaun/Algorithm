def solution(price):
    
    if price >= 500000:
        dis = price * 0.2
        price -= dis
    elif price >= 300000:
        dis = price * 0.1
        price -= dis
    elif price >= 100000:
        dis = price * 0.05
        price -= dis
    
    return int(price)
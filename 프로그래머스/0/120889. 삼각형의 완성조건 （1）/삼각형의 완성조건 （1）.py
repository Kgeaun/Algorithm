def solution(sides):
    max1 = max(sides)
    sides.remove(max1)
    
    if (sides[0] + sides[1]) > max1:
        return(1)
    else:
        return(2)
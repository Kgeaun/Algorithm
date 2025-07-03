def solution(my_string):
    moum = ["a", "e", "i", "o", "u"]
    for m in moum:
        my_string = my_string.replace(m,"")
    return my_string
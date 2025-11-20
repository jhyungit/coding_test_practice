# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    big_n = n+1
    num = str(bin(n)[2:]).count("1")
    while True:
        if str(bin(big_n)[2:]).count("1") == num:
            break
        else:
            big_n += 1
    return big_n
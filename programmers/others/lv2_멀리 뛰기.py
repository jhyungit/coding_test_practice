# https://school.programmers.co.kr/learn/courses/30/lessons/12914
# 피보나치 이용
def solution(n):
    a, b = 1, 2
    if n == 1:
        return 1
    
    for i in range(2,n):
        a, b = b, a+b
    return b % 1234567

solution(4)
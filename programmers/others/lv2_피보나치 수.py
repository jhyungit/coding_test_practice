# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
    x = [0,1]
    
    for i in range(n):
        x.append(x[i]+x[i+1])
        
    return x[n] % 1234567
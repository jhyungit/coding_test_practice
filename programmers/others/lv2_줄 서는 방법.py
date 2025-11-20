# https://school.programmers.co.kr/learn/courses/30/lessons/12936

import math

def solution(n, k):
    answer = []
    people = [i for i in range(1,n+1)]
    
    while people:
        idx = (k-1) // math.factorial(n-1)
        answer.append(people.pop(idx))
        
        k %= math.factorial(n-1)
        n-=1

    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    data = []
    
    for order in orders:
        for cnt in course:
            if len(order) >= cnt:
                for food in combinations(order,cnt):
                    data.append(food)
    
    nor = [tuple(sorted(t)) for t in data]
    check = [0] * 11
    lst = Counter(nor)
    sort_lst = sorted(lst.items(), key=lambda x : x[1], reverse=True)
    
    for k,v in sort_lst:
        if v > 1:
            if check[len(k)] <= v:
                check[len(k)] = v
                answer.append("".join(k))
    answer.sort()
    return answer
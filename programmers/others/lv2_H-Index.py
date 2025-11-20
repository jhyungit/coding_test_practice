# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    h = len(citations)
    while h >= 0:
        gte = 0
        lte = 0
        for c in citations:
            if c >= h:
                gte += 1
            else:
                lte += 1
        
        if gte >= h and lte <= h:
            return h
        h -= 1

print(solution([3, 0, 6, 1, 5, ]))
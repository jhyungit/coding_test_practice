# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from collections import deque
from itertools import product

def solution(user_id, banned_id):
    detect_id = []
    que = deque(banned_id)

    while que:
        q = que.popleft()
        temp = []
        for user in user_id:
            check = ''
            if len(q) != len(user): # 길이가 같아야함
                continue
            for u_id,b_id in zip(user,q):
                if b_id == '*' or u_id == b_id:
                    check += u_id
                else:
                    break
            else:
                temp.append(check)
        detect_id.append(temp)
    
    detect = product(*detect_id)
    d_set = set()
    for d in detect:
        if len(set(d)) == len(banned_id):
            d_set.add(''.join(sorted(d)))
    
    return len(d_set)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["*rodo", "*rodo", "******"])
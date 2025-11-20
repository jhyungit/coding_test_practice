# https://school.programmers.co.kr/learn/courses/30/lessons/172927

from collections import deque

def solution(picks, minerals):
    answer = 0
    total_picks = sum(picks) # 곡괭이 수
    
    tired = [[1, 1, 1],
            [5, 1, 1],
            [25,5,1]]
    
    x = []
    cnt = 0
    arr = [0,0,0]
    for mineral in minerals:
        if cnt == 5:
            x.append(arr)
            cnt = 0
            arr = [0,0,0]
        if mineral == "diamond":
            arr[0] += 1
        elif mineral == "iron":
            arr[1] += 1
        else:
            arr[2] += 1
        cnt += 1
    if arr != [0,0,0]:
        x.append(arr)
    
    if total_picks < len(minerals):
        x = x[:total_picks]
    
    x.sort(key=lambda x: (-x[0],-x[1],-x[2]))
    deque_x = deque(x)
    
    pick = deque()
    for i,p in enumerate(picks):
        for _ in range(p):
            pick.append(i)
    
    while pick != deque() and deque_x != deque():
        p = pick.popleft()
        xq = deque_x.popleft()
        cur_tired = tired[p]
        for i,m in enumerate(xq):
            if m:
                answer += cur_tired[i] * m
    
    
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

from collections import deque
def solution(n):
    _sum = 0
    cnt = 0
    i = 1
    que = deque()
    while i <= n+1:
        if _sum == n:
            cnt += 1
            que.popleft()
        elif _sum < n:
            que.append(i)
            i += 1
        else:
            que.popleft()
        _sum = sum(que)
    return cnt
solution(15)
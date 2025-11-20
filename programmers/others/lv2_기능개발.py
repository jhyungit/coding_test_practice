# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
import math
def solution(progresses, speeds):
    answer = deque()
    real = []
    cnt = 0
    n = 0
    for p in progresses:
        answer.append(math.ceil((100-p)/speeds[cnt]))
        cnt+=1
        if len(answer) > 1:
            if answer[0] < answer[1]:
                answer.popleft()
                n += 1
                real.append(n)
                n = 0
            else:
                answer.popleft()
                answer.popleft()
                n += 2
    real.append(n)
    
    if answer != deque():
        real.append(1)              
    return real

solution([93, 30, 55],[1, 30, 5])
# solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
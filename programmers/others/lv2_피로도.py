# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    answer = []
    new_k = k
    
    for p in permutations(dungeons, len(dungeons)):
        k = new_k
        cnt = 0
        for x,y in p:
            if k >= x:
                k -= y
                cnt += 1
        answer.append(cnt)
    return max(answer)

solution(80, [[80,20],[50,40],[30,10]])
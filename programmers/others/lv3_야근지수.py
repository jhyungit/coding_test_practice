# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    answer = 0
    heap = []
    
    for work in works:
        heapq.heappush(heap, -work)
    
    while n:
        minimum = heapq.heappop(heap)
        if minimum:
            minimum += 1
            heapq.heappush(heap,minimum)
            n-=1
        else:
            break
    
    for h in heap:
        answer += (-h * -h)
    
    
    return answer
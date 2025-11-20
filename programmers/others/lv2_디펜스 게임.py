# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq

def solution(n, k, enemy):
    max_stage = 0
    _sum = 0
    max_heap = []
    heapq.heapify(max_heap)
    
    for e_num in enemy:
        heapq.heappush(max_heap,-e_num)
        _sum += e_num
        
        if _sum > n:
            if k == 0:
                break
            x = heapq.heappop(max_heap)
            _sum -= -x
            k-=1
        max_stage += 1

    return max_stage

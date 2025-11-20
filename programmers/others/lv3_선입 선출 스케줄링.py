# https://school.programmers.co.kr/learn/courses/30/lessons/12920

def solution(n, cores):
    
    if n <= len(cores):
        return n
    
    n -= len(cores)
    
    left, right = 1, max(cores) * n
    
    while left < right:
        mid = (left+right) // 2
        proc = 0
        for core in cores:
            proc += mid//core
            
        if proc >= n:
            right = mid
        else:
            left = mid+1
    
    for core in cores:
        n -= (right-1)//core
        
    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1
    
# 시간초과 발생
# import heapq

# def solution(n, cores):
    
#     if n <= len(cores): # 작업 수보다 코어가 더 많으면 반환
#         return n
        
#     heap = [(c,i) for i,c in enumerate(cores)] # 작업시간, 인덱스
#     heapq.heapify(heap)
    
#     n -= len(cores) # 코어 수만큼 작업 할당
    
#     while n:
#         finish_time, idx = heapq.heappop(heap)
#         finish_time += cores[idx]
#         heapq.heappush(heap,(finish_time, idx))
#         n-=1
#         if n == 0:
#             return idx + 1
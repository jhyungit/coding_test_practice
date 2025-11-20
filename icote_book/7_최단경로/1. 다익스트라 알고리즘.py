# https://school.programmers.co.kr/learn/courses/30/lessons/12978

from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    dist = {node: float('inf') for node in range(1,N+1)}
    graph = defaultdict(list)
    
    for r in road:
        s_node, e_node, length = r
        graph[s_node].append((e_node,length))
        graph[e_node].append((s_node,length))

    
    start = 1 # 1에서 시작
    # 우선순위 큐 primary queue
    pq = [(0,start)]
    dist[start] = 0 # 자기 자신까지의 거리는 0
    
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        
        if dist[cur_node] < cur_dist:
            continue
        
        for i in graph[cur_node]:
            distance = cur_dist + i[1]
            
            if distance < dist[i[0]]:
                dist[i[0]] = distance
                heapq.heappush(pq,(distance,i[0]))

    for v in dist.values():
        if v <= K:
            answer += 1
    
    return answer
    

print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4)) # 4
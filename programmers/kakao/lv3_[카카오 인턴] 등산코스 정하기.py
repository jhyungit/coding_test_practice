# 멀티 소스 다익스트라
# 모든 출입구 -> 각 지점까지 갈 수 있는 최소 intensity

import heapq

INF = float("inf")

# 출발지 -> 산봉우리 경로 중
# 경로 내 최대 간선 값의 최소 구하기  

def dijkstra(n, graph, gates, summits):
    gates_set = set(gates)
    summits_set = set(summits)

    dist = [INF] * (n+1)
    heap = []
    
    # 멀티소스 시작
    for gate in gates:
        dist[gate] = 0
        heapq.heappush(heap, (0, gate))
        
    while heap:
        intensity, u = heapq.heappop(heap)
        
        if intensity > dist[u]:
            continue
        
        # 산봉우리면 탐색 안 함
        if u in summits_set:
            continue
        
        for v, w in graph[u]:
            # 다른 출입구는 중간 방문 x
            if v in gates_set:
                continue
            
            new_intensity = max(intensity, w)
            
            if new_intensity < dist[v]:
                dist[v] = new_intensity
                heapq.heappush(heap, (new_intensity, v))
    
    return dist
    

# 지점, 등산로 정보, 출입구, 산봉우리
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    
    for u,v,w in paths:
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    dist = dijkstra(n, graph, gates, summits)
    
    summits.sort()
    answer = [0, INF]
    for summit in summits:
        if answer[1] > dist[summit]:
            answer = [summit, dist[summit]]
    
    return answer

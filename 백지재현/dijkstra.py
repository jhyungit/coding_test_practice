# 다익스트라
INF = float("inf")

import heapq

def dijkstra(graph, start, n):
    dist = [INF] * n # 0에서 모든 좌표까지 거리
    dist[start] = 0 # 자기 자신까지 거리 초기화

    heap = []
    heapq.heappush(heap, (start, 0))
    
    while heap:
        u, d = heapq.heappop(heap)

        if dist[u] < d:
            continue

        for v, w in graph[u]:
            nd = d + w
            if dist[v] > nd:
                dist[v] = nd
                heapq.heappush(heap, (v, nd))

    return dist

# 자기자신까지는 0 다른 건 거리 | 시작노드 | 노드 개수
print(dijkstra([[[1,1],[2,3]],[[0,1],[2,1]],[[1,1],[0,3]]], 0, 3))
def bellman_ford(n, edges, src):
    dist = [float('inf')]*n
    dist[src] = 0
    parent = [-1] * n
    for _ in range(n-1): # n-1번 완화 => 최단 거리는 최대 n-1개의 간선으로 이루어짐
        update = False
        for u,v,w in edges:
            if dist[u]+w < dist[v] and dist[u] != float('inf'):
                dist[v] = dist[u] + w
                parent[v] = u
                update =True
        if not update:
            break
    print(dist)
    
    # print(dist)
    
    has_neg_cycle = False
    for u,v,w in edges: # n-1번 이후, 한 번 더 갱신이 발생하면 음수 사이클!
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            has_neg_cycle = True
            break
    
    return dist, has_neg_cycle


n = 5 # 0~4까지
edges = [ # 출발, 도착, 가중치
    (0,1,6), (0,2,7),
    (1,2,8), (1,3,5), (1,4,-4),
    (2,3,-3), (2,4,9),
    (3,1,-2),
    (4,0,2), (4,3,7),
] 

print(bellman_ford(n,edges, 0))
# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque,defaultdict

def solution(n, vertex):
    dist = [0] + [float('inf')] * (n)
    start = 1
    dist[start] = 0 # 시작 좌표 초기화
    node_dict = defaultdict(list)

    for v in vertex:
        k,v = v
        node_dict[k].append(v)
        node_dict[v].append(k)
        
    que = deque([start])

    
    while que:
        start_node = que.popleft()
        
        for next_node in node_dict[start_node]:
            if dist[next_node] == float('inf'):
                dist[next_node] = dist[start_node] + 1
                que.append(next_node)
    
    return dist.count(max(dist))
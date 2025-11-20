from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        print(node, end = ' ')
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

visited = [False] * 9
bfs(graph,1,visited) # 그래프, 시작좌표, 방문여부
from collections import deque

# 노드 수, 간선 수 입력
v, e = map(int,input().split())

degree = [0] * (v+1) # 진입 차수 초기화

# 각 노드에 연결된 간선 정보
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    start, end = map(int, input().split())
    graph[start].append(end) # start->end 이동 가능
    degree[end] += 1 # end노드의 진입차수 증가

# 위상 정렬 함수
def topology_sort():
    answer = []
    
    q = deque()
    
    for i in range(1, v+1):
        if degree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        answer.append(now)
        
        for next in graph[now]:
            degree[next] -= 1 # now노드에서 진입 가능한 next노드의 진입차수 줄이기
            if degree[next] == 0:
                q.append(next) # next 노드의 진입차수가 0이면 append
                
    return answer

print(topology_sort())
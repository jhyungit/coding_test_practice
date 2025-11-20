import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 도시 개수(3), 통로 개수(2), 보내는 곳(1)
n, m, start = map(int,input().split())

graph = [[] for i in range(n+1)] # 각 노드 연결 정보 리스트 생성
distance = [INF] * (n+1) # 최단 거리 테이블 초기화

for _ in range(m):
    # x -> y, 거리
    x,y,cost = map(int,input().split())
    graph[x].append((cost,y))

pq = [(0,start)]
distance[start] = 0

while pq:
    length, cur_node = heapq.heappop(pq)
    
    if distance[cur_node] < length:
        continue
    
    for next_node in graph[cur_node]:
        weight = length + next_node[0]
        if weight < distance[next_node[1]]:
            distance[next_node[1]] = weight
            heapq.heappush(pq, (weight, next_node[1]))

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
        
print(count-1, max_distance)
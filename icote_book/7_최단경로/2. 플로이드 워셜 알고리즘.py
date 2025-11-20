INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

n,m = map(int, input().split()) # 노드, 간선 입력

graph = [[INF] * (n+1) for _ in range(n+1)]

for x in range(1,n+1):
    for y in range(1,n+1):
        if x==y:
            graph[x][y] = 0
            
for _ in range(m):
    a,b,c = map(int, input().split()) # 시작, 종료, 거리
    graph[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

for x in range(1,n+1):
    for y in range(1,n+1):
        # 도달할 수 없는 경우
        if graph[x][y] == INF:
            print('갈 수 없는 곳', end = ' ')
        else:
            print(graph[x][y], end = ' ')
    print()
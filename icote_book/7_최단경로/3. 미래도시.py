INF = int(1e9)

n,m = map(int, input().split()) # 회사 개수, 경로 개수

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신 0으로 초기화
for x in range(1,n+1):
    for y in range(1,n+1):
        if x == y:
            graph[x][y] = 0

for _ in range(m):
    start,end = map(int,input().split())
    graph[start][end] = 1
    graph[end][start] = 1

goal, date = map(int,input().split())

# 1 -> date -> goal 최소 거리 구하기

for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y],graph[x][k]+graph[k][y])

answer = graph[1][date] + graph[date][goal]

if answer >= INF:
    print('-1')
else:
    print(answer)
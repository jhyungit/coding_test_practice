n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
    
def dfs(x,y):
    # 그래프 범위를 벗어나는 경우
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드 미방문 시
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
        
    
answer = 0
for x in range(n):
    for y in range(m):
        if dfs(x,y) == True:
            answer += 1

print(answer)
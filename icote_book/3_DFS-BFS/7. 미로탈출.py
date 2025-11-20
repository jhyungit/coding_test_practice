from collections import deque
n,m = map(int,input().split())
moves = [[0,1],[0,-1],[1,0],[-1,0]]

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
    
def bfs(x,y):
    queue = deque([(x,y,1)]) # x,y, 이동 횟수(시작점 포함)
    while queue:
        x,y,cnt = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt
        
        for dx,dy in moves:
            nx,ny = x+dx, y +dy
            
            if 0<=nx< n and 0 <= ny < m and graph[nx][ny] != 0:
                queue.append((nx,ny,cnt+1))
            else:
                continue
    return cnt            
    
print(bfs(0,0))
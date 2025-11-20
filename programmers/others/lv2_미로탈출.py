# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def bfs(maps,rows,cols,directions,start,goal):
    queue = deque([(start[0],start[1],0)])
    visited = [[False]*cols for _ in range(rows)]
    
    visited[start[0]][start[1]] = True
    
    while queue:
        x,y,cnt =queue.popleft()
        
        if (x,y) == goal:
            return cnt
        
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and maps[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny,cnt+1))
    
    return -1
def solution(maps):
    rows, cols = len(maps), len(maps[0])
    directions = [(0,1),(0,-1),(-1,0),(1,0)]
    start = lebar = exit = 'None'
    
    # S,L,E좌표 구하기
    for i,m in enumerate(maps):
        if 'S' in m:
            start = (i,m.index('S'))
        if 'L' in m:
            lebar = (i,m.index('L'))
        if 'E' in m:
            exit = (i,m.index('E'))
    
    # S -> L 체크
    sl = bfs(maps,rows,cols,directions,start,lebar)
    if sl == -1:
        return -1
    
    # L -> E 체크
    le = bfs(maps,rows,cols,directions,lebar,exit)
    if le == -1:
        return -1
    
    return sl+le
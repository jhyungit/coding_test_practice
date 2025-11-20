# https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    dist = [[float("inf")] * col for _ in range(row)]
    que = deque()
    
    # 시작, 목적지 좌표 구하기
    for i,r in enumerate(board):
        for j,c in enumerate(r):
            if c == "R":
                que.append((i,j,0))
            elif c == "G":
                goal = (i,j)
    
    
    moves = [(0,-1),(0,1),(-1,0),(1,0)] # 상,하,좌,우
    
    while que:
        x,y,d = que.popleft()
        if (x,y) == goal:
            return d
        
        for dx, dy in moves:
            nx,ny = x, y
            while 0 <= nx+dx < row and 0 <= ny+dy < col and board[nx+dx][ny+dy] != "D":
                nx += dx
                ny += dy
            
            if dist[nx][ny] > d+1:
                dist[nx][ny] = d+1
                que.append((nx,ny,d+1))
        
    return -1
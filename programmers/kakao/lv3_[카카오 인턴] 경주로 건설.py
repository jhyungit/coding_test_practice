# https://school.programmers.co.kr/learn/courses/30/lessons/67259

import heapq

def solution(board):
    row, col = len(board), len(board[0])
    INF = 10**9
    goal = (row-1,col-1)
    moves = [(-1,0,0),(1,0,1),(0,-1,2),(0,1,3)] #상 하 좌 우
    cost = [[[INF] * 4 for _ in range(col)] for _ in range(row)]
    
    pq = []
    
    for i in range(4):
        cost[0][0][i] = 0 # 시작 좌표는 0
        
    if not board[0][1]:
        cost[0][1][3] = 100 # 오른쪽 이동
        heapq.heappush(pq, (100, 0, 1, 3)) # money, x, y, direction
        
    if not board[1][0]:
        cost[1][0][1] = 100 # 아래로 이동
        heapq.heappush(pq, (100, 1, 0, 1)) # money, x, y, direction
        
    
    while pq:
        money, x, y, d = heapq.heappop(pq)
        
        if money > cost[x][y][d]:
            continue
        if (x,y) == goal:
            break
        
        for dx, dy, nd in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < row and 0 <= ny < col and not board[nx][ny]: # 장애물이 없으면
                    weight = 100 if d == nd else 600
                    new_cost = money + weight
                    if new_cost < cost[nx][ny][nd]:
                        cost[nx][ny][nd] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny, nd))

    return min(cost[-1][-1])

print(solution([[0,0,0],[0,0,0],[0,0,0]])) # 900
# https://school.programmers.co.kr/learn/courses/30/lessons/84021

from collections import deque    

def rotate(block):
    cnt = 0
    rot_block = [(y,-x) for x,y in block]
    min_x = min(x for x,_ in rot_block)
    min_y = min(y for _,y in rot_block)
    norm_block = [(x-min_x,y-min_y) for x,y in rot_block] # 왼쪽 위로 땡겨주기
    norm_block.sort() # 비교 쉽게 하기 위한 정렬
    
    return norm_block
        
        
def empty_block(start_x,start_y,visited,moves,row,col):
    q = deque([(start_x,start_y)]) # 탐색 좌표
    visited[start_x][start_y] = True
    pos = [(start_x,start_y)]
    
    while q:
        x,y = q.popleft()
        
        for dx,dy in moves:
            nx,ny = x+dx, y+dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                pos.append((nx,ny))
                visited[nx][ny] = True
                q.append((nx,ny))
                
    min_x = min(x for x,_ in pos)
    min_y = min(y for _,y in pos)
    norm_pos = [(x-min_x,y-min_y) for x,y in pos] # 왼쪽 위로 땡겨주기
    norm_pos.sort() # 비교 쉽게 하기 위한 정렬
    return norm_pos

def solution(game_board, table):
    row,col = len(game_board), len(game_board[0])
    moves = [(-1,0),(1,0),(0,-1),(0,1)] # 상 하 좌 우
    empty_visited = [[False]*col for _ in range(row)]
    block_visited = [[False]*col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            if game_board[i][j] == 1:
                empty_visited[i][j] = True
            if table[i][j] == 0:
                block_visited[i][j] = True
    
    shapes = [] # 빈 공간 모양
    blocks = [] # 블럭 모양
    for i in range(row):
        for j in range(col):
            if not empty_visited[i][j]:
                shapes.append(empty_block(i,j,empty_visited,moves,row,col))
            if not block_visited[i][j]:
                blocks.append(empty_block(i,j,block_visited,moves,row,col))
        
    answer = 0
    for block in blocks:
        if block in shapes:
            shapes.remove(block)
            answer += len(block)
            continue
        
        for _ in range(3):
            block = rotate(block)
            if block in shapes:
                shapes.remove(block)
                answer += len(block)
                break
    return answer
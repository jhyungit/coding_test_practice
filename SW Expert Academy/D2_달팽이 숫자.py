# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open("coding_test_practice/SW Expert Academy/input_txt/달팽이 숫자.txt","r")

def dalpang(n):
    ans = [[0]*n for _ in range(n)]
    # right, down, left, up
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    x,y,d = 0,0,0 # 시작좌표(x,y), 방향
    
    for num in range(1,n*n+1):
        ans[x][y] = num
        
        # 다음 좌표
        nx = x + dx[d]
        ny = y + dy[d]
        
        # 범위를 벗어나거나 이미 숫자를 채웠으면 방향 전환
        if not (0<=nx<n and 0<=ny<n) or ans[nx][ny] != 0:
            d = (d+1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        
        x,y = nx, ny
    
    return ans

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    print(f"#{test_case}")
    arr = dalpang(n)
    for row in arr:
        print(" ".join(map(str,row)))
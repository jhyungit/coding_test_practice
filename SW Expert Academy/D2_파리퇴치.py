# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

import sys
sys.stdin = open("SW Expert Academy/input_txt/파리퇴치.txt","r")

def solution(flies, weapon):
    ans = set()
    row, col = len(flies), len(flies[0])
    x,y = 0,0 # 시작 좌표
    while True:
        if x == row-weapon and y == col-weapon:
            break
        nx,ny = x+weapon,y+weapon
        cnt = 0
        for i in range(x,nx):
            for j in range(y,ny):
                if i <= row and j <= col:
                    cnt += flies[i][j]
        ans.add(cnt)
        if y < col - weapon:
            y += 1
        else:
            x+=1
            y = 0

    return max(ans)

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int,input().split()) # 파리영역, 채 크기
    area = []
    for _ in range(n):
        area.append(list(map(int,input().split())))
    flies = solution(area,m)
    print(f"#{test_case} {flies}")
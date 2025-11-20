# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    game = [[False] * (n+1) for _ in range(n+1)]
    
    for win,lose in results:
        game[win][lose] = True
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if game[i][k] and game[k][j]:
                    game[i][j] = True
    
    answer = 0
    for i in range(1,n+1):
        cnt = 0
        for j in range(1,n+1):
            if game[i][j] or game[j][i]:
                cnt += 1
        if cnt == n-1:
            answer += 1
    return answer
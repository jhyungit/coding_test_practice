# https://school.programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    
    if row == 1 or col == 1:
        return max(board[0])
    
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j]:
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1])+1
    
    for x in board:
        large_x = max(x)
        if large_x > answer:
            answer = large_x
            
    return answer** 2
# https://school.programmers.co.kr/learn/courses/30/lessons/92344

# type 1공격, 2회복
# skill은 유형, 범위(row1, col1 ~ row2, col2), 내구도

def solution(board, skill):
    row = len(board)
    col = len(board[0])
    
    diff = [[0]*(col+1) for _ in range(row+1)]
    
    for s in skill:
        typp, row1, col1, row2, col2, how_many = s

        if typp == 1: # 공격
            diff[row1][col1] -= how_many
            diff[row2+1][col1] += how_many
            diff[row1][col2+1] += how_many
            diff[row2+1][col2+1] -= how_many
        else: # 회복일 때
            diff[row1][col1] += how_many
            diff[row2+1][col1] -= how_many
            diff[row1][col2+1] -= how_many
            diff[row2+1][col2+1] += how_many

    def calc_row(diff, row, col): # 행 누적합
        for r in range(row):
            for c in range(col):
                diff[r][c+1] += diff[r][c]

    def calc_col(diff, row, col): # 열 누적합
        for c in range(col):
            for r in range(row):
                diff[r+1][c] += diff[r][c]

    calc_row(diff, row, col)
    calc_col(diff, row, col)
            
    answer = 0
    for r in range(row):
        for c in range(col):
            if board[r][c] + diff[r][c] > 0:
                answer += 1
    
    return answer
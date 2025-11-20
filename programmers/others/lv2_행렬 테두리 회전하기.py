# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    arr = [[0]*columns]
    num = 1
    
    for _ in range(rows):
        temp = [0]
        for _ in range(columns):
            temp.append(num)
            num+=1
        arr.append(temp)
    
    for query in queries:
        check = []
        s_row, s_col, e_row, e_col = query
        rotate = [[0]*(columns+1) for _ in range (rows+1)]
        
        # 맨 위 회전
        for i in range(s_col,e_col):
            rotate[s_row][i+1] = arr[s_row][i]
        
        # 맨 오른쪽 회전
        for i in range(s_row,e_row):
            rotate[i+1][e_col] = arr[i][e_col]
            
        # 맨 아래 회전
        for i in range(s_col+1,e_col+1):
            rotate[e_row][i-1] = arr[e_row][i]
            
        # 맨 왼쪽 회전
        for i in range(s_row+1,e_row+1):
            rotate[i-1][s_col] = arr[i][s_col]
            
        for row,x in enumerate(rotate):
            for col,y in enumerate(x):
                if y:
                    check.append(y)
                    arr[row][col] = rotate[row][col]
        answer.append(min(check))
    
    return answer
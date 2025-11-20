def solution(n):
    answer = []
    arr = [[0] * n for i in range(n)]
    x, y = -1, 0 # 처음에는 무조건 아래 방향이므로 x는 -1로 초기화
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            # down
            if i % 3 == 0:
                x += 1
            #right
            elif i % 3 == 1:
                y += 1
            #up
            else:
                x -= 1
                y -= 1
            arr[x][y] = num
            num +=1
    
    for a in arr:
        for b in a:
            if b:
                answer.append(b)
                
    return answer
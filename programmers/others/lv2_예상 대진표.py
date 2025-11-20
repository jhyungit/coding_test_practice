# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    cnt = 0
    answer = []
    x = [0] * n
    x[a-1], x[b-1] = 1, 1
    
    while x.count(1) != 1:
        for i in range(0,n,2):
            if x[i] == 0 and x[i+1] == 0:
                answer.append(0)
            else:
                answer.append(1)
        cnt += 1
        x = answer
        n = len(x)
        answer = []
    return print(cnt)

solution(8,4,7)
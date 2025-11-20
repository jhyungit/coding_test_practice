# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def hanoi(n, start, end, temp, answer):
    if n == 1:
        answer.append([start,end])
        return
    
    # n-1개 원판을 start -> temp 이동
    hanoi(n-1, start, temp, end, answer)
    
    # 가장 큰 원판 start -> end로 이동
    answer.append([start,end])
    
    # n-1개 원판을 temp -> end 이동
    hanoi(n-1, temp, end, start, answer)
    
    

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer
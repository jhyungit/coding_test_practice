# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0
    a_idx = 0
    b_idx = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    for i in range(len(B)):
        if A[a_idx] < B[b_idx]:
            answer += 1
            a_idx += 1
            b_idx += 1
        else:
            B.pop()
            a_idx += 1
    
    return answer

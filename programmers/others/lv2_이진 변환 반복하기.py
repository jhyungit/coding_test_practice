# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = ""
    rotation = 0
    cnt_zero = 0
    
    while True:
        for i in s:
            if i == "1":
                answer += "".join(i)
            else:
                cnt_zero += 1
        s = bin(len(answer))[2:]
        answer = ""
        rotation += 1
        
        if s == "1":
            break
        
    return [rotation,cnt_zero]
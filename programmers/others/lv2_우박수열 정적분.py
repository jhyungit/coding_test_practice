# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    answer = []
    hist = {0:k}
    time = 0
    
    while k != 1:
        if k % 2 == 0: # 짝수
            k //= 2
        else:
            k = (k * 3) + 1
        time += 1
        hist[time] = k
    
    for r in ranges:
        x = r[0]
        y = time + r[1]
        area = 0
        if x > y:
            answer.append(-1)
            continue
        for i in range(x,y):
            area += (hist[i] + hist[i+1]) / 2
        answer.append(area)
    
    
    return answer
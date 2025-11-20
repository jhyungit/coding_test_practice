# https://school.programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):    
    answer = 0
    start = 1
    w_range = w * 2 + 1
    
    for station in stations:
        area = station - w - start
        if start < station-w:
            mok, remain = divmod(area,w_range)
            answer += mok
            if remain:
                answer += 1
        start = station + w + 1
    
    if start <= n:
        area = n+1 - start
        if area <= w_range:
            return answer + 1
        mok, remain = divmod(area,w_range)
        answer += mok
        if remain:
            answer += 1
    return answer

solution(16,[9],2) # 3
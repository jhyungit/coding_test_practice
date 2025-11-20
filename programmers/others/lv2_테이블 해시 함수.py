# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    answer = 0
    arr = []
    data.sort(key = lambda x : (x[col-1], -x[0]))
    
    for i in range(row_begin, row_end+1):
        _sum = 0
        for num in data[i-1]:
            _sum += (num % i)
        arr.append(_sum)
    
    for x in arr:
        answer ^= x
    return answer
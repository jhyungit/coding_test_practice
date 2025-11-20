# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    x = []
    y = []
    for i in range(len(sizes)):
        x.append(max(sizes[i]))
        y.append(min(sizes[i]))
    return print(max(x) * max(y))

solution([[60, 50], [30, 70], [60, 30], [80, 40]])
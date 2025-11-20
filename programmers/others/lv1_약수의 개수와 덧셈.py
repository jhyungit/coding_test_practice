# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def f(left, right):
    new = [i for i in range(left, right+1)]
    x = []
    answer = 0
    for i in range(left, right+1):
        little = []
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                little.append(j)
        if len(little) % 2 == 0:
            x.append(1)
        else:
            x.append(-1)
    for i in range(right - left + 1):
        answer +=  new[i] * x[i]
    return print(answer)

left = 13
right = 17
f(left, right)
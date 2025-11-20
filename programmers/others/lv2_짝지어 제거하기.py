# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    x = []
    for i in s:
        x.append(i)
        if len(x) >=2:
            if x[-2] == x[-1]:
                x.pop()
                x.pop()
            else:
                pass
    return 1 if x == [] else 0

solution("baabaa")
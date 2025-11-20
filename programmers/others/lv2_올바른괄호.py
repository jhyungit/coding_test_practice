# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    x = []
    for i in s:
        if i == "(":
            x.append(i)
        else:
            if x == []:
                return False
            else:
                x.pop()
    return x == []
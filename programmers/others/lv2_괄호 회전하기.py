# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    x = list(s)
    
    for _ in range(len(s)):
        temp = []
        for j in range(len(s)):
            if len(temp) > 0:
                if temp[-1] == '(' and x[j] == ')':
                    temp.pop()
                elif temp[-1] == '{' and x[j] == '}':
                    temp.pop()
                elif temp[-1] == '[' and x[j] == ']':
                    temp.pop()
                else:
                    temp.append(x[j])
            else:
                temp.append(x[j])
        if len(temp) == 0:
            answer += 1
        x.append(x.pop(0))
    return answer

solution("[](){}")
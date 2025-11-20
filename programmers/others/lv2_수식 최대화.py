# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import operator

answer = set()
arr = set(['+','-','*'])
op_map = {"+" : operator.add,
         "-" : operator.sub,
         "*" : operator.mul}

def calc(priority,expression):
    num = []
    susik = []
    temp = ""
    
    for express in expression:
        if express not in arr:
            temp += express
        else:
            num.append(int(temp))
            temp = ""
            susik.append(express)
    num.append(int(temp))

    for p in priority:
        idx = 0
        while idx < len(susik):
            if susik[idx] == p: # 수식이 같으면
                x = num.pop(idx)
                y = num.pop(idx)
                num.insert(idx, op_map[p](x,y))
                susik.pop(idx)
            else:
                idx += 1
    if num[0] < 0:
        answer.add(-num[0])
    else:
        answer.add(num[0])

def solution(expression):
    
    # +, -, * 세 개의 연산자 우선순위
    for priority in permutations(arr,3):
        calc(priority, expression)
    
    
    return max(answer)

solution("100-200*300-500+20")
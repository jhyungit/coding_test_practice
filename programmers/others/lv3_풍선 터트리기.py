# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    x = [a[0]]
    y = [a[-1]]
    
    for num in a[1:]: # 왼쪽부터 최소
        if x[-1] > num:
            x.append(num)
        else:
            x.append(x[-1])
    
    for num in a[len(a)-2::-1]:
        if y[-1] > num:
            y.append(num)
        else:
            y.append(y[-1])
    new_y = y[::-1] # 오른쪽부터 최소

    answer = set(x + new_y) # 중복 제거
    return len(answer)
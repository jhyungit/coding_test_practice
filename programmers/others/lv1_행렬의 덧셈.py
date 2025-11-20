# https://school.programmers.co.kr/learn/courses/30/lessons/12950

def li_add(a, b):
    answer = [[]]
    sum = 0

    for i in range(len(a)-1):
        answer.append([])

    for i in range(len(a)):
        for j in range(len(a[i])):
            sum = a[i][j] + b[i][j]
            answer[i].append(sum)
    return print(answer)

a = [[1,2],[2,3]]
b = [[3,4],[5,6]]
li_add(a,b)

######## numpy 활용
# a = [[1,2],[2,3]]
# b = [[3,4],[5,6]]
# import numpy as np
# A = np.array(a)
# B = np.array(b)
# C = A + B
# C.tolist()
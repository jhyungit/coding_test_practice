# https://school.programmers.co.kr/learn/courses/30/lessons/12949

import numpy as np
def solution(arr1, arr2):
    answer = []
    x = np.matmul(arr1,arr2)
    for i in range(len(x)):
        answer.append([int(x) for x in list(x[i])])
    return answer
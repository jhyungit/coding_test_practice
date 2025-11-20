# https://school.programmers.co.kr/learn/courses/30/lessons/12982

# 물품 지원! 예산 정해져 있음
# 목표 : 최대한 많은 부서에게 물품 구매할 수 있도록 함
# 금액은 정확히 지불 (적은 금액 지원 불가)
#  최대 몇 개의 부서에 물품을 지원할 수 있는지 return

def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if budget >= d[i]:
            answer += 1
            budget -= d[i]
        else:
            break
    return print(answer)

solution([2,2,3,3], 10)
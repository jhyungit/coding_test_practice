# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open("coding_test_practice/SW Expert Academy/input_txt/햄버거 다이어트.txt","r")
# 테스트 케이스 수
# 재료수, 제한 칼로리
# 점수 칼로리

# 조건1) 제한 칼로리 이하
# 조건2) 점수 최대

def solution(score_cal, dp):
    for k in range(1, len(dp)):
        k_cal, k_worth = score_cal[k-1]
        for limit_cal in range(len(dp[0])):
            if k_cal <= limit_cal:
                dp[k][limit_cal] = max(dp[k-1][limit_cal], k_worth + dp[k-1][limit_cal-k_cal])
            else:
                dp[k][limit_cal] = dp[k][limit_cal-1]

    return dp[-1][-1]


T = int(input())
for test_case in range(1, T + 1):
    ingre_num, limit_cal =  map(int,input().split()) # 재료 5개 제한:1000cal
    score_cal = []
    for _ in range(ingre_num):
        score, cal = map(int,input().split())
        score_cal.append([cal,score])
    score_cal.sort(key=lambda x: x[1]) # 칼로리 오름차순, 점수 내림차순
    dp = [[0] * (limit_cal+1) for _ in range(ingre_num+1)]
    print(f"#{test_case} {solution(score_cal, dp)}")
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

import sys
sys.stdin = open("SW Expert Academy/input_txt/백만 장자 프로젝트.txt","r")

def solution(price):
    max_price = price[-1]
    income = 0
    
    for p in price[::-1]:
        if max_price > p:
            gap = max_price - p
            income += gap
            continue
        else:
            max_price = p
        
    return income


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    price = list(map(int,input().split()))
    ans = solution(price)
    
    print(f"#{test_case} {ans}")
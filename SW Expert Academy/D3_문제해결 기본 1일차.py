# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open("coding_test_practice/SW Expert Academy/input_txt/1일차.txt","r")

def solution(n, building):
    house = 0
    
    for i in range(2, n-2):
        cur_floor = building[i]
        if any(building>=cur_floor for building in building[i-2:i]):
            continue
        elif any(building >= cur_floor for building in building[i+1:i+3]):
            continue
        else:
            other_floor = max(building[i-2:i]+building[i+1:i+3])
            house += (cur_floor-other_floor)
    
    return house
        

for i in range(1,11):
    n = int(input()) # 빌딩 수
    arr = list(map(int,input().split()))
    print(f"#{i} {solution(n,arr)}")
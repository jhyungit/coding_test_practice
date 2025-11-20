# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZmeHlF68SDHBIPN

import sys
sys.stdin = open("SW Expert Academy/input_txt/유치원생은 쉽게 푸는 문제.txt","r")

space = [1,0,0,0,1,0,1,0,2,1]
num = [i for i in range(0,10)]
space_num_dict = {k:v for k,v in zip(num,space)}

T = int(input())
arr = []

for test_case in range(1, T + 1):
    answer = ''
    x = int(input())
    if x == 1:
        print(0)
        continue
    mok,remain= divmod(x,2)

    if remain == 0: # 짝수일 때
        answer = '8' * mok
    else: # 홀수일 때
        answer = '4' + '8' * mok
    
    print(int(answer))
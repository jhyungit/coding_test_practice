# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq

import sys
sys.stdin = open("SW Expert Academy/input_txt/홀수만 더하기.txt","r")

T = int(input())
arr = []

for i in range(1,T+1):
	total = 0
	for num in (list(map(int,input().split()))):
		if num % 2 == 1:
			total += num
	print(f"#{i} {total}")
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD

import sys
sys.stdin = open("coding_test_practice/SW Expert Academy/input_txt/최대상금.txt","r")

T = int(input())

def solution(num_str,cnt):
    num_list = list(num_str)
    
    # visited[k]: 교환 k번 남은 상태에서 이미 나온 숫자들
    visited = [set() for _ in range(cnt+1)]
    
    max_val = 0
    
    def dfs(cur_list,k):
        nonlocal max_val
        
        s = ''.join(cur_list)
        
        if s in visited[k]:
            return
        visited[k].add(s)
        
        if k == 0:
            max_val = max(max_val, int(s))
            return
        
        n = len(cur_list)
        for i in range(n-1):
            for j in range(i+1,n):
                cur_list[i],cur_list[j] = cur_list[j],cur_list[i]
                dfs(cur_list,k-1)
                cur_list[i],cur_list[j] = cur_list[j],cur_list[i]
    
    dfs(num_list,cnt)
    return max_val
    
for test_case in range(1, T + 1):
    num, cnt = input().split()
    cnt = int(cnt)
    ans = solution(num,cnt)
    print(f"#{test_case} {ans}")
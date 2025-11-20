# https://school.programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    answer = 0
    length = len(sticker)
    if length < 3:
        return max(sticker)
    
    dp0 = [0] + sticker[:-1] # 0번 선택 0 ~ length-1까지
    for i in range(2,length):
        dp0[i] = max(dp0[i] + dp0[i-2], dp0[i-1])
    
    dp1 = [0] + sticker[1:] # 1번 선택 1 ~ length까지
    for i in range(2,length):
        dp1[i] = max(dp1[i] + dp1[i-2], dp1[i-1])
    
    return max(dp0[-1],dp1[-1])
    
solution([14, 6, 5, 11, 3, 9, 2, 10])
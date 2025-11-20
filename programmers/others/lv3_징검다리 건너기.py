# https://school.programmers.co.kr/learn/courses/30/lessons/64062

# 슬라이딩 윈도우 풀이
from collections import deque

def solution(stones, k):
    deque_window = deque()  # 현재 윈도우에서 최댓값을 관리하는 덱
    answer = float('inf')  # 최종 결과 (최솟값 저장)

    for i in range(len(stones)):
        # 1️⃣ 덱에서 윈도우 범위를 벗어난 인덱스를 제거
        if deque_window and deque_window[0] < i - k + 1:
            deque_window.popleft()
        
        # 2️⃣ 덱에서 stones[i]보다 작은 값을 제거 (필요 없는 값이므로)
        while deque_window and stones[deque_window[-1]] <= stones[i]:
            deque_window.pop()
        
        # 3️⃣ 현재 인덱스를 덱에 추가
        deque_window.append(i)

        # 4️⃣ 슬라이딩 윈도우가 k 크기에 도달했을 때 최댓값 갱신
        if i >= k - 1:
            answer = min(answer, stones[deque_window[0]])  # 현재 윈도우에서 최댓값 찾기

    return answer



# 이진 탐색 풀이
# def solution(stones, k):
#     left,right = 0, max(stones)
    
#     while left <= right:
#         mid = (left + right) // 2
#         possible = True
#         jump = 0
        
#         for stone in stones:
#             if stone - mid <= 0:
#                 jump += 1
#                 if jump >= k:
#                     possible = False
#                     break
#             else:
#                  jump = 0
        
#         if possible:
#             left = mid + 1
#         else:
#             right = mid -1
            
#     return left
        
        
solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	, 3)
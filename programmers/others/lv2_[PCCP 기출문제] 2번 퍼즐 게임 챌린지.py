# https://school.programmers.co.kr/learn/courses/30/lessons/340212

#     diff        time_cur       time_prev
# 현재 퍼즐 난이도   현재 퍼즐 소요 시간  이전 퍼즐 소요시간

def solution(diffs, times, limit):
    result = set()
    left, right = 1, max(diffs)
    
    while left <= right:
        answer = 0
        mid = (left + right) // 2
        
        for i, diff in enumerate(diffs):
            if mid >= diff:
                answer += times[i]
            else:
                cnt = diff - mid
                if i != 0:
                    answer += (times[i] + times[i-1]) * cnt + times[i]
        if answer <= limit:
            result.add(mid)
            right = mid - 1
            
        else:
            left = mid + 1
    
    return min(result)



#  아래 코드도 가능
# def solution(diffs, times, limit):
#     left, right = 1, max(diffs)
#     answer = 0
    
#     while left <= right:
#         total = 0
#         mid = (left + right) // 2
        
#         for i, diff in enumerate(diffs):
#             if mid >= diff:
#                 total += times[i]
#             else:
#                 cnt = diff - mid
#                 if i != 0:
#                     total += (times[i] + times[i-1]) * cnt + times[i]
#         if total <= limit:
#             answer = mid
#             right = mid - 1
#         else:
#             left = mid + 1
    
#     return answer
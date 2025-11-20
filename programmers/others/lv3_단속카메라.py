# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    minimum = -30001
    routes.sort(key = lambda x:x[1])
    
    for route in routes:
        if minimum < route[0]:
            minimum = route[1]
            answer += 1
    return answer


# def solution(routes):
#     answer = 0
#     routes.sort(key = lambda x:x[1])
#     camera = -float('inf')
    
#     for route in routes:
#         if route[1]> camera:
#             answer += 1
#             camera = route[1]
#     return answer
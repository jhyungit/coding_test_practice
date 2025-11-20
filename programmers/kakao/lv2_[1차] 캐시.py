# https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return 5 * len(cities)
    
    upper_cities = []
    for c in cities:
        upper_cities.append(c.upper())
    
    x = deque([])
    for c in upper_cities:
        if c in x:
            answer += 1
            x.remove(c)
            x.append(c)
        else:
            if len(x) == cacheSize:
                x.popleft()
            answer += 5
            x.append(c)
    return answer

# # 아래와 같이 deque에 maxlen을 이용하면 더욱 간단한 코딩이 가능
# from collections import deque
# def solution(cacheSize, cities):
#     answer = 0
#     x = deque(maxlen=cacheSize)
    
#     for c in cities:
#         big_c = c.upper()
#         if big_c in x:
#             x.remove(big_c)
#             x.append(big_c)
#             answer += 1
#         else:
#             x.append(big_c)
#             answer += 5
#     return answer
# def solution(n, words):
#     d = set()
#     answer = [0, 0]
#     last = ""

#     for i, w in enumerate(words):
#         if d:
#             if w in d or w[0] != last:
#                 answer[1] = i
#                 break
#         d.add(w)
#         last = w[-1]
    
#     if answer[1]:
#         answer[0] = answer[1] % n + 1
#         answer[1] = answer[1] // n + 1
    
#     return answer
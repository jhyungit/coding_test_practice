# https://school.programmers.co.kr/learn/courses/30/lessons/42578

# 내가 푼 것
def solution(clothes):
    dict_clothes = dict(clothes)
    new_dict = {}
    x = 1
    
    for c in dict_clothes.values():
        if c in new_dict:
            new_dict[c] += 1
        else:
            new_dict[c] = 1
    
    for i in range(len(new_dict)):
        x *= (list(new_dict.values())[i]+1)
        
    return x-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	)

# def solution(clothes):
    
# #강사님 푼 것
#     clothes_dict = {}
    
#     for name, category in clothes:
#         if category in clothes_dict:
#             clothes_dict[category].append(name)
#         else:
#             clothes_dict[category] = [name]
#     # 2) 각 카테고리별로 몇 종류의 구체적인 의상이 있는지 --> 계산
#     # 과거에 수학적인 부분집합 계산 그 방식 (사용한다, 안 한다)
#     # 단순 계산
    
#     answer = 1
#     for k, v in clothes_dict.items():
#         answer *= (len(v)+1)
#     answer -= 1 
# # 모든 항목에서 사용 안 한 경우 제외.
    
#     return answer
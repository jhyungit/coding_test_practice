# https://school.programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict

def solution(gems):
    gem_cnt = defaultdict(int)
    n = len(set(gems))
    min_len = float('inf')
    start = 0
    
    for end in range(len(gems)):
        gem_cnt[gems[end]] += 1
        
        while len(gem_cnt) == n: # 같으면 슬라이딩 +1
            if end - start + 1 < min_len:
                min_len = end - start + 1
                answer = [start+1,end+1]

            gem_cnt[gems[start]] -= 1
            if gem_cnt[gems[start]] == 0:
                del gem_cnt[gems[start]]
            start += 1
            
    return answer

# solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "EMERALD", "SAPPHIRE", "RUBY"]) # [8,11]
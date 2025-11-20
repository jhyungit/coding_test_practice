# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):

    if target not in set(words):
        return 0
    
    que = deque([(begin,0)])
    check = set()
    
    while que:
        q, cnt = que.popleft()

        if q == target:
            return cnt

        for word in words:
            diff_count = sum(1 for x,y in zip(q,word) if x != y) # 다른 글자 수 확인
            if diff_count == 1: # 글자 한 개만 변경 가능
                if word not in check:
                    check.add(word)
                    que.append((word,cnt+1))
    return 0

print(solution("AAAA", "AABB", ["AABA", "AABB"])) # 2
print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"])) # 4
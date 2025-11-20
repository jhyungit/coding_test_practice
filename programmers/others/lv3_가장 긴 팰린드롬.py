# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    n = len(s)
    if n < 2:
        return n

    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1  # 마지막으로 같던 구간의 길이

    best = 1
    for i in range(n):
        # 홀수 중심
        best = max(best, expand(i, i))
        # 짝수 중심
        if i + 1 < n and s[i] == s[i+1]:
            best = max(best, expand(i, i+1))

    return best

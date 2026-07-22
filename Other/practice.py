def solution(w, h, start, waypoints):
    INF = float("inf")
    n = len(waypoints) # 경유지 개수

    def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # 거리 미리 계산 (장애물 없으니 맨해튼) ← 이게 통째로 빠져 있었음
    from_start = [manhattan(start, waypoints[i]) for i in range(n)]
    dist = [[manhattan(waypoints[i], waypoints[j]) for j in range(n)] for i in range(n)]
    
    # dp[mask][i] 경유지, 현재 위치
    dp = [[INF] * n for _ in range(1 << n)]

       # 3. 기저 ← 이게 빠져서 inf 나왔음
    for i in range(n):
        dp[1 << i][i] = from_start[i]

    for mask in range(1<<n): # 어떤 상태 mask에서
        for i in range(n): # 위치 i에서 
            if dp[mask][i] == INF or not (mask & (1<<i)): # i가 방문 안 한 곳이면
                continue 
            for j in range(n): # 아직 안 간 j로
                if mask & (1<<j):
                    continue
                nmask = mask | (1 << j) # j를 추가한 새 집합
                cost = dp[mask][i] + dist[i][j] # i -> j 가는 비용
                if cost < dp[nmask][j]: # 더 작으면
                    dp[nmask][j] = cost        
        
    full = (1 << n) - 1
    return min(dp[full][i] for i in range(n))

print(solution(5, 5, (1,1), [(2,2), (1,4), (5,1)])) # 10

# 1. 상태: dp[mask][i] = ?  (말로 한 문장 쓰기)
# 2. 배열 선언: dp = [[INF]*n for _ in range(1<<n)]
# 3. 기저: 계산 없이 아는 값 채우기 (보통 1<<i 짜리)
# 4. 전이: 명사(mask, i, j) 개수만큼 루프. 안전장치 2개 챙기기
# 5. 답: full = (1<<n)-1, min 또는 특정 칸
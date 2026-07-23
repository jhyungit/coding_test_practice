def manhattan(x,y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def solution(w, h, start, waypoints):
    INF = float("inf")
    n = len(waypoints)
    from_start, dist = [], []

    for i in range(n):
        from_start.append(manhattan(start, waypoints[i]))
        temp = []
        for j in range(n):
            temp.append(manhattan(waypoints[i], waypoints[j]))
        dist.append(temp)
    
    # dp[mask][i] 경유지, 현재 위치 (말로 한 문장 쓰기)
    dp = [[INF] * n for _ in range(1 << n)]

    # 3. 기저: 계산 없이 아는 값 채우기 (보통 1<<i 짜리)
    for i in range(n):
        dp[1 << i][i] = from_start[i]
    
    for mask in range(1 << n): # 어떤 상태 mask에서
        for i in range(n): # 위치 i에서
            # 방문 체크
            if dp[mask][i] == INF or not (mask & (1 << i)): # i가 실제로 방문한 곳이어야함
                continue

            for j in range(n):
                if mask & (1<<j): # 아직 안 간 j로
                    continue
                nmask = mask | (1 << j) # j를 추가한 새 집합
                cost = dp[mask][i] + dist[i][j] # i -> j 가는 비용
                if cost < dp[nmask][j]: # 더 작으면
                    dp[nmask][j] = cost

    full = (1 << n) - 1
    return min(dp[full])

print(solution(5, 5, (1,1), [(2,2), (1,4), (5,1)])) # 10
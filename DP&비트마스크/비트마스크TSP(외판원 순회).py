# [Lv.3] 외판원 순회
# 0번부터 (N−1)번까지 번호가 붙은 N개의 도시가 있습니다. 한 외판원이 한 도시에서 출발하여 N개의 모든 도시를 정확히 한 번씩 방문한 뒤, 다시 출발한 도시로 돌아오는 여행 경로를 외판원 순회라고 합니다.
# 도시 간 이동 비용이 2차원 배열 W로 주어집니다. W[i][j]는 도시 i에서 도시 j로 갈 때 드는 비용입니다. 단, 방향에 따라 비용이 다를 수 있어 W[i][j]와 W[j][i]가 다를 수 있으며, W[i][j]가 0이면 i에서 j로 가는 길이 아예 없다는 뜻입니다 (자기 자신 W[i][i]는 항상 0).
# 도시의 수 n과 이동 비용 배열 W가 매개변수로 주어질 때, 모든 도시를 순회하는 데 드는 최소 비용을 return 하도록 solution 함수를 완성해 주세요. 어느 도시에서 출발하든 순회 비용은 같으므로 출발 도시는 자유롭게 정하면 됩니다. 입력은 항상 순회가 가능한 경우만 주어집니다.

# 제한사항
# 2 ≤ n ≤ 16
# W는 n × n 크기의 2차원 정수 배열
# W[i][i] = 0
# 이동 가능한 경우 1 ≤ W[i][j] ≤ 1,000,000
# 이동 불가능한 경우 W[i][j] = 0
# 항상 하나 이상의 유효한 순회가 존재함
        

def solution(n, W):
    INF = float("inf")
    
    # dp[mask][i] (방문한곳, 현재 위치)
    dp = [[INF] * n for _ in range(1<<n)]

    # 기저
    dp[1<<0][0] = 0
    
    # dp[n비트개][n개]이므로 제일 밖은 n비트개 반복: 즉 어떤 상태 mask에서
    for mask in range(1<<n):
        # 현재 서 있는곳
        for i in range(n):
            # i가 실제로 방문한 곳이어야함
            if dp[mask][i] == INF or not ((1<<i) & mask):
                continue

            # 다음곳 체크
            for j in range(n):
                # 이미 방문한 곳이면
                if mask & (1<<j) or W[i][j] == 0:
                    continue
                cost = dp[mask][i] + W[i][j]
                nmask = mask | (1<<j)
                if cost < dp[nmask][j]:
                    dp[nmask][j] = cost

    answer = INF
    full = (1 << n) - 1
    for i in range(n):
        if W[i][0] == 0:
            continue
        answer = min(answer, dp[full][i] + W[i][0])
    
    return answer


# 테스트 1: 기본 예제
print(solution(4, [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0],
]))  # 기대값 35

# 테스트 2: 갈 수 없는 경로(0) 포함
print(solution(4, [
    [0, 10, 0, 20],
    [0, 0, 9, 0],
    [6, 0, 0, 12],
    [8, 8, 0, 0],
]))  # 기대값 39

# 테스트 3: 최소 크기 N=2
print(solution(2, [
    [0, 5],
    [7, 0],
]))  # 기대값 12
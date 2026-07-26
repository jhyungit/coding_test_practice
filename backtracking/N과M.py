# N과 M: 순열 만들기(1~N까지, 길이 M의 순열)
def solution(N,M):
    answer = []
    selected = []
    visited = [False] * (N + 1)

    def backtrack():
        # 종료 조건
        if len(selected) == M:
            answer.append(selected[:])
            return

        # 1~N까지
        for num in range(1,N+1):
            # 가지치기
            if visited[num]:
                continue

            # 선택 표시
            visited[num] = True
            selected.append(num)

            # 다음 자리 채우러 깊이 들어감
            backtrack()

            # 원복
            selected.pop()
            visited[num] = False

    backtrack()

    return answer


print(solution(3,2))
# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
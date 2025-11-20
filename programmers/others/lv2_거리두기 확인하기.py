# https://school.programmers.co.kr/learn/courses/30/lessons/81302

def is_valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] != 'P':
                continue

            # 상하좌우 거리 1
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = i + dx, j + dy
                if is_valid(nx, ny) and place[nx][ny] == 'P':
                    return 0

            # 대각선 방향
            for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                nx, ny = i + dx, j + dy
                if is_valid(nx, ny) and place[nx][ny] == 'P':
                    # 사이에 하나라도 빈 테이블이면 위반
                    if place[i][ny] == 'O' or place[nx][j] == 'O':
                        return 0

            # 상하좌우 거리 2
            for dx, dy in [(-2,0), (2,0), (0,-2), (0,2)]:
                nx, ny = i + dx, j + dy
                mx, my = i + dx // 2, j + dy // 2  # 중간 지점
                if is_valid(nx, ny) and place[nx][ny] == 'P':
                    if place[mx][my] == 'O':
                        return 0

    return 1

def solution(places):
    return [check(place) for place in places]
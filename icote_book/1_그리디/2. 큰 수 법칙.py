# n, m, k
# m 번 더하여 가장 큰 수
# k 번 연속해서 못 더함

n,m,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort(reverse=True)

answer = 0
first,second = l[0],l[1]

while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0:
            break
        answer += first
        m -= 1
    if m == 0:
        break
    answer += second
    m -= 1

print(answer)
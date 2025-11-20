n = int(input())
food = list(map(int,input().split()))
d = [0] * 100

for i in range(n):
    if i == 0:
        d[i] = food[i]
    elif i == 1:
        d[i] = max(food[i-1], food[i])
    else:
        d[i] = max(d[i-1], d[i-2]+food[i])

print(d[n-1])
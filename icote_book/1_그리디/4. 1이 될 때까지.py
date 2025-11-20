# n, k
# 1 빼거나, K로 나누거나

n,k = map(int,input().split())
cnt = 0

while True:
    target = (n // k) * k
    cnt += (n - target)
    n = target
    
    if n < k:
        break
    cnt += 1
    n //= k
    
print(cnt-1)
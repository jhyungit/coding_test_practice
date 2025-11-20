# n 행, m 열

n, m = map(int,input().split())
result = []

for i in range(n):
    result.append(min(map(int,input().split()))) 

print(result)
print(max(result))
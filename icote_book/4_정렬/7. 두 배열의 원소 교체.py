n,k = map(int, input().split())
arr = []

for _ in range(2):
    arr.append(list(map(int,input().split())))

a,b = arr[0], arr[1]

a.sort()
b.sort(reverse = True)

for i in range(k):
    a[i] = b[i]

print(sum(a))
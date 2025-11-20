def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 개수, 간선 수
n,v = map(int,input().split())

parent = [0] * (n+1) # 부모 테이블 초기화

for i in range(1, n+1):
    parent[i] = i # 부모 노드 자기 자신으로 초기화

# union 연산 각각 수행
for _ in range(v):
    start, end = map(int, input().split())
    union_parent(parent, start, end)

# 각 원소가 속한 집합 만들기
for i in range(1, n+1):
    find_parent(parent, i)

print(parent)

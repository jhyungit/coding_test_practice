from collections import Counter

def find_parent(parent,x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a,b, parent):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v,e =6,4 # 노드 수, 간선 수
graph = [(1,4),(2,3),(2,4),(5,6)]

parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

for i in range(e):
    a,b = graph[i]
    union_parent(a,b, parent) 
print(parent)
node = []
for i in range(1,v+1):
    node.append(find_parent(parent,i))
    
answer = Counter(node)
print(len(answer))
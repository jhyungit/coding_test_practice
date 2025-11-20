# 팀 번호 0~n번, 연산 개수
n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def find_parnet(parent, x): # 1 같은 팀 여부 확인
    if parent[x] != x:
        parent[x] = find_parnet(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b): # 0 팀 합치기
    a = find_parnet(parent,a)
    b = find_parnet(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
answer = []
for _ in range(m):
    want, a, b = map(int,input().split())
    
    if want: # 1일 때(같은 팀 여부 확인)
        if find_parnet(parent,b) == find_parnet(parent,a):
            answer.append('YES')
        else:
            answer.append('NO')
    else:
        union_parent(parent,a,b)

for say in answer:
    print(say)
    
# 입력
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

# 출력
# No
# No
# YES
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import defaultdict,Counter

def find_parent(x,parent):
    if x != parent[x]:
        return find_parent(parent[x],parent)
    return x

def union_parent(a,b,parent):
    a = find_parent(a,parent)
    b = find_parent(b,parent)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    parent = [0] * (n)
    for i in range(n):
        parent[i] = i
    
    node = defaultdict(list)
    
    
    for key, computer in enumerate(computers):
        for i,c in enumerate(computer):
            if key != i and c:
                node[key].append(i)
    
    for a in range(n):
        for b in node[a]:
            union_parent(a,b,parent)
    answer = []
    for i in range(n):
        answer.append(find_parent(i,parent))
    
    answer = Counter(answer)
    
    return len(answer)


# from collections import deque

# def solution(n, computers):
#     answer = 0
#     visited = [0] * n
    
#     def bfs(start):
#         visited[start] = 1
#         que = deque([start])
        
#         while que:
#             cur = que.popleft()
            
#             for next in range(n):
#                 if computers[cur][next] == 1 and not visited[next]:
#                     visited[next] = 1
#                     que.append(next)
    
#     for i in range(n):
#         if not visited[i]:
#             bfs(i)
#             answer += 1
#     return answer
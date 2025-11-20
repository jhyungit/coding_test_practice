# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import deque,defaultdict

def solution(tickets):
    depth = len(tickets) + 1
    
    for ticket in tickets:
        ticket.append(False)
    
    tickets.sort(key = lambda x : x[1])
    way = ['ICN']
    
    def dfs(airport):
        for ticket in tickets:
            start, end, visited = ticket
            
            if start == airport and not visited:
                way.append(end)
                ticket[2] = True # 방문 처리
                
                if depth == len(way) or dfs(ticket[1]):
                    return way
                
                ticket[2] = False # 탐색했는데, 경로가 다 안 찼으면
                way.pop()
                
    answer = dfs('ICN')
    
    return answer

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
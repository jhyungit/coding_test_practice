# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    alive = [False] * len(operations)  # i번째 삽입이 살아있는지
    
    for i, oper in enumerate(operations):
        op, num = oper.split()
        num = int(num)
        
        if op == "I":
            # 같은 값을 두 힙에 모두 넣음. 인덱스 i로 연결.
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            alive[i] = True
        
        elif num == 1:  # D 1: 최댓값 삭제
            # 이미 죽은 top은 청소
            while max_heap and not alive[max_heap[0][1]]:
                heapq.heappop(max_heap)
            # 살아있는 top을 꺼내서 죽임
            if max_heap:
                _, idx = heapq.heappop(max_heap)
                alive[idx] = False
        
        else:  # D -1: 최솟값 삭제
            while min_heap and not alive[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                _, idx = heapq.heappop(min_heap)
                alive[idx] = False
    
    # 최종 결과 뽑기 전, top들 청소
    while max_heap and not alive[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not alive[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if not max_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]
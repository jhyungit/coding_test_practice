from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque()
    sec = deque()
    w = deque(truck_weights)
    
    while True:
        if truck == deque():
            truck.append(w.popleft())
            sec.append(1)
            answer += 1
        
        if w != deque() and (sum(truck) + w[0]) <= weight and len(truck) < bridge_length:
            truck.append(w.popleft())
            sec = deque(map(lambda x : x+1, sec))
            sec.append(1)
            answer += 1
        else:
            while sec[0] != bridge_length:
                sec = deque(map(lambda x : x+1, sec))
                answer +=1
            sec.popleft()
            truck.popleft()
        
        if w == deque() and truck == deque():
            answer += 1
            break
    
    return answer
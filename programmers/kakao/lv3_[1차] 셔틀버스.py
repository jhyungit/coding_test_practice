# https://school.programmers.co.kr/learn/courses/30/lessons/17678

# 셔틀 9시부터
# n횟수, t분, m최대인원, 크루별 대기열
from collections import deque

def solution(n, t, m, timetable):
    first_bus = 540
    bus_schedule = deque()
    
    for _ in range(n): # 분으로 계산
        if bus_schedule == deque(): # 첫차
            bus_schedule.append(first_bus)
            continue
        first_bus += t
        bus_schedule.append(first_bus)
    
    waiting_line = []
    for t_table in timetable:
        t_h,t_m = map(int, t_table.split(":"))
        total = (t_h * 60) + t_m
        waiting_line.append(total)
    
    waiting_line.sort()
    waiting_line = deque(waiting_line)
    
    while bus_schedule:
        bus = bus_schedule.popleft()
        cnt = 0
        last = None
            
        for _ in range(m):
            if waiting_line != deque() and waiting_line[0] <= bus:
                last = waiting_line.popleft()
                cnt += 1
    
    def time_to_str(minutes):
        hour,minute = divmod(int(minutes),60)
        return f"{hour:02d}:{minute:02d}"
    
    if cnt < m:
        return time_to_str(bus)
    else:
        if last <= bus:
            return time_to_str(last-1)
        else:
            return time_to_str(bus)
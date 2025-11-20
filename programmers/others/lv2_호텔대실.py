# https://school.programmers.co.kr/learn/courses/30/lessons/155651

from collections import deque
def solution(book_time):
    answer = 0
    book = []
    
    for b in book_time:
        start, end = b
        s_h,s_m = map(int,start.split(":"))
        e_h,e_m = map(int,end.split(":"))
        book.append([(s_h * 60 + s_m), (e_h * 60 + e_m+10)]) # 청소 10분 추가

    book.sort()
    room = []
    que = deque(book)
    room.append([que.popleft()[1]])
    
    while que:
        q = que.popleft()
        for i,ro in enumerate(room):
            for r in ro:
                if r <= q[0]:
                    room[i].append(q[1])
                else:
                    room.append([q[1]])
            break
    print(len(room))
            
    return answer

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
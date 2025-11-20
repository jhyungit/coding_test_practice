# https://school.programmers.co.kr/learn/courses/30/lessons/77486

# 조건1) 추천인한테 10%배분 나머지 자기가 가짐
# 조건2) 원단위 절사. floor또는 int변환

# 이름, 추천인, 판매자, 판매개수
# enroll 순서대로 리턴

def solution(enroll, referral, seller, amount):
    answer = []
    name_dict = {k:[[],0] for k in enroll} # 인당 수익금 초기화
    
    for child, parent in zip(enroll,referral):
        name_dict[child][0] = parent
            
    for s, cnt in zip(seller, amount):
        money = cnt * 100
        while s != '-' and money > 0:
            p_money = money // 10 # 추천인이 받을 돈
            name_dict[s][1] += (money - p_money) # 판 사람이 갖는 돈
            if money == 0:
                break
            s = name_dict[s][0] # 추천인 이름
            money = p_money
    
    for worker in enroll:
        answer.append(name_dict[worker][1])
    return answer
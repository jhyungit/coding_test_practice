# scores = [근무 태도 점수, 동료 평가 점수]
# if 임의 사원 보다 둘 다 낮은 경우
# else 두 점수 합 석차, rank

def solution(scores):
    n = len(scores)
    
    # 완호 점수
    wanho_a, wanho_b = scores[0][0], scores[0][1]
    
    # 스코어 정렬(a 내림차순, b 오름차순)
    sort_score = scores.copy()
    sort_score.sort(key = lambda x : (-x[0],x[1]))
    
    max_b = float('-inf')
    
    # 완호의 인센티브 여부 체크
    for a, b in sort_score: 
        if wanho_a < a and wanho_b < b: # 완호가 인센티브 받지 못할 경우
            return -1
        if wanho_a >= a: # 완호가 인센티브 받는 경우
            break
    
    max_a = sort_score[0][0]
    rank_score = []
    for a,b in sort_score:
        if max_b <= b:
            max_b = b
        else:
            if max_a != a: # 지배 당함
                continue
            else:
                max_a = a
        rank_score.append([a,max_b])
    
    answer = []
    for rk in rank_score:        
        answer.append((rk, rk[0]+rk[1]))

    answer.sort(key=lambda x: -x[1])
    
    score = answer[0][1]
    weight = 0 # 동점 순위 체크
    rank = 1 # 시작 순위
    
    for r in answer:
        ab, point = r
        
        if score == point: # 동점자 카운트
            weight += 1
        else: # 이후 순위
            score = point
            rank += weight
            weight = 1
            
        if ab == [wanho_a, wanho_b]:
            return rank
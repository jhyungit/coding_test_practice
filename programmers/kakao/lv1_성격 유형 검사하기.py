# # https://school.programmers.co.kr/learn/courses/30/lessons/118666

# # choices	뜻
# # 1	매우 비동의 3
# # 2	비동의 2
# # 3	약간 비동의 1
# # 4	모르겠음 0
# # 5	약간 동의 1
# # 6	동의 2
# # 7	매우 동의 3

# 지표 번호	성격 유형
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

def solution(survey, choices):
    answer = ''
    typ = {"R" : 0, "T" : 0,
            "C" : 0, "F" : 0,
            "J" : 0, "M" : 0,
            "A" : 0, "N" : 0}
    score = {1 : 3, 2 : 2, 3 : 1,
                4 : 0,
            5 : 1, 6: 2, 7 : 3}
    cnt = 0

    for s in survey:
        if choices[cnt] < 4 :
            typ[s[0]] += score[choices[cnt]]
            cnt += 1
        elif choices[cnt] == 4:
            pass
            cnt += 1
        else:
            typ[s[1]] += score[choices[cnt]]
            cnt += 1

    # typ 는 {'R': 0, 'T': 3, 'C': 1, 'F': 0, 'J': 0, 'M': 2, 'A': 1, 'N': 1}

    k = list(typ)
    v = list(typ.values())

    for i in range(0,len(v), 2):
        if v[i] > v[i+1]:
            answer += k[i]
        elif v[i] == v[i+1]:
            answer += min(k[i], k[i+1])
        else:
            answer += k[i+1]
        if i+2 == len(v):
            break

    return answer


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]) # TCMA
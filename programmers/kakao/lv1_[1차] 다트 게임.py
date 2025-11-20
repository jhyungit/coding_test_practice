# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    score = set(i for i in range(11))
    area = {'S' : 1, 'D': 2, 'T' : 3}
    new = []
    cnt = 0
    num = 0

    for s in dartResult:
        if s in str(score):
            if num != 0:
                num = (int(str(num) + s))
                continue
            num = int(s)
        else:
            if s == "S":
                new.append(pow(num, area[s]))
                cnt += 1
            elif s == "D":
                new.append(pow(num, area[s]))
                cnt += 1
            elif s == "T":
                new.append(pow(num, area[s]))
                cnt += 1
            elif s == "*":
                if cnt == 1:
                    new[-1] = new[-1] * 2
                else:
                    new[-1], new[-2] = (new[-1] * 2), (new[-2] * 2)
            elif s == "#":
                new[-1] = -new[-1]
            num = 0

    return print(sum(new))

# 10처리 시 .replace('10', 'K') 와 같은 것 이용 가능

# solution("1S2D*3T") # 37
# solution("1D2S#10S") # 9
# solution("1D2S0T") # 3
# solution("1S*2T*3S") # 23
# solution("1D#2S*3S") # 5
# solution("1T2D3D#") # -4
# solution("1D2S3T*") # 59
# solution("10D2S1S") # 103
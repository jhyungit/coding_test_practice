# 00시 00분 00초 ~ n시 59분 59초
# 3 포함 시각 수

n = int(input())
h, s, m = 0, 0, 0
answer = 0

while True:
    if n + 1 == h:
        break
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    
    temp = str(h) + str(m) + str(s)
    if "3" in temp:
        answer += 1
        
print(answer)
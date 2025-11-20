# 수평 2 수직 1, 수직 2 수평 1
# 8 X 8 

position = list(input())
d = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
now = [int(position[1])-1, d[position[0]]]
result = 0

# 수평 +2
if now[1] + 2 <= 7:
    if now[0] + 1 <= 7:
        result += 1
    if now[0] - 1 >= 0:
        result += 1
# 수평 -2
if now[1] - 2 >= 0:
    if now[0] + 1 <= 7:
        result += 1
    if now[0] - 1 >= 0:
        result += 1
# 수직 +2
if now[0] - 2 >= 0:
    if now[1] + 1 <= 7:
        result += 1
    if now[1] - 1 >= 0:
        result += 1
# 수직 -2
if now[0] + 2 <= 7:
    if now[1] + 1 <= 7:
        result += 1
    if now[1] - 1 >= 0:
        result += 1

print(result)
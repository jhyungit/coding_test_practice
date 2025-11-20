# github 연습
# run 단축키 : ctrl + option + n
# https://school.programmers.co.kr/learn/courses/30/lessons/12917

def string_sorting(s):
    low = []
    up = []
    new_s = ''
    for i in s:
        if i.islower() == True:
            low.append(i)
        else:
            up.append(i)
    low.sort(reverse = True)
    up.sort(reverse = True)

    for i in low:
        new_s += i
    for  j in up:
        new_s +=j
    return print(new_s)

s = 'ZBcSDds'
string_sorting(s)


# 다른사람 풀이
# ''.join(sorted(s, reverse=True))
# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ""
    
    num = set(str(i) for i in range(10))
    s_num = {"zero" : 0,"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5,
                "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    new_s = ""
    for i in s:
        if i in num:
            if new_s in s_num:
                answer += str(s_num[new_s])
                new_s = ""
            answer += i
        else:
            if new_s in s_num:
                answer += str(s_num[new_s])
                new_s = ""
            new_s += i
    if new_s in s_num:
        answer += str(s_num[new_s])
    return print(int(answer))

solution("one4seveneight")
# solution("23four5six7")
# solution("one4seveneight")
# solution("one4seveneight")
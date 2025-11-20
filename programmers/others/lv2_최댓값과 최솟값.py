# https://school.programmers.co.kr/learn/courses/30/lessons/12939

# map 메소드 활용가능!
# s = list(map(int, s.split()))

# s	return
# "1 2 3 4"	"1 4"
# "-1 -2 -3 -4"	"-4 -1"
# "-1 -1"	"-1 -1"

def solution(s):
    answer = ''
    s = s.split(" ")
    new = []

    for i in s:
        new.append(int(i)) 

    sort_new = sorted(new)

    if int(sort_new[0]) < int(sort_new[-1]):
        answer += str(sort_new[0]) + " " + str(sort_new[-1])
    else:
        answer += str(sort_new[-1]) + " " + str(sort_new[0])
        
    return print(answer)

# solution("1 2 3 4")
# solution("-1 -2 -3 -4")
# solution("-1 -1")
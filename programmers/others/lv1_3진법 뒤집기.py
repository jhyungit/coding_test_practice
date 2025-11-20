# https://school.programmers.co.kr/learn/courses/30/lessons/68935

# divmob() 활용 가능
# 두 숫자를 인자로 전달 받아 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 tuple 형식으로 반환한다.  

def solution(n):
    x = []
    mok = n // 3
    x.append(n % 3)
    while mok >= 3:
        x.append(mok % 3)
        mok = mok // 3
    if mok == 0 :
        pass
    else:
        x.append(mok)
    x.reverse()
    sum = 0
    for i in range(len(x)):
        sum += x[i] * pow(3, i)
    return sum

solution(45)


# 다른 사람 풀이 int(x, y) --> y진법 x를 10진법으로

# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3)
#     return answer

# solution(45)
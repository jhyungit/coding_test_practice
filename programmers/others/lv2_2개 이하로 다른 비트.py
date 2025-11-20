# https://school.programmers.co.kr/learn/courses/30/lessons/77885?language=python3

def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0: # 짝수
            answer.append(int(str(int(bin(num)[2:]) + 1), 2))
        else: # 홀수
            s = list('0' + bin(num)[2:])
            idx = ''.join(s).rfind('0')
            s[idx], s[idx+1] = '1', '0'
            answer.append(int(''.join(s), 2))

    return answer
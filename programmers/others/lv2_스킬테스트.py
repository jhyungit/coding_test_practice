# # 1번 문제
# def solution(A,B):
#     answer = 0
#     A.sort()
#     B.sort(reverse=True)
#     for i in range(len(A)):
#         answer += A[i] * B[i]

#     return answer

# 2번 문제
def solution(s):
    result = []
    for i in range(1, len(s)+1):
        x = ""
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, len(s)+i, i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    x += str(cnt) + tmp
                else:
                    x += tmp
                tmp = s[j:j+i]
                cnt = 1
        result.append(len(x))
        
    return print(min(result))

solution("aabbaccc")
# "aabbaccc" 7
# "ababcdcdababcdcd" 9
# "abcabcdede" 8
# "abcabcabcabcdededededede" 14
# "xababcdcdababcdcd" 17
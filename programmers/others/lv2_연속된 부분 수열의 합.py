# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = [0, len(sequence)]
    l, r = 0 , 0
    plus = sequence[0]
    
    while True:
        if plus < k:
            r += 1
            if r == len(sequence):
                break
            plus += sequence[r]
        else:
            if plus == k:
                if r - l < answer[1] - answer[0]:
                    answer = [l, r]
            plus -= sequence[l]
            l += 1
        print(l,r)
    return answer

solution([1, 2, 3, 4, 5], 7)
solution([1, 1, 1, 2, 3, 4, 5], 5)
solution([2, 2, 2, 2, 2], 6)
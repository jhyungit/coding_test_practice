# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    li = []
    b_li = []
    blank = 0
    
    for a in s.split():
        answer += a[0].upper()
        answer += a[1:].lower()
        li.append(answer)
        answer = ''

    for b in s:
        if b == ' ':
            blank += 1
        else:
            if blank != 0:
                b_li.append(blank)
            blank = 0
    b_li.append(blank)
            
    cnt = 0
    for i in li:
        if len(li)-1 != cnt:
            answer += i + (' ' * b_li[cnt])
        else:
            answer += i + (' ' * b_li[cnt])
        cnt += 1

    return print(len(answer))

# solution("3people unFollowed me") # "3people Unfollowed Me"
solution("qwed    ")
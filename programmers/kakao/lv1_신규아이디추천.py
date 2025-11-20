# https://school.programmers.co.kr/learn/courses/30/lessons/72410

# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다. 0
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다. 0
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다. 0
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다. 0
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다. 0
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.0
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.0
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

import re

def solution(new_id):
    special = "-_.~!@#$%^&*()=+[{]}:?,<>/"
    
    new_id = new_id.lower() # 1단계

    for s in special:
        if s not in "-_.":
            new_id = new_id.replace(s, "") # 2단계

    new_id = re.sub(r'\.+', '.', new_id) # 3단계

    # 4-1, 4-2 한 번에 가능한 방법 정규식 활용
    # new_id = re.sub('^[.]|[.]$', '', new_id)
    if len(new_id) != 0 and new_id[0] == ".":
        new_id = new_id[1:] # 4-1단계
    
    if len(new_id) != 0 and new_id[-1] == ".":
        new_id = new_id[:-1] # 4-2단계

    if new_id == "":
        new_id += "a" # 5단계

    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1] # 6단계

    while len(new_id) < 3:
        new_id += new_id[-1]

    return print(new_id)

solution("...!@BaT#*..y.abcdefghijklm") # bat.y.abcdefghi
# solution("z-+.^.") # z--
# solution("=.=") # aaa
# solution("123_.def") # 123_.def
# solution("abcdefghijklmn.p") # abcdefghijklmn
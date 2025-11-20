# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def get_dis(number, pos):
    key_pos = {
        "1" : (0,0),"2" : (0,1),"3" : (0,2),
        "4" : (1,0),"5" : (1,1),"6" : (1,2),
        "7" : (2,0),"8" : (2,1),"9" : (2,2),
        "*" : (3,0),"0" : (3,1),"#" : (3,2),
    }

    number = str(number)
    pos = str(pos)

    x_number, y_number = key_pos[number]
    x_pos, y_pos = key_pos[pos]

    return abs(x_number-x_pos) + abs(y_number-y_pos)

def solution(numbers, hand):
    answer = ''
    left_pos = "*"
    right_pos = "#"

    if hand == "right":
        hand = "R"
    elif hand=="left":
        hand = "L"

    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left_pos = str(num)
        elif num in [3, 6, 9]:
            answer += "R"
            right_pos = str(num)
        elif num in [2, 5, 8, 0]:
            dis_left = get_dis(num, left_pos)
            dis_right = get_dis(num, right_pos)
            if dis_left == dis_right:
                answer += hand
                if hand == "L":
                    left_pos = str(num)
                elif hand == "R":
                    right_pos = str(num)
            elif dis_left > dis_right:
                answer +="R"
                right_pos = str(num)
            elif dis_left < dis_right:
                answer +="L"
                left_pos = str(num)
            else:pass 
        else:pass                        
    return print(answer)

# solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
# solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def money_gap(price, money, count):

    sum = 0
    for i in range(1, count+1):
        sum += price * i
    if money < sum :
        return print(f"모자란 돈 : {sum - money}")
    else:
        return print(0)
money_gap(3, 20, 4)
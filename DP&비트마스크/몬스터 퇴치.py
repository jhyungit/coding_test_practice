def solution(monsters):
    monsters.sort()
    pos, neg = [], []

    for monster in monsters:
        if monster > 0: # 양수면
            pos.append(monster)
        else: # 음수면
            neg.append(monster)
    neg.reverse()

    sort_monsters = pos + neg
    cur, need = 0, 1
    for monster in sort_monsters:
        if monster > 0:
            need = max(need, monster - cur)
            cur += monster
        else:
            cur += monster
            need = max(need, 1 - cur)

    return need

print(solution([-1,-2,-6,-14]))
print(solution([1,2,6,14]))
print(solution([-3,10,2,-6]))


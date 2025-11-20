def solution(bandage, health, attacks):
    sec = 1
    success = 0
    max_time = attacks[-1][0]
    max_hp = health
    attack_dict = {}
    
    for a in attacks:
        attack_dict[a[0]] = a[1]
    
    while sec <= max_time:
        if sec in attack_dict:
            health -= attack_dict[sec]
            success = 0
            
            if health <= 0:
                return -1
            
        else:
            success += 1
            if success == bandage[0]:
                health += bandage[1] + bandage[2]
                if health > max_hp:
                    health = max_hp
                success = 0
            else:
                health += bandage[1]
                if health > max_hp:
                    health = max_hp
        sec += 1
        
    return health
    
print(solution([5,1,5],30,[[2, 10], [9, 15], [10, 5], [11, 5]]))
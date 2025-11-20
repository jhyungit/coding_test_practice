# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    fail_dict = {}
    num_people = len(stages)

    for stage in range(1, N+1):
        fail_num = stages.count(stage)
        if num_people > 0:
            fail_dict[stage] = fail_num / num_people
        else:
            fail_dict[stage] = 0
        num_people -= fail_num
        
    fail_list = sorted(fail_dict.items(), key = lambda x : x[1], reverse= True)
    answer = [ info[0] for info in fail_list]

    return print(answer)

# solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4,4,4,4,4])
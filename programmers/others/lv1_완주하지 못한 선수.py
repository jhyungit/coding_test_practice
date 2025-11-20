# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    people_dict = {}
    x = 0
    
    for p in participant:
        if p in people_dict:
            people_dict[p] += 1
        else:
            people_dict[p] = 1
    
    for p in completion:
        if people_dict[p] == 1:
            del people_dict[p]
        else:
            people_dict[p] -= 1
            
    answer = list(people_dict.keys())[0]
    return print(answer)

# solution(["leo", "kiki", "eden"],["eden", "kiki"])
# solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"]	,["stanko", "ana", "mislav"])
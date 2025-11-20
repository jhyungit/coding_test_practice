from collections import defaultdict

def solution(genres, plays):
    answer = []
    g_dict = defaultdict(int)
    r_dict = defaultdict(list)
    idx = 0
    
    for genre,play in zip(genres,plays):
        g_dict[genre] += play
        r_dict[genre].append((play,idx))
        idx += 1

    g_rank = sorted(g_dict.items(),key=lambda x: x[1], reverse = True)
    
    for g in g_rank:
        new = r_dict[g[0]]
        new = sorted(new, key=lambda x : (-x[0],x[1]))
        if len(new) == 1:
            answer.append(new[0][1])
        else:
            answer.append(new[0][1])
            answer.append(new[1][1])

    return answer

# from collections import defaultdict

# def solution(genres, plays):
#     answer = []
#     i = 0
#     g_dict = defaultdict(list)
#     n_dict = defaultdict(int)
    
#     if len(plays) == 1:
#         return [0]
    
#     for g, p in zip(genres, plays):
#         g_dict[g] += [[i,p]]
#         n_dict[g] += p
#         i+=1
    
#     n_dict = sorted(n_dict.items(), key = lambda x:x[1], reverse = True)
    
#     for n in n_dict:
#         new = g_dict[n[0]]
#         new = sorted(new,key=lambda x : (-x[1], x[0]))
#         if len(new) == 1:
#             answer.append(new[0][0])
#         else:
#             answer.append(new[0][0])
#             answer.append(new[1][0])
        
    
#     return answer
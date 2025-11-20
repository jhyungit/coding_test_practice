# https://school.programmers.co.kr/learn/courses/30/lessons/12906

answer = []
arr = [1,1,3,3,0,1,1]
for i in range(len(arr)):
    answer.append(arr[i])
    for j in range(len(arr)):
        if answer[i] != arr[j]:
            answer.append(arr[j])
            i += 1
    break
print(answer)
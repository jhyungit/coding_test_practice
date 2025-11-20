# # https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    x = []
    y = []

    for i in range(n):
        x.append(list(str(format(arr1[i], 'b'))))
        y.append(list(str(format(arr2[i], 'b'))))

        if len(x[i]) < n:
            while len(x[i]) != n:
                x[i].insert(0, 0)
        if len(y[i]) < n:
            while len(y[i]) != n:
                y[i].insert(0, 0)

    
    map = []
    for i in range(n):
        for j in range(n):
            if int(x[i][j]) + int(y[i][j]) != 0:
                map.append(1)
            else:
                map.append(0)
    
    real_map = ''
    for i in range(len(map)):
        if map[i] == 1:
            real_map += '#'
        else:
            real_map += ' '

    answer = []
    start_pos = 0
    end_pos = len(map)
    for i in range(start_pos, end_pos+n, n):
        out = map[start_pos:start_pos + n]
        if out != []:
            answer.append(real_map[start_pos:start_pos + n])
        start_pos += n
    return answer

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])
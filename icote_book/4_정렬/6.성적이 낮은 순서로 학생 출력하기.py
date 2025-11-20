n = int(input())
student = dict()

for _ in range(n):
    k,v = input().split()
    v = int(v)
    student[k] = v
    
x = sorted(student.items(), key = lambda x : x[1])

for name, score in x:
    print(name, end = ' ')
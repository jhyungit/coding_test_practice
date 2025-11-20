n = 1260
count = 0

coin = [500,100,50,10]

for c in coin:
    count += n // c
    n %= c

print(count)
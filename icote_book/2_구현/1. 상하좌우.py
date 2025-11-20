n = int(input())
moves = list(input().split())
direction = {"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]} # L R U D
x, y = 1, 1

for move in moves:
    dx, dy = direction[move]
    nx, ny = x + dx, y + dy
    if 0 < nx <= n and 0 < ny <= 5:
        x,y = nx,ny
        
print(x,y)
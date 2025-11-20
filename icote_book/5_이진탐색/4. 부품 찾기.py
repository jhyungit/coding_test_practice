def binary_search(array,target,left,right):
    while left <= right:
        mid = (left+right)//2
        
        if array[mid] == target:
            return print('yes')
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return print('no')

n = int(input())
have = list(map(int,input().split()))
m = int(input())
asked = list(map(int,input().split()))

have.sort()

for target in asked:
    binary_search(have, target, 0, len(have)-1)
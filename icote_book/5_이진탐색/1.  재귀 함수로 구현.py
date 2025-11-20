def binary_search(array, target, left, right):
    if left > right:
        return None
    
    mid = (left+right)//2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target, left,mid-1)
    else:
        return binary_search(array,target,mid+1,right)

array = [1,3,5,7,9,11,13,15,17,19]

target = int(input())
answer = binary_search(array, target, 0, len(array)-1)

if answer == None:
    print('존재하지 않는 숫자')
else:
    print(f'{answer+1}번 째에 위치')
def binary_search(array, target, left, right):
    while left <= right:
        mid = (left+right) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid]< target:
            left = mid+1
        else:
            right = mid-1
    return None

array = [1,3,5,7,9,11,13,15,17,19]
target = int(input())

x = binary_search(array, target, 0, len(array)-1)
if x == None:
    print('존재하지 않는 숫자')
else:
    print(f'{x+1}번 째에 위치')
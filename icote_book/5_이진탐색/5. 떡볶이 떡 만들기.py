def binary_search(array, target, bottom, top):
    while bottom <= top:
        total = 0
        mid = (bottom+top) // 2
        total = sum((x - mid) for x in array if x > mid)
        
        if total < target: # 떡이 짧으면 더 많이 자르기
            top = mid - 1
        else: # 떡이 길면 덜 자르기
            answer = mid # 최대한 덜 자른 게 정답이므로, 꾸준히 갱신
            bottom = mid + 1
            
    return answer

n,m = map(int,input().split())
array = list(map(int,input().split()))

answer = 0
bottom = 0
top = max(array)
target = m

x = binary_search(array,target,bottom,top)
print(x)
# 재귀함수: 자기 자신을 다시 호출하는 함수
# DFS/BFS 구현을 위해 보통 사용

def recursive_function(i):
    if i == 10:
        print('재귀 함수를 종료합니다...')
        return
    print(f'{i}번 째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    
recursive_function(1)

# 팩토리얼 재귀함수 구현
def factorial_func(i):
    if i <= 1:
        return 1
    return i * factorial_func(i-1)
    
print(factorial_func(5))
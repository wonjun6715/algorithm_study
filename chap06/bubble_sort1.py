# 버블 정렬 알고리즘 구현하기

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1): # n -1개의 원소의 정렬이 끝나면 마지막 원소는 이미 끝에 놓이게 됨
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1] # 패스
                
if __name__ == "__main__":
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    bubble_sort(x)
    
    print('오른차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
    
        



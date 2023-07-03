# 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬(오름차순)"""
    n = len(a)
    for i in range(1, n): # 범위가 1 ~ n-1인 이유는 단순 삽입 정렬은 0번째 인덱스는 이미 정렬이 되어 있다고 가정하기 때문
        tmp = a[i] # 정렬되지 않은 값 중 인덱스가 가장 작은 원소의 값
        j = i # 정렬되지 않은 값 중 가장 작은 원소의 인덱스
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('단순 삽입 정렬을 수행합니다.') 
    num = int(input('원소 수를 입력하세요.: '))
    
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
        
    insertion_sort(x)
    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')       
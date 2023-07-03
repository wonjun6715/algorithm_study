# 이진 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        key = a[i] # 정렬하려는 원소 값
        pl = 0 # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1 # 검색 범위의 맨 끝 원소 인덱스
        
        while True:
            pc = (pl + pr) // 2
            if a[pc] == key: # 종료 조건
                break
            elif a[pc] < key:
                pl = pc + 1
            elif a[pc] > key:
                pr = pc -1
            if pl > pr: # 종료 조건, 검색 범위가 더 이상 없는 경우
                break
            
        #pd = pc + 1 if pl <= pr else pr + 1 # 삽입해야 할 위치의 인덱스
        if pl <= pr:
            pd = pc + 1
        else:
            pd = pr + 1
        
        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

if __name__ == '__main__':
    print('이진 삽입 정렬을 수행합니다.') 
    num = int(input('원소 수를 입력하세요.: '))
    
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
        
    binary_insertion_sort(x)
    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')     
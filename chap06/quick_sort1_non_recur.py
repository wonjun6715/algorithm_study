# 비재귀적인 퀵 정렬 구현하기

from stack import Stack
from typing import MutableSequence

def qsort(a : MutableSequence, left : int, right : int) -> None:
    """a[left] ~ a[right]를 퀵 정렬(비재귀적인 정렬)"""
    range = Stack(right - left + 1) # 스택 생성
     
    range.push((left, right)) # 바깥쪽 () 연산자는 push 함수 호출, 안쪽 () 연산자는 left와 right를 튜플로 만들기 위해 결합하는 연산자
     
    while not range.is_empty():
        pl, pr = left, right = range.pop() # 왼쪽, 오른쪽 커서를 꺼냄
        x = a[(left + right) // 2] # 피벗(가운데 원소)

        while pl <= pr:
            while a[pl] < x:
                pl += 1
            while a[pr] > x:
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
                         
        if left < pr:
            range.push((left, pr)) # 왼쪽 그룹의 커서를 저장
        if pl < right:
            range.push((pl, right)) # 오른쪽 그룹의 커서를 저장
        
def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)
    
if __name__ == "__main__":
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num # 원소 수가 num인 배열을 생성
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
        
    quick_sort(x) # 배열 x를 퀵 정렬
    
    print('오름차순으로 정렬했습니다.')
    
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
      
    
    
    
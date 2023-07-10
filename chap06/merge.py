# 정렬을 마친 두 배열을 병합하기

from typing import Sequence, MutableSequence

def merge_sorted_list(a: MutableSequence, b: Sequence, c: MutableSequence) -> None:
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0 # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c) # 각 배열의 원소 수 
    
    while pa < na and pb < nb: # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1
    
    while pa < na: # pb는 len(b)까지 갔지만, pa가 가지 못한 경우 a에 남은 원소를 c에 복사 => pa가 배열 a의 맨 끝에 도달하지 않은 경우 실행
        c[pc] = a[pa]
        pa += 1
        pc += 1
    
    while pb < nb: # pa는 len(a)까지 갔지만, pb가 가지 못한 경우 b에 남은 원소를 c에 복사 => pb가 배열 b의 맨 끝에 도달하지 않은 경우 실행
        c[pc] = b[pb]
        pb += 1
        pc += 1
        
if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + (len(b)))
    print('정렬을 마친 두 배열의 병합을 수행합니다.')
    
    merge_sorted_list(a, b, c) # 배열 a와 b를 병합하여 c에 저장
    
    print('배열 a와 b를 병합하여 배열 c에 저장했습니다.')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'배열 c: {c}')
    
    
    
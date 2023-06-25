# 이진 검색 알고리즘

from typing import Sequence, Any

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1
    
    while True:
        pc = (pl + pr) // 2 # 중앙 원소의 인덱스
        
        if a[pc] == key: # 검색 성공한 경우
            return pc
        elif a[pc] < key: # 검색 범위를 뒤쪽 절반으로 좁힘
            pl = pc + 1
        else:
            pr = pc - 1 # 검색 범위를 앞쪽 절반으로 좁힘
        if pl > pr:
            break
    return -1 # 검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    
    print('배열 데이터를 오름차순으로 입력하세요.')
    x = [None] * num
    
    x[0] = int(input('x[0]: ')) # 무조건 원소가 하나는 있어야 함
    
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] > x[i - 1]:
                break
            
    ky = int(input('검색할 값을 입력하세요.: '))
    
    idx = bin_search(x, ky)
    
    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
        
        
    
    
            
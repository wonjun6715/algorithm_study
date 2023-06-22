# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any: # Any는 제약이 없는 임의의 자료형, Sequence는 시퀀스형을 의미(list형, byte형, 문자열형, 튜플형 등)
    """시퀀스형 a 원소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
            
    return maximum

if __name__ == '__main__': # 메인 함수의 선언, 시작을 의미, 현재 스크립트 파일이 실행되는 상태를 파악하기 위해 사용
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num # 원소 수가 num인 리스트를 생성
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))
        
    print(f'최댓값은 {max_of(x)}입니다.')    
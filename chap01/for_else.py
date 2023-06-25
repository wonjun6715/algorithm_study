# 10~99 사이의 난수 n개 생성하기(13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요: '))
for i in range(n):
    r = random.randint(10,99)
    print(r, end = ' ')
    
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else:  # for-else문 
    print('\n난수 생성을 종료합니다.') # 스위트 : break 문이 실행되지 않았을 때만 실행됨
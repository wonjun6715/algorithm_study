# 2자리 양수 (10~99 입력받기)

print('2자리 양수를 입력하세요.')
while True:
    n = int(input('값을 입력하세요.: '))
    if n >= 10 and n <= 99:
        break
    
print(f'입력받은 양수는 {n}입니다.')
        
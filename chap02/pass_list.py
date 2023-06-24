# 인수의 형이 뮤터블(리스트)인 경우에서 임의의 원솟값을 업데이트

def change(lst, idx, val):
    """lst[idx]의 값을 val로 업데이트"""
    lst[idx] = val
    
x = [11, 22, 33, 44, 55]
print(f'x = {x}')

index = int(input('업데이트할 인덱스를 선택하세요: '))
value = int(input('새로운 값을 입력하세요.: '))

change(x, index, value) # list는 뮤터블 객체이기 때문에 Call by Reference 방식으로 메모리 주소 자체를 넘기므로 값이 변함
print(f'x = {x}')
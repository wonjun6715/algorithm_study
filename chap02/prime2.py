# 1부터 1000이하의 소수를 구할 때 지금까지 구한 소수를 배열에 저장하여 개선

counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr+=1

for n in range(3, 1001, 2): # 홀수만을 대상으로 설정
    for i in range(1, ptr): # 이미 찾은 소수로 나눔
        counter+=1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr+=1
            
for i in range(ptr):
    print(prime[i])
    
print(f'나눗셈을 실행한 횟수: {counter}') 
print()

'''
for 반복문

for 변수 in range() : 
    수행해야할 문장 1
'''

# range() : 숫자 리스트를 자동으로 만들어 주는 함수
list = range(10)
print(list)  # 0 부터 10 미만의 정수를 자동으로 생성

# 시작, 끝 숫자를 지정하려면 콤마로 구분
list = range(1, 11)
print(list)

# 끝 숫자가 미만임에 유의
for i in range(1, 11):
    print('for 반복문', i)

print('-----------------------------------------')

for i in range(1, 10):
    print(i, '번째', '3 *', i, '=', (3*i))

print('-----------------------------------------')

# 사용자로부터 숫자 하나 입력받아서 해당 구구단 출력 - 5단
value = int(input('몇단?'))

for i in range(1, 10):
    print(value, '*', i, '=', (value*i))
















































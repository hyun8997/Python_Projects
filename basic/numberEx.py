name = 'Python'  #문자 따옴표로 초기화
age = 1991

print(name, '은', age, '년 생 입니다.')  # 숫자에 ' '를 붙여도 실행 결과는 같음

this_year = 2021 - age

print(name, '은', this_year, '살입니다.') # 숫자형이던 age에 ''를 붙이면 연산이 안되서 에러
                                        # TypeError: unsupported operand type(s) for -: 'int' and 'str'

# 자료형을 구분해서 사용해야 함
# 자료형이 맞지 않으면 에러

print('--------------------------------------------')

# 숫자는 사칙연산 가능
plus = 1 + 2
minus = 1 - 2
multiple = 3 * 3
divide = 30/5
square = 2 ** 10  # **로 제곱 승 수
remainder = 10%5

print(plus, minus, multiple, divide, square, remainder)

div1 = 6/5
div2 = 6//5  # //로 몪 구하기

print(div1, div2)










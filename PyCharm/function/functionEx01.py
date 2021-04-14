print()
'''
# 함수
: 코드 조각에 기능별로 이름을 붙인 것으로 해당 기능을 쉽게 쓸 수 있도록 도와주는 역할
: 반복되는 부분이 있을 경우, 추후에 호출될 가능성이 있을 경우 생성

함수 구조 - 결과값이 없는 함수
def 함수명(입력 인수):  # def(define)
    수행문장~
    ...
'''

def function():
    print('Hello Python Function')

function()  #call by name

print("------------------------------")
# 입력값이 없는 함수 - 매개변수 없는 함수, call by name
a = 10;
b = 20;
def sum():
    result = a + b
    print(result)

sum()

print("------------------------------")
# 입력값이 있는 함수 - 매개변수가 있는 함수, call by value
c = 10
d = 20
def sum(x, y):
    result = x + y;
    print(result)

sum(c, d)

print("------------------------------")

'''
함수 구조 2 - 결과값이 있는 함수 (return)
def 함수명(입력 인수):
    수행문장~
    ...
    return 결과값
'''

def hello():
    return 'hi python function'

hello = hello()
print(hello)

print("------------------------------")

# 실습: 3000만원 연봉을 받는 신입사원 연봉을 10% 인상한 값으로 돌려주는 함수를 생성
def payup(sal):
    return sal*1.1
annual = 3000
upsal = payup(annual)
print(upsal)

print("------------------------------")
# return을 이용해서 어떤 상황이 되어서 함수를 빠져나가고자 할 때도 자주 사용
def return_a():
    for i in range(100):
        return i;


result = return_a()
print(result)  # return 구문은 오직 한개의 객체만 반환하도록 설계됨

print("------------------------------")
def avoid(num):
    if num == 5:
        return
    print(num)

avoid(19)
avoid(5)































print()
# 절차(구조적) 지향 프로그래밍
showInfo = ''


def person(name, age):
    global showInfo
    showInfo += '이름 : ' + name + ', ' + '나이 : ' + age + '\n'
    return showInfo


person('홍길동', '20')  # 함수 호출해서 전역 변수인 showInfo에 정보 집어넣음
person('유관순', '17')  # 남여 구분에 대한 항목을 넣으려면 따로 새로운 함수를 만들어야 함, 확장성 X
print(showInfo)

print('----------------------------------------------------------------------')


# 객체 지향 프로그래밍
class Person:
    def __init__(self):
        self.info = ''  # 변수를 하나 초기화

    def showInfo(self, name, age):
        self.info += '이름 : ' + name + ', ' + '나이 : ' + age
        print(self.info)


man = Person()      # 인스턴스화
man.showInfo('홍길동', '20')  # 재사용과 유지보수 이점

woman = Person()
woman.showInfo('유관순', '17')

print('---------------------------------------------------------------------')
# 객체 정보 : type()
print(type(5))
print(type(man))

# 객체 일치 여부 : isinstance()
print(isinstance(5, int))
print(isinstance(5, Person))

print('---------------------------------------------------------------------')


num1 = []
print(type(num1))

num2 = list(range(10))
print(type(num2))

text = list('hello python')  # 문자열은 리스트랑 비슷해서 이렇게 바로 꽂아도 됨
print(type(text))

print(isinstance(num2, list))
print(isinstance(text, list))


print('---------------------------------------------------------------------')


print(isinstance(num1, list))
print(num1 == list)


















print()

'''
함수 구조 3 - 함수 입력값(매개변수)이 몇 개 인지 모를 경우
def 함수명(*입력변수명(
    <수행문장>
    return
'''

def sum(*args):  #args - 관례적 사용
    sum = 0
    for i in args:
        sum += i
    return sum

result = sum(1, 2, 3, 4, 5, 6, 7 , 8, 9, 10)
print(result)

print("----------------------------------------------")

var = 1
def ranTest(var):  # 변수를 다 var로 만들어서 누구쓰는건지 모름
    var = var + 1  # 함수에 매개변수 사용시, 외부 내부 신경쓸 것

print(ranTest(var))
print(var)

print("----------------------------------------------")

var = 1
def ranTest(var2):  # 변수를 다 var로 만들어서 누구쓰는건지 모름
    var2 = var2 + 1  # 함수에 매개변수 사용시, 외부 내부 신경쓸 것

print(ranTest(var))
print(var)

'''
cf) 내장함수 : import 하지 않고 즉시 사용 가능한 함수들
            : 주의 - 내장 함수명을 일종의 키워드로 간주 
            :      - 사용자(개발자)가 식별자 또는 사용자 정의 함수로 만들어서 사용 

pip을 통해서 내장 함수 가져올 수 있음
'''











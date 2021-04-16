print()
'''
클래스
'''


class Human:
    pass             # 클래스 안에 아무것도 없는 채로 두고 싶으면 pass 구문 사용


person1 = Human()
person2 = Human()

print(person1, person2)     # 서로 주소가 다름, 다른 객체이다.


# Human에 특징 부여 - 값(field) 대입
person1.language = 'KOREAN'     # 동적 타이핑 언어라서 없어도 값을 부여할 수 있다.
person2.language = 'ENGLISH'

print(person1.language)
print(person2.language)

person1.name = '홍길동'
person2.name = '유관순'

print(person1.name)
print(person2.name)


# 객체이므로 행위(함수)도 부여할 수 있음
def speak(person):
    print('{}이 {}로 대화합니다.'.format(person.name, person.language))
# 위처럼 그냥 함수를 선언해 놓으면 일반함수 생성임.
# 클래스 안에 함수가 생성된 상태가 아님
# 클래스 안에 함수를 적용하려면? 클래스가 행위하도록 해주어야 함



# Human.speak = speak
# speak(person1)
# speak(person2)

# speak()을 호출할 때 인자로 person1,2필요

print('---------------------------------------------')
# 클래스가 행위를 하도록 수행
Human.speak = speak

person1.speak();
person2.speak();
# person1,2가 직접 speak 호출

'''
말하는 행위가 중심일 때는 행위 함수에 '누가' 말한것인지 전달
클래스(객체)가 중심일 때는 객체가 말하는 것이므로 굳이 실행인자로 마시 사람을 전달할 필요 X
'''














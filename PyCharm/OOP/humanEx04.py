print()
'''
메소드에 대한 특별한 규칙 : 메소드를 호출할 때 첫번째 인자를 생략하면 인스턴스 자신으로 채워준다.
keyword : self - 자기 자신을 자동으로 호출하는 매개변수
'''

class Human():
    def create_human(name, height):
        person = Human()
        person.name = name
        person.height = height
        return person

    # 먹기
    def eat(self):
        self.height += 0.2
        print('{}이 건강하게 먹어서 {}이 되었어요'.format(self.name, self.height))

    # 걷기
    def walk(self):
        self.height += 0.3
        print('{}이 운동을 해서 {}이 되었어요'.format(self.name, self.height))

    def speak(self, message):
        print(message)


person = Human.create_human('유관순', 162.7)
person.eat()  # 자동으로 self 로서 들어감
person.walk()

print('----------------------------------------------------------------------')
person = Human.create_human('이순신', 178.3)
person.speak('필사즉생')
'''
인스턴스에서 call by value 수행 시 첫번째 매개변수인 self는 생략하고 호출해 줌
파이선이 첫번째 매개변수인 self는 자동으로 호출
'''

print('----------------------------------------------------------------------')
def no_eat(self):
    self.height -= 0.5
    print('{}이 다이어트를 열심히 해서 {}가 되었어요.'.format(self.name, self.height))

person = Human.create_human('신사임당', 43.8)
no_eat(person)

person.no_eat()  # 이건 안됨, 없으니까

























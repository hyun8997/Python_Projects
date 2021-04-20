# 상속
# 부모 클래스 : Super Class
class Animal:

    # 객체 이름 초기화
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('삼시 세끼를 잘 챙깁시다')
    def sleep(self):
        print('하루 8시간은 자야해요')

    def move(self):
        # 각 객체가 걷는다
        print('걷는 것은 {} 이다'.format(self.name))

# 자식 클래스 : Sub Class
class Human(Animal):

    def __init__(self, name, angle):
        super().__init__(name)       # 부모 메소드 호출 : super().메소드명
        self.angle = angle

    def coding(self):
        print('godGoogle, StackOverflow')

    def walk(self):
        print('두 발로 서서 전방 {} 도를 주시하며'.format(self.angle))

    def move(self):
        self.walk()
        super().move()

class Dog(Animal):

    def __init__(self, name, angle):
        super().__init__(name)
        self.angle = angle

    def detect(self):
        print('집을 지키자')

    def walking(self):
        print('네발로 서서 {}를 돌아보며 '.format(self.angle))

    def move(self):
        self.walking()
        super().move()

'''
# 두 발로 서서 전방 15도를 주시하며 걷는 것은 사람이다.
  네 발로 서서 사방을 돌아보며 걷는 것은 강아지이다
 - move
 - angle, name
'''

person = Human('사람', 15)
person.move()

print('-----------------------------------')
dog = Dog('강아지', '사방')
dog.move()

















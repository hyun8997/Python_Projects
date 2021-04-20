# 상속
# 부모 클래스 : Super Class
class Animal:
    def eat(self):
        print('삼시 세끼를 잘 챙깁시다')
    def sleep(self):
        print('하루 8시간은 자야해요')
    def move(self):
        print('걸어요')

# 자식 클래스 : Sub Class
class Human(Animal):
    def coding(self):
        print('godGoogle, StackOverflow')

    def walk(self):
        print('두 발로 걸어요')
    
    def move(self):
        self.walk()

class Dog(Animal):
    def detect(self):
        print('집을 지키자')

    def walking(self):
        print('네발로 걸어요')

    def move(self):
        self.walking()

person = Human()
person.eat()
person.sleep()
person.coding()
person.move()

print('---------------------------')
dog = Dog()
dog.eat()
dog.sleep()
dog.detect()
dog.move()













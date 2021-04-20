# 상속
# 부모 클래스 : Super Class
class Animal:
    def eat(self):
        print('삼시 세끼를 잘 챙깁시다')
    def sleep(self):
        print('하루 8시간은 자야해요')
    def walk(self):
        print('두 발로 걸어요')

# 자식 클래스 : Sub Class
class Human(Animal):
    def coding(self):
        print('godGoogle, StackOverflow')

class Dog(Animal):
    def detect(self):
        print('집을 지키자')

person = Human()
person.eat()
person.sleep()
person.coding()

print('---------------------------')
dog = Dog()
dog.eat()
dog.sleep()
dog.detect()













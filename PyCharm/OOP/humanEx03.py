class Human():
    pass

    def creadte_human(name, height):
        person = Human()
        person.name = name
        person.height = height
        return person

    def eat(person):
        person.height += float(0.1)
        print('{}이 건강하게 먹어서 {}이 되었어요'.format(person.name, person.height))

    def walk(person):
        person.height += float(0.2)
        print('{}이 운동을 해서 {}이 되었어요'.format(person.name, person.height))


'''
클래스 구조
class 클래스명:
    변수  - 클래스에 내부 변수들을 필드(field)라고 부름
    
    함수  - 클래스 내부 함수들을 메소드(method)

클래스는 필드와 메소드로 구성된다. 이를 클래스의 속성(attribute)이라고 정의


'''






































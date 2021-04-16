print()
'''
특수한 메소드 : 메소드 이름 양쪽에 __있는 메소드
-> python special attributes

'''

class Human:
    # 초기화 메소드
    def __init__(self):
        pass
        print('__init 실행')

    def __init__(self, name, height):
        print('__init 실행')
        print('이름:{}, 키:{}'.format(name, height))

    # 문자열화 메소드 : 인스턴스를 문자열로 변환할 때 어떻게 표현할지를 결정
    def __str__(self):
        return "이름 : {}, 키 : {}".format(self.name, self.height)




#person = Human()  # 자동으로 init 실행함

#person = Human('홍길동', 178.8)

person = Human('유관순', 160.3)
print(person)  # 오류나는데? 'Human' object has no attribute 'name'






















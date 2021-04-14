# coding: utf-8

# java는 객체와 클래스가 같은데
# 파이선은 객체 안에 클래스가 있는 형태

class Singer:
    def __init__(self, name="브브걸"):  # 생성자 역할, 파이선 대부분의 코드에서
        self.name = name               # 여기의 self는 쓰지 않아도 자동으로 알아서 인식

    def song(title='No name'):  # self가 없어도 위의 생성자처럼 앞칸에 self 있는거임
        print('Hit Number', title)














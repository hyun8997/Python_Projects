print()
'''
dictionary : {name1 : value1, name2 : value2, ...}
'''

wager = {
    '가위': '보',
    '바위': '가위',
    '보': '바위'
}

print('name = 보 -> value =', wager['보'])  # 이름으로 값을 찾아옴


# 가위, 바위, 보 승패 판정 함수 생성
def rsp(x, y):   # 내가 낸 것 x, 남이 낸 것 y
    if y == wager[x]:
        print('승리')
    elif x == y:
        print('무승부')
    else:
        print('패배')


import random

game = ['가위', '바위', '보']
mine = random.choice(game)
others = random.choice(game)

print('x =', mine, ', y =', others)
rsp(mine, others)

print('---------------------------------------')
# name에는 리스트를 사용할 수 없지만 값에는 리스트 사용 가능
dic = {
    'tag': [1, 2, 3]
}

print(dic)


















































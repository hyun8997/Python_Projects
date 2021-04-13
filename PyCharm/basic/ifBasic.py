print()
'''
조건문(분기문)    :를 사용하고 들여쓰기로 코드블럭 인식
if 조건 :
    수행문장 1
    수행문장 2
    .
    .
'''

people = 2

if people:  #0은 false, 그 외는 true (C와 같은듯?)
    print('사람이 한 명 들어있어요')

'''
들여쓰기 중요 : 코드 블록을 구분해 주는 역할
탭 또는 스페이스바 4칸을 이용하여 들여쓰기 수행하면 됨 (cf. python 2.x라면 혼용 안됨)
'''

if people==1:
    print('사람이 한 명 있습니다')
elif people==2:
    print('사람이 2명')
else:
    print('모름')

# 조건 참/거짓을 구분할 때는 연산자(비교, 논리) 사용

#비교 연산자
x = 3
y = 2

if x!=y:
    print('x, y 서로 다름')

print('------------------------------------------')

'''
블록 - 콜론(:) 다음에 들여쓴 코드 블록
     - 같은 실행 흐름에서 순서대로 실행되는 코드 덩어리
     - 여러 줄로 작성이 가능, 여러 줄일 경우, 들여쓰기 칸 수가 모두 같아야 함
'''

# 논리 연산자 : True, False
if True:
    print('블록 코드')
    print('같은 블록')
    print('여러줄 가능')

'''
블록을 끝내려면 들여쓰기를 끝내줘야 함 - 내어쓰기
한번이라도 내어 쓴 블록은 끝난 블록이 되고, 다시 열 수 없음
'''

print('------------------------------------------')

print('바깥에 있는 코드')

if True:
    print('첫번째 블록 코드')
    # 블록 안에는 또 다른 블록이 들어갈 수 있음
    if False:
        print('실행되지 않을 코드')
    if True:
        print('첫번째 - 안쪽 블록 코드')
    print('첫번째 블록 끝 코드')
print('바깥 코드')

print('------------------------------------------')

if False:
    print('첫번째 블록 코드')
    # 블록 안에는 또 다른 블록이 들어갈 수 있음
    if False:
        print('실행되지 않을 코드')
    if True:
        print('첫번째 - 안쪽 블록 코드')
    print('첫번째 블록 끝 코드')
print('바깥 코드')

print('------------------------------------------')

'''
분기
if <조건> : 
    <코드 블록>
else:
    <코드 블록>
'''

num1 = 50
num2 = 100

# 둘 중 큰 수 구하기
if num1 > num2:
    print('num1:', num1, '이(가) 더 큼')
else:
    print('num2:', num2, '이(가) 더 큼')

#절대값 구하기(????????)
if num1 > num2:
    dif = num1 - num2
    print(dif)
else:
    dif = num2 - num1
    print(dif)

'''
elif가 else if임
'''


#입력을 받는 내장함수 : input()
'''value = input()
print(value)'''

#프롬프트에 알리고 입력받기
'''
value = input("숫자를 입력하세요:")
print(value)

score = int(value)

if score > 50:
    print('50이상')
elif score > 30:
    print('30이상')
else:
    print('0')
'''

print('------------------------------------------')

#태어난 년도 4자리 입력받아서 화면에 당신은 ~~~ 띠 입니다 출력
#자축인묘 진사오미 신유슬해
#쥐소호토 용뱀말양 원닭개되
#4 5 6 7 8 9 10 11 12 1 2 3

value = input("태어난 년도 입력:")
role = int(value) % 12

if role == 4:
    print('당신은 쥐띠입니다.')
elif role == 5:
    print('당신은 소띠입니다.')
elif role == 6:
    print('당신은 호랑이띠입니다.')
elif role == 7:
    print('당신은 토끼띠입니다.')
elif role == 8:
    print('당신은 용띠입니다.')
elif role == 9:
    print('당신은 뱀띠입니다.')
elif role == 10:
    print('당신은 말띠입니다.')
elif role == 11:
    print('당신은 양띠입니다.')
elif role == 0:  #==12
    print('당신은 원숭이띠입니다.')
elif role == 1:
    print('당신은 닭띠입니다.')
elif role == 2:
    print('당신은 개띠입니다.')
else:  #==3
    print('당신은 돼지띠입니다.')






















# list = []
#
# print(list[0])

print('---------------------------')
# text = 'aaa'
#
# number = int(text)
#
# print(number)

print('---------------------------')
try:
    list = []
    print(list[0])

    text = 'aaa'
    number = int(text)
    print(number)
except:  # 어떤 오류인지 명확하지 않을 때 일단 열어둘 수 있음
    print('오류 발생')  # 잡아는 주지만 어떤 오류인지 모름

print('---------------------------')
# 가장 상위의 에러를 사용해서 어떤 오류가 나는지 받아올 수 있다.
try:
    # list = []
    # print(list[0])

    text = 'aaa'
    number = int(text)
    print(number)
except Exception as ex:  # 이렇게 별칭을 선언해두면 어떤 오류인지 받을 수 있다.
    print('오류 발생', ex)






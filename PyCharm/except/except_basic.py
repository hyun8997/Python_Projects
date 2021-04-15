print()

# list = []
#
# print(list[0])  # 인덱스가 없는데 불러서 오류

print('----------------------------------------------------')

# text = 'abc'
#
# number = int(text)

print('----------------------------------------------------')
# 파이선은 컴파일 언어가 아니라서 에디터가 오류를 안잡아줌(인터프리터 언어), exception 처리 중요
'''
[예외처리]
 - 예외 : 프로그램에서 벌어지는 예외적인 상황(에러)을 의미
 - ex) FileNotFoundError (파일이 없을 때)
       ZeroDivisionError (숫자를 0으로 나눌 때 에러)
       IndexError (리스트에서 얻어 올 수 없는 값일 경우 에러)
       SyntaxError (문법, 구문 오류)
       EOFError (파일의 끝일 경우, 더 이상 읽을 내용 없을 경우)
       ValueError (캐스팅 오류, type error)
       TypeError
       ...

 - 기본 형식
 try :
    수행 명령
 except [발생에러[as 에러메시지 변수]] :
    수행 명령

'''

text = '100%'

try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아닙니다.'.format(text))

print('-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-')
def pop(list, index):
    try:
        print(list.pop(index))  #index 번호를 받아서 처리하니까 인덱스가 없으면 에러날듯
        print(list)
    except IndexError:
        print('{} index 값이 없습니다.'.format(index))

pop([1, 2, 3], 1)  # 정상 동작
pop([1, 2, 3], 5)  # 에러메세지 출력, 없는 인덱스

# 위 pop과 같은 결과를 얻고 싶으나, try-except 이 없다면? if 구문으로도 직접 처리 가능

print('-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-')
# except 중첩 가능
# try:
#     str = input('문자를 입력하세요 : ')
# except EOFError:
#     print('읽은 내용이 없습니다.')
# except KeyboardInterrupt:
#     print('입력 취소되었습니다.')
# else:
#     print('except가 아닌 나머지 - {}'.format(str))
# finally:
#     print('개의치 않고 실행')

print('-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-')
# pass 구문 : 비어있는 클래스를 만들 수 없다. 뭐라도 넣어야 하는데 틀만 만들고 나중에 작업할때 사용
#            에러가 발생하여 except로 들어갈 경우 통과시키기 위한 구문
try:
    f = open('nofile.txt', 'r')
except FileNotFoundError:
    pass  # 보통은 에러터지면 따로 특정 로직을 실행하지만, 하지않고 넘기도록
    print('에러없이 수행되었음')

class Test:  # 틀만 만든 클래스에 pass 넣어서 오류 안뜨게
    pass




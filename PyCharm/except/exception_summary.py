print()
'''
exception 다루는 방법
1) 예외를 잡는 방법
2) 파이선에 미리 정의되어 있는 예외를 일으키는 방법
'''

# value = '가'
#
# try:
#     if value not in ['A', 'B', 'C']:
#         raise ValueError('알파벳 중 하나이어야 합니다.')
# except ValueError as ve:
#     print('오류가 발생했음 :', ve)

'''
코드가 복잡해지고 함수를 여러번 호출하게 되면 오류를 낼 수 있는 코드도 많아지게 됨.

더해서 어디에선가는 잡지 말아야 할 오류를 잡게 되어버린다면 
전체 코드 진행이 의도한대로 되지 않을 가능성도 있어짐

또 이미 처리해버린 오류가 실제 어디서 발생했는지 알아내는 것은 처리 하지 않은 오류가 
어디서 발생했는지 알아내는 것보다 번거로움

이런 다양한 문제들을 처리하기 위해 파이선도 프로젝트에 맞게 예외를 하나의 클래스(사용자 정의)로 
만들어서 직접 새 예외를 만들 수 있음
'''

# from 구문 후 호출할 파이선 모듈이 안보일 경우 : 그냥 디렉토리일 경우 발생(낮은 버전에서), source 루트로 하면 됨
from exceptionObject import Unexpected_exep

value = '가'

try:
    if value not in ['A', 'B', 'C']:
        raise Unexpected_exep
except Unexpected_exep:
    print('오류가 발생했음')

'''
사용자 정의로 exception 처리 결과는 일반 오류 처리 결과와 섞이지 않고
모두 처리해 줌을 확인할 수 있음
'''

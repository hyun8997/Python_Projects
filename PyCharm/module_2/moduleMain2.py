print()
'''
특정 함수나 클래스만 불러오기
from <모듈명> import <함수명>
'''
# calculator 모듈의 add()만 호출
from calculator import add

print(add(100, 200))

# calculator 모듈의 모든 메소드 사용
from calculator import *
    # 이렇게 하면 이미 모듈을 호출한것이므로 calculator를 안쓰고 함수만 불러도 됨
print(add(100, 200))
print(mul(100, 200))
print(div(100, 200))

print('-----------------------------------------------------')
# 모듈을 다른 이름으로 호출(별칭) - 사용하려는 모듈 이름이 너무 긴 경우
# ex) 관례적인 별칭 tensorflow -> tf, pandas -> pd, numpy -> np, matplotlib -> plt
import thisisVeryLongNameModule as t

t.hello()







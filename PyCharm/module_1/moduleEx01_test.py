import math

# 둘레 구하기 : r * 2 * 3.14
import os

r = 10

print(r * 2 * math.pi)

# 올림 : ceil
print(math.ceil(3.4))

# 내림 : floor
print(math.floor(3.8))

# 반올림 : round, 자주 사용해서 기본 내장함수임
print(round(3.14))

# 이 밖에도 삼각함수, 지수, 승, 로그 등 다양한 기능이 math에 있음

print('-------------------------------------------------------------------')

import sys

print(sys.argv)
print(sys.path)     # 어떤 환경에서 어떤 작업하는지 현재 환경 확인
                    # 추후 pip으로 import 할 때 오류나면 환경설정 파악 가능

print('-------------------------------------------------------------------')


import os

# 시스템의 환경변수값 확인 - 시스템의 정보를 딕셔너리 객체로 리턴
print(os.environ)  # '이름' : '값' 형태

# 환경변수 - 인덱싱
print(os.environ['Path'])  # 환경 변수의 Path를 인덱싱해옴

# 현재 위치 확인
print(os.getcwd())

# 디렉토리 변경
#os.chdir('C:\\Users\\goott7\\PycharmProjects\\goott_python')  # 경로의 \\ 유의
print(os.getcwd())

os.system('dir')  # os의 커멘드 창 명령어 사용, 한글 엔코딩 깨져서 나옴

'''
그 외 os 모듈
os.popen : 시스템 명령어를 수행한 결과값을 읽기모드의 파일 객체로 리턴
os.mkdir(디렉토리명) : 디렉토리 생성
os.rmdir(디렉토리명) : 디렉토리 삭제 (주의 - 디렉토리가 비어있어야 함)
os.unlink(파일명) : 파일 삭제
os.rename(src, dst) : src 이름 파일을 dst 이름으로 바꿈 
'''
#os.mkdir('testDir')
#os.rmdir('testDir')


print('-------------------------------------------------------------------')

import shutil

'''
shutil.copy(src, dst) : src라는 이름으로 파일을 dst로 복사
'''
shutil.copy('moduleEx01.py', 'moduleEx01_test.py')



























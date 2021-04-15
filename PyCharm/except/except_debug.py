print()
'''
다른 코드에서 쓸 함수나 모듈을 생성 시 디버깅을 먼저 해보기 위해서 오류를 일으켜 볼 수도 있음
'''

# ex) 가위, 바위, 보 함수 체크 - / 묵, 찌, 빠 가 입력될 때
def rsp(x, y):
    allowed = ['가위', '바위', '보']
    if x not in allowed:
        raise ValueError   # 오류를 일부러 발생시키는 키워드
    if y not in allowed:
        raise ValueError

#rsp('가위', '바위')

try:
    rsp('가위', '묵')
except:
    print('잘못된 값 입력')

print('------------------------------------------------------')
# 예외처리 말고도 오류를 활용하는 다른 방법도 존재
# : 중첩된 반복문에서 예외를 발생시켜 전체 반복문 밖으로 빠져나가기
'''
ex) KBL 구단 2개
    (조건: 3m를 넘는 선수가 있으면 그 구단 정보를 출력하고 구단활동 정지)
    두 구단 중 먼저 3m 넘는 선수가 있는 구단을 찾는 순간 다 정지
'''
kbl = {'A구단': [178, 188, 190, 198, 302], 'B구단': [199, 192, 189, 301, 208]}

for id, heights in kbl.items():
    # print(id, heights)  # 딕셔너리라서 키 2개, 그에 해당하는 값    해서 2번 실행함
    for height in heights:
        if height > 300:
            print(id, '3m를 넘는 선수를 발견했습니다.', height)
            break
        # 이 방식은 두 팀 다 찾음
print('------------------------------------------------------')
# 한 팀에서 찾으면 나오도록 함, 오류 활용
# for id, heights in kbl.items():
#     # print(id, heights)  # 딕셔너리라서 키 2개, 그에 해당하는 값    해서 2번 실행함
#     for height in heights:
#         if height > 300:
#             print(id, '3m를 넘는 선수를 발견했습니다.', height)
#             raise StopIteration  # 반복을 멈추게 하는 오류


# 반복을 멈추면서 프로그램도 멈추므로 에러를 띄우면서 에러를 잡게 하면 됨(계속 돌아가도록)
try:
    for id, heights in kbl.items():
        # print(id, heights)  # 딕셔너리라서 키 2개, 그에 해당하는 값    해서 2번 실행함
        for height in heights:
            if height > 300:
                print(id, '3m를 넘는 선수를 발견했습니다.', height)
                raise StopIteration  # 찾고나서 완전히 멈추고
except StopIteration:
    print('협회 차원에서 처리중...')   # 그 다음 로직을 실행 시킬 수 있다, 오류 활용










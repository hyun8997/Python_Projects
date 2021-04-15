seasons = ['봄', '여름', '가을', '겨울']

for s in seasons:
    print(s)

print('----------------------------------')
result = {'java': 80, 'jsp': 90, 'spring': 80}

print(result)


# key, value 각각 호출 가능
for key in result.keys():
    print(key)

for value in result.values():
    print(value)

print('---------------------------------------------------')
# 과목과 점수 모두를 출력 - key를 가져오는게 우선
for key in result.keys():  # 당연히 key로 불러온다는 것을 파이선도 알아서 keys() 삭제해도 인식
    print('{} 점수는 {} 입니다.'.format(key, result[key]))

print('000000000000000000000000000000000000000000000000000')
# 리스트도 인덱스 번호를 통해서 값을 구하는 방식 - enumerate()을 통해 두가지 정보를 처리
# 딕셔너리도 위와 같은 역할을 하는 함수가 존재: items()
for key, value in result.items():
    print('{} 점수는 {} 입니다.'.format(key, value))

'''
출력 순서가 다를 수 있다.

리스트는 인덱스가 있으니까 순서가 존재하지만 
딕셔너리는 key가 있고 순서가 필요없으니 항상 같은 순서로 출력될 보장이 없다.
순서가 중요한 경우라면 딕셔너리가 아닌 리스트를 사용해야 함
'''





















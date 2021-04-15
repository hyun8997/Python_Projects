print()

# 리스트
list = [1, 2, 3, 4, 5]
print(list)

# 3번째 값을 수정
list[2] = 33
print(list)

# 리스트에 새로운 값을 추가 - 없는 인덱스에 값을 추가하면 오류남, append 사용
list.append(6)
print(list)

print('------------------------------------')
# 딕셔너리
dict = {'one': 1, 'two': 2, 'three': 3}
print(dict)

# 수정 - 리스트와 비슷(단, 인덱스가 아닌 이름을 호출해서 수정)
dict['two'] = 22
print(dict)

# 새로운 값 추가 - append() 와 같은 함수는 없다
dict['four'] = 4
print(dict)

print('-------------------------------------------')
# 삭제 - 리스트, 딕셔너리 모두 값음 (인덱스/이름 차이)
del(list[0])
print(list)

del(dict['one'])
print(dict)

# pop()
result = list.pop(0)  # del과 같은 동작이지만 무엇을 없앴는지 리턴함
print(list, '지워진것 :', result)

result = dict.pop('two')
print(dict, '지워진것 :', result)

















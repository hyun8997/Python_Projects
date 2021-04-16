print()
'''
파이선은 조건식을 사용할 때 and 연산과 or 연산을 적극적으로 활용한다.
'''


# ex) 항상 False만을 반환하는 함수
def always_false():
    print('언제나 false')
    return False


# ex) 항상 True만을 반환하는 함수
def always_true():
    print('언제나 True')
    return True


result1 = always_false()
result2 = always_true()

# print(result1, result2)

if result1 and result2:
    print(True)
else:
    print(False)

print('-------------------------------------------------')
# 변수에 담지 않고 바로 함수를 호출해서 조건식 사용
if always_false() and always_true():
    # false가 하나라도 있으니까 and 까지만 보고 뒤에 뭐가 오든 false 니까 바로 else로 넘김
    print(True)
else:
    print(False)

'''
파이선은 and 나 or 연상을 할 때 첫 번째 값을 보고 더 이상 실행할 필요가 없으면
두 번째 값을 실행하지 않음
=> 이런 활용을 단락 평가(short-circuit)이라고 함
'''

# 단락 평가로 인해 앞의 false를 보고 and를 보자마자 뒤를 보지 않고 false 반환
print(always_false() and always_true())

print('-------------------------------------------------')


# 단락 평평가 복잡한 코드를 단순하게 하는데 유용함
dic = {'key2', 'value1'}

# key1에 value1이 대입되어 있는지 확인
if 'key1' in dic:
    if dic['key1'] == 'value1':
        print('dic의 key1에 value1이 존재')
    else:
        print('dic에 key1이 있으나 values1이 아님')
else:
    print('dic에 key1이 없음')

print('-------------------------------------------------')

if 'key1' in dic and dic['key1']=='value1':
    print('dic의 key1에 value1이 존재')
else:
    print('dic에 key1이 없음')

print('-------------------------------------------------')

# if dic['key1']=='value1' and 'key1' in dic:  # 이건 에러남
#     print('dic의 key1에 value1이 존재')
# else:
#     print('key1이 없음')








































































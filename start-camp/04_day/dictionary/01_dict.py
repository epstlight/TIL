#dictionary make
lunch1 ={
    '중국집': '02',
}
print(lunch1)

lunch2 = dict(중국집='02') #{}
print(lunch2)

#dictionary 내용 추가하기

print(lunch1['중국집'])
lunch1['분식집'] = '031'
print(lunch1)

idol = {
    'bts': {
        '지민': 24,
        'RM': 25
    }
}

print(idol['bts']['RM'])

#dictionary 반복문 활용하기  dic for문돌리면 key값만 나옴     // keys(), values(), items() 튜플로 묶여서 나옴
for key in lunch1 :
    print(key, lunch1[key], sep=' : ')

#value만 가져오기 
for value in lunch1.values() :
    print(value)
for key, value in lunch1.items():
    print(key, value)

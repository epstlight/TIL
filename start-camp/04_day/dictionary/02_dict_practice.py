# 1. 평균을 구하시오.

score = {

    '수학': 80,

    '국어': 90,

    '음악': 100

}

# 아래에 코드를 작성해 주세요.

print(sum(score.values())/len(score))


# 2. 반 평균을 구하시오. -> 전체 평균

scores = {

    'a': {

        '수학': 80,

        '국어': 90,

        '음악': 100

    },

    'b': {

        '수학': 80,

        '국어': 90,

        '음악': 100

    }

}



# 아래에 코드를 작성해 주세요.

a_avr = sum(scores['a'].values())/len(scores['a'])
b_avr = sum(scores['b'].values())/len(scores['b'])

print((a_avr+b_avr)/(len(scores['a'])+len(scores['b'])))










# 3. 도시별 최근 3일의 온도입니다.

city = {

    '서울': [-6, -10, 5],

    '대전': [-3, -5, 2],

    '광주': [0, -2, 10],

    '부산': [2, -2, 9],

}

# 3-1. 도시별 최근 3일의 온도 평균은?


# 아래에 코드를 작성해 주세요.


for city_name in city:
    city_avr = sum(city[city_name])/len(city[city_name])
    print('%s : %.2f \n' %(city_name, city_avr))


"""

출력 예시)

서울 : 값

대전 : 값

광주 : 값

부산 : 값

"""


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

city_max = 0
city_min = 9999
city_maxname = ''
city_minname = ''

for city_name in city :
    for city_temper in city[city_name] :

        if city_max < city_temper :
            city_max = city_temper
            city_maxname = city_name

        if city_min > city_temper :
            city_min = city_temper
            city_minname = city_name



# 아래에 코드를 작성해 주세요.

print(f'가장 추웠던 곳 : {city_minname}, {city_min}도')
print(f'가장 더웠던 곳 : {city_maxname}, {city_max}도')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.

if 2 in city['서울'] :
    print('서울은 영상 2도였던 적이 있다.')
else : 
    print('서울은 영상 2도였던 적이 없다.')


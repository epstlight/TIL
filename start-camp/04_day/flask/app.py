from flask import Flask, render_template, request   #request는 flask 자체에서 제공되며, 사용자의 요청을 확인할 수 있도록 해주는 모듈 
import requests, bs4
app = Flask(__name__)

@app.route('/')    # '/'  => root 
def index():
    return 'hello world!'


@app.route('/greeting/<name>')
def greeting(name):
    return f'안녕 {name}'


@app.route('/greeting2/<name>')
def greeting_tem(name):
    return render_template('greeting.html', name=name)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age=age)


@app.route('/google')
def google():
    return render_template('google.html')

    
@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')

    
@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')  # Message
    #Ascii art API를 활용해서 사용자의 input값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    return render_template('ascii_result.html', result=response.text)


@app.route('/lotto_input')
def lotto_input():
    return render_template('lotto_input.html')

@app.route('/lotto_result')
def lotto_result():
    n_round = request.args.get('round')
    numbers = list(map(int, request.args.get('numbers').strip().split(" ")))
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n_round}'

    lotto_info = requests.get(url).json()  #json 타입의 파일을 dic로 parsing 해줘


    if len(numbers) == 6 : 
        cnt = 0
        bnus = False
        for i in range(1,7):
            if lotto_info[f'drwtNo{i}'] in numbers :
                cnt += 1
                
        if lotto_info['bnusNo'] in numbers:
                bnus = True

        if cnt == 3:
            result_num = 5 
        elif cnt == 4:
            result_num = 4 
        elif cnt == 5 and bnus == True:
            result_num = 2 
        elif cnt == 5:
            result_num = 3 
        elif cnt ==6:
            result_num = 1 
        else : 
            result_num = 0

        if result_num == 0:
            return '꽝!'
        else :
            return f'{result_num}등 입니다.!'

    else : 
        return '잘못 입력하셨습니다.'


if __name__ == "__main__":
    app.run(debug=True)

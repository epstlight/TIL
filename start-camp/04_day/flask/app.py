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


if __name__ == "__main__":
    app.run(debug=True)

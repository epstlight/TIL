from flask import Flask, render_template 
import datetime
import random

app = Flask(__name__)


@app.route("/")   #endpoint
def hello():
    # return "Hello Python!"
    return render_template('index.html')     # render_template 모듈을 통해서 template 폴더의 있는 파일을 불러 올 수 있다.  폴더명은 꼭 template 여야만 한다. 

@app.route('/ssafy')
def ssafy():
    return 'Hello ssafy'


@app.route('/D-day')
def Dday():
    today = datetime.datetime.now()
    bday = datetime.datetime(2019, 9, 17)
    td = bday - today
    return f'{td.days} 일 남았습니다.'


@app.route('/html')
def html():
    return '<h1>this is HTML h1 Tag</h1>'


@app.route('/html_lines')
def html_lines():    #'''으로 감싸면 스트링으로 받아 들여짐 
    return '''   
    <h1>SSAFY 2기</h1>
    <h2 style="color:gold;"> 개별로 stlye입히기 </h2>
    <span>문단을 구분하지 않습니다.</span>
    '''

@app.route('/greeting/IU')
def greeting_IU():
    return '반갑습니다! IU님!'


@app.route('/greeting/ZionT')
def greeting_ZionT():
    return '반갑습니다! ZionT님!'


#Variable Routing
@app.route('/greeting/<name>')  #url에서 변수를 받아서 적용할 수 있다. 기본적으로 String Type 으로 받는다 
def greeting(name):
    return render_template('greeting.html', name=name)


@app.route('/cube/<int:number>') 
def cube(number):
    return render_template('cube.html', html_num=number, html_num3=number ** 3)

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '짬뽕', '볶음밥', '탕수육', '깐풍기']
    result_menu = random.sample(menu, people)
    return str(result_menu)
    
@app.route('/movie')
def movie():
    movies =['스파이더맨', '알라딘', '엔드게임', '기생충']
    return render_template('movie.html', movies=movies)

if __name__ == "__main__":
    app.run(debug=True)


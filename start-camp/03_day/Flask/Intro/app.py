from flask import Flask
import datetime
import random

app = Flask(__name__)

@app.route("/")   #endpoint
def hello():
    return "Hello Python!"

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

@app.route('/html_link')
def html_link():
    pass

@app.route('/greeting/IU')
def greeting_IU():
    return '반갑습니다! IU님!'

@app.route('/greeting/ZionT')
def greeting_ZionT():
    return '반갑습니다! ZionT님!'

#Variable Routing
@app.route('/greeting/<name>')  #url에서 변수를 받아서 적용할 수 있다. 기본적으로 String Type 으로 받는다 
def greeting(name):
    return f'반갑습니다! {name}님!'

@app.route('/cube/<int:number>') 
def cube(number):
    return f'{number}의 3제곱은 {number ** 3} 입니다.'

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '짬뽕', '볶음밥', '탕수육', '깐풍기']
    result_menu = random.sample(menu, people)
    return str(result_menu)
    

if __name__ == "__main__":
    app.run(debug=True)


# app.py
from flask import Flask, render_template
import naver_corona

# flask app create
app = Flask(__name__)

# url setting = 라우터 설정
@app.route('/')
def index():
    # corona_data = {'k1':3, 'k2':6, 'k3':9} # 가짜 데이터
    corona_data = naver_corona.get_corona_summary() # 진짜 데이터
    return render_template("index.html", corona_data=corona_data)

@app.route('/prac')
def practice():
    return render_template('jinja_practice.html')

@app.route('/chart')
def chart():
    return render_template('chart_practice.html')

# 플라스크 앱 실행
if __name__ == "__main__":
    app.run(debug=True)

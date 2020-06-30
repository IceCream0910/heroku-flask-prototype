from flask import Flask, render_template
app = Flask(__name__)

# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup


@app.route('/')
def hello():

    # 엔터치기
    req = requests.get('https://www.daum.net/')

    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')

    myList = []

    for i in soup.select("#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li") :
        myList.append(i.find("a").text)
        print(i.find("a").text)

    return render_template("index.html", list = myList)

@app.route('/about')
def about():
    return "여기는 어바웃입니다."


if __name__ == '__main__':
    app.run()

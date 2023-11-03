from flask import Flask, redirect, url_for, request, jsonify, render_template
import crawler
import requests
from bs4 import BeautifulSoup
import re


app = Flask(__name__)

#최민주 바보설. 플라스크라는 건 플라스크로 서버를 구동시키는 거고 플라스크로 웹개발을 하는 거고, 그냥 프레임워크가 플라스크인 거잖아
#그래서 여기 route에서 index.html이라는 파일을 가져오는 거잖아. 그러면 걍 플라스크만 작동시키면 알아서 html이 따라오는 거잖아
#근데 프론트랑 백 개념으로 계속 잘못 이해해서 플라스크는 플라스크대로 구동 시켜놓고 또 html 따로 작동시켜서 포트번호 왜 다르지,, 왜 작동 안되지,, 포트번호를 지정해줘야 되나... 하면서 하루종일 고민함

@app.route("/") #얘 주소로 가면 index.html 나오는 거
def index():
    return render_template('index.html')
#templates에 넣을 거면 그냥 open.read 하면 안되고 render_template 해야 함.
#거기에 안 넣고 그냥 밖에 있는 거 하려면 걍 open.read 해도 됨. 근데 그러면 또 css 문제가 생기니 지금처럼 하자^~^
@app.route('/redirect-to-index')
def redirectToIndex():
    return redirect(url_for('index'))

@app.route("/write") #얘 주소로 가면 index.html 나오는 거
def write():
    return render_template('write.html')

@app.route("/run-script")
def run_script():
    result = crawler.crawl_velog('https://velog.io/')
    return jsonify(result)

@app.route("/run-recent")
def run_recent():
    result = crawler.crawl_velog('https://velog.io/recent')
    return jsonify(result)

@app.route("/process-url", methods=['POST'])
def process_url():
    data = request.get_json()
    url = data['url']
    print("ldksajlfskdjflkasjdf" + url)
    
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    

    title = soup.find('h1').text

    # 사용자 이름을 찾는 부분
    username_element = soup.find('span', class_='username')
    if username_element and username_element.a:
        username = username_element.a.text
    else:
        username = "Unknown"

    # 날짜를 찾는 부분
    date_element = soup.find('span', string=re.compile(r"\d+일 전"))
    if date_element:
        date = date_element.text
    else:
        date = "Unknown date"

    # 좋아요 수를 찾는 부분
    like_element = soup.find('button', {'data-testid': 'like-btn'})
    if like_element and like_element.span:
        like_count = like_element.span.text
    else:
        like_count = "0"

    # 썸네일 이미지 URL을 찾는 부분
    image_url_element = soup.find('img')  # 첫 번째 이미지를 기준으로 가져옴
    if image_url_element and 'src' in image_url_element.attrs:
        image_url = image_url_element['src']
    else:
        image_url = ""

    return {
        'title': title,
        'username': username,
        'date': date,
        'like_count': like_count,
        'image_url': image_url
    }


#이렇게.. 캐시를 지워줍시다...
@app.after_request
def add_header(response):
    response.cache_control.no_cache = True
    return response

if __name__ == "__main__":
   app.run(debug=True)


from flask import Flask, jsonify, render_template
import crawler

app = Flask(__name__)

#최민주 바보설. 플라스크라는 건 플라스크로 서버를 구동시키는 거고 플라스크로 웹개발을 하는 거고, 그냥 프레임워크가 플라스크인 거잖아
#그래서 여기 route에서 index.html이라는 파일을 가져오는 거잖아. 그러면 걍 플라스크만 작동시키면 알아서 html이 따라오는 거잖아
#근데 프론트랑 백 개념으로 계속 잘못 이해해서 플라스크는 플라스크대로 구동 시켜놓고 또 html 따로 작동시켜서 포트번호 왜 다르지,, 왜 작동 안되지,, 포트번호를 지정해줘야 되나... 하면서 하루종일 고민함

@app.route("/") #얘 주소로 가면 index.html 나오는 거
def index():
    return render_template('index.html')
#templates에 넣을 거면 그냥 open.read 하면 안되고 render_template 해야 함.
#거기에 안 넣고 그냥 밖에 있는 거 하려면 걍 open.read 해도 됨. 근데 그러면 또 css 문제가 생기니 지금처럼 하자^~^

@app.route("/run-script")
def run_script():
    result = crawler.crawl_velog('https://velog.io/')
    return jsonify(result)

@app.route("/recent")
def run_recent():
    result = crawler.crawl_velog('https://velog.io/recent')
    return jsonify(result)



#이렇게.. 캐시를 지워줍시다...
@app.after_request
def add_header(response):
    response.cache_control.no_cache = True
    return response

if __name__ == "__main__":
   app.run(debug=True)


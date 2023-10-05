
from flask import Flask, jsonify
import python  # 당신의 크롤링 스크립트

app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/run-script")
def run_script():
    result = python.crawl_velog()  # 크롤링 스크립트 실행 함수
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

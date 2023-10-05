
from flask import Flask, jsonify
import crawler

app = Flask(__name__)

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/run-script")
def run_script():
    result = crawler.crawl_velog()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

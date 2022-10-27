from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>楊子青Python網頁</h1>"
    homepage += "<a href=/about>個人求職自傳履歷網頁</a><br>"
    return homepage

@app.route("/about")
def about():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
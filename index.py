import firebase_admin

from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

from flask import Flask, render_template, request

from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")

def index():

homepage = "<h1>陳霈哲Python網頁</h1>"

homepage += "<a href=/mis>MIS</a><br>"

homepage += "<a href=/today>顯示日期時間</a><br>"

homepage += "<a href=/welcome?nick=tcyang>傳送使用者暱稱</a><br>"

homepage += "<a href=/about>霈哲簡介網頁</a><br>"

homepage += "<br><a href=/read>讀取Firestore資料</a><br>"

return homepage

@app.route("/read")

def read():

Result = ""

collection_ref = db.collection("靜宜資管")

docs = collection_ref.order_by("mail", direction=firestore.Query.DESCENDING).get()

for doc in docs:

Result += "文件內容：{}".format(doc.to_dict()) + "<br>"

return Result
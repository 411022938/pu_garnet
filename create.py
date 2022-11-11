import firebase_admin

from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [

{

"name": "陳武林",

"mail": "wlchen@pu.edu.tw",

"lab": 665

},

{

"name": "楊子青",

"mail": "tcyang@pu.edu.tw",

"lab": 579

},

{

"name": "莊育維",

"mail": "ywchuang@pu.edu.tw",

"lab": 566

},

{

"name": "汪于茵",

"mail": "yywang13@pu.edu.tw",

"lab": 674

}

]

collection_ref = db.collection("靜宜資管")

for doc in docs:

collection_ref.add(doc)
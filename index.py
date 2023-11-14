from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
import firebase_admin
from firebase_admin import credentials, firestore 

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
app = Flask(__name__)
db = firestore.client()


@app.route("/")
def index():
    homepage = "<h1>黃子鑒Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=ZGHUANG>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>子鑒簡介網頁</a><br>"
    homepage += "<a href=/account>帳號密碼表單</a><br>"
    homepage += "<br><a href=/books>圖書</a><br>"
    homepage += "<br><a href=/query>查詢</a><br>"
    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    tz = timezone(timedelta(hours=+8))
    now = datetime.now(tz)
    return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")
@app.route("/read")
def read():
    Result = ""     
    collection_ref = db.collection("人選之人─造浪者")    
    docs = collection_ref.order_by("name", direction=firestore.Query.DESCENDING).get()    
    for doc in docs:         
        Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
    return Result
@app.route("/books")
def books():
    Result = ""     
    collection_ref = db.collection("圖書精選")    
    docs = collection_ref.order_by("author", direction=firestore.Query.DESCENDING).get()    
    for doc in docs:         
        bk = doc.to_dict()
        Result += "書名:<a href=" +bk["url"] + ">" + bk ["title"] + "</a><br>"
        Result += "作者:" + bk["author"] + "<br>"
        Result += str(bk["anniversary"]) + "周年紀念版<br>"
        Result += "<img src=" + bk["cover"] + "> </img><br>"
    return Result
@app.route("/query", methods=["GET", "POST"])
def query():
    if request.method == "POST":
        keyword = request.form["keyword"]
        Result = "您輸入的書名是：" + keyword
  
        collection_ref = db.collection("圖書精選")    
        docs = collection_ref.get()    
        for doc in docs:         
            bk = doc.to_dict()
            if keyword in bk["title"]:
                Result += "書名:<a href=" +bk["url"] + ">" + bk ["title"] + "</a><br>"
                Result += "作者:" + bk["author"] + "<br>"
                Result += str(bk["anniversary"]) + "周年紀念版<br>"
                Result += "<img src=" + bk["cover"] + "> </img><br>"
        return Result
    else:
        return render_template("search.html")

if __name__ == "__main__": 
    app.run(debug=True)

from unittest import result
from flask import Flask 
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

app = Flask(__name__,static_folder="static",static_url_path="/")
app.secret_key="any string but secret"

#處理路徑 / 的對應函式
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["GET","POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]

    if account and password == "test":
        session["account"]= account
        return redirect("/member/")
    elif account =="" or password =="":
        result = "請輸入帳號、密碼"
        return redirect(url_for("error", message=result))
    else:
        result = "帳號、或密碼輸入錯誤"
        return redirect(url_for("error", message=result))


@app.route("/member/")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")



@app.route("/error")
def error():
    error=request.args.get("message", "")
    return render_template("fail.html", message=error)

@app.route("/signout")
def signout():
    session.clear()
    return redirect('/')



app.run(port=3000)
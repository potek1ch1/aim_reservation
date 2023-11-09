# #ここのエラーは気にしない
from flask import Flask, render_template, request, redirect, session  # , request, redirect, url_for,flash
from datetime import timedelta
import datetime
import uuid
import random

# from flask_sqlalchemy import SQLAlchemy
from config import Config
import pymysql
from models import User, Supplyment,Reservation, db
import json


app = Flask(__name__, static_folder="./static/")
# app.config["DEBUG"] = True
# mysqlの接続設定

# セッション情報
# #これは環境変数に入れる
app.secret_key = "AIM"
app.config["SESSION_COOKIE_NAME"] = "aim"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=50)

try:
    app.config.from_object(Config)
    db.init_app(app)
except:
    print("すでにあります．")

with app.app_context():
    db.create_all()
# with app.app_context():
#     if not db.engine.dialect.has_table(db.engine, 'your_table_name'):
#         db.create_all()


# def check_login():
#     if not session.get("student_id"):
#         return redirect("/session-expired")


@app.get("/database")
def getdata():
    # データの取得
    all = []
    users = User.query.all()
    for user in users:
        lis = [user.id, user.name, user.email, user.phone]
        all.append(lis)
    return all


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/")
def get_student_id():
    student_id = request.form.get("studentID")
    print(student_id)
    session["student_id"] = student_id
    return redirect("/register")


@app.get("/register")
def return_register():
    if not session.get("student_id"):
        return redirect("/session-expired")
    student_id = session.get("student_id")
    user = User.query.filter_by(id=student_id).first()
    if user:
        return redirect("/confirm")
    else:
        return render_template("register.html")


@app.post("/register")
def register():
    if not session.get("student_id"):
        return redirect("/session-expired")
    student_id = session.get("student_id")
    user_name = request.form.get("name")
    mail_address = request.form.get("mailAddress")
    phone_number = request.form.get("phoneNumber")
    new_user = User(student_id, user_name, mail_address, phone_number)
    print(student_id, user_name, mail_address, phone_number)

    db.session.add(new_user)
    db.session.commit()
    return redirect("/confirm")


# except:
#     print("すでに存在するデータ")
#     return "problem"


@app.get("/change")
def change():
    if not session.get("student_id"):
        return redirect("/session-expired")
    # ユーザーを特定
    # user = User.query.get(student_id)
    # ユーザー情報の変更
    return render_template("change_info.html")


@app.post("/change")
def update_info():
    student_id = session.get("student_id")
    if not student_id:
        return redirect("/session-expired")
    user = User.query.get(student_id)
    if user:
        mail_address = request.form.get("mailAddress")
        phone_number = request.form.get("phoneNumber")
        user.email = mail_address
        user.phone = phone_number
        try:
            db.session.commit()
        except:
            return "問題が発生した"
        return redirect("/confirm")


@app.get("/confirm")
def show_confirm():
    if not session.get("student_id"):
        return redirect("/session-expired")
    student_id = session.get("student_id")
    user = User.query.filter_by(id=student_id).first()
    user_info = {"id": user.id, "user": user.name, "mail": user.email, "phone": user.phone}
    session["user_name"] = user_info["user"]
    session["mail_address"] = user_info["mail"]
    session["phone_number"] = user_info["phone"]
    return render_template("confirm_user.html")


@app.get("/catalogs")
def show_supplyment():
    if not session.get("student_id"):
        return redirect("/session-expired")
    return render_template("catalogs.html")


@app.get("/supplyments")
def return_suuplyments():
    supplyment = {
        "supplyments": [
            {"id": "room00", "name": "静音ブース", "availableOutside": 0, "url": "seion.png"},
            {"id": "room01", "name": "編集ブース", "availableOutside": 0, "url": "hennsyuu.png"},
        ]
    }
    return json.dumps(supplyment)


@app.post("/search_by_date")
def search_by_date():
    req = request.get_json()
    print(req["startDate"])
    reservations = Reservation.query.filter_by(start_date=req["startDate"]).all()
    print(reservations)
    reservData = []
    for reservation in reservations:
        data = {"start": reservation.start_time, "return":reservation.return_time}
        reservData.append(data)
    return reservData


@app.post("/submit")
def receive_submit():
    req = request.get_json()
    for i in req:
        print(req[i])
    d_today = datetime.date.today()
    # reservation = Reservation(
    #     req["startDate"],
    #     req["startTime"],
    #     req["returnDate"],
    #     req["returnTime"],
    # )
    # u = uuid.uuid1()
    reservation_id = str(random.randrange(10000, 99999))
    print(reservation_id)
    new_reservation = Reservation(
        reservation_id,session.get("student_id"),
        req["supplymentId"],req["startDate"],
        req["startTime"],req["returnDate"],
        req["returnTime"],d_today
        )
    print(new_reservation)
    print(d_today)
    # new_user = User(student_id, user_name, mail_address, phone_number)
    # print(student_id, user_name, mail_address, phone_number)

    db.session.add(new_reservation)
    db.session.commit()

    print(d_today)
    return "OK"

@app.get("/session")
def get_session():

    return "ok"

@app.get("/complete")
def complete_reservation():
    return render_template("complete.html")


@app.get("/supplyment")
def supplyment_view():
    render_template("detail.html")


@app.get("/supplyment/<supplyment_id>")
def decide_supplyment(supplyment_id):
    # print(data)
    supplyment_data = Supplyment.query.filter_by(id=supplyment_id).first()
    print(supplyment_data.name)
    data = {
        "name": supplyment_data.name,
    }
    print(data)
    return render_template("detail.html", **data)


# #セッションが切れた時
@app.get("/session-expired")
def session_error():
    return render_template("session_expired.html")


@app.get("/apply")
def apply():
    return render_template("apply.html")


@app.get("/vue")
def vue():
    return render_template("vue.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)

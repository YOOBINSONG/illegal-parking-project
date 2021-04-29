from flask import Flask, render_template, request, redirect, url_for, abort
import dbtest
app=Flask(__name__)

dbtest.create_userinfo()
dbtest.create_carinfo()
dbtest.create_illigal_parking()

@app.route('/')
def front():
    return 'hello'

@app.route('/hello')
def hellohtml():
    return render_template("hello.html")

@app.route('/test')
def testhtml():
    return render_template("test.html")

@app.route('/method',methods=['GET','POST'])
def method():
    if request.method=='GET':
        usernum=request.args["usernum"]
        username=request.args.get("username")
        userid=request.args.get("userid")
        userpw=request.args.get("userpw")
        location=request.args.get("location")
        return "GET으로 전달된 데이터({},{},{},{},{})".format(usernum,username,userid,userpw,location)
    else:
        usernum=request.form["usernum"]
        username=request.form["username"]
        userid=request.form["userid"]
        userpw=request.form["userpw"]
        location=request.form["location"]
        dbtest.insert_userinfo(usernum,username,userid,userpw,location)
        return "POST로 전달된 데이터 {},{},{},{},{}".format(usernum,username,userid,userpw,location)

@app.route('/method2',methods=['GET','POST'])
def method2():
    if request.method=='GET':
        illigal_num=request.args["illigal_num"]
        carnum=request.args.get("carnum")
        illigal_time=request.args.get("illigal_time")
        cctvname=request.args.get("cctvname")
        return "GET으로 전달된 데이터({},{},{},{})".format(illigal_num,carnum,illigal_time,cctvname)
    else:
        illigal_num=request.form["illigal_num"]
        carnum=request.form["carnum"]
        illigal_time=request.form["illigal_time"]
        cctvname=request.form["cctvname"]
        dbtest.insert_illigal_info(illigal_num,carnum,illigal_time,cctvname)
        return "POST로 전달된 데이터 {},{},{},{}".format(illigal_num,carnum,illigal_time,cctvname)



@app.route('/getinfo')
def getinfo():
    info=dbtest.select_all_user()
    return render_template("info.html",data=info)
app.run(host='0.0.0.0', port=9900)
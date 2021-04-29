import sqlite3

def dbcon():
    return sqlite3.connect('parking.db')


def create_carinfo():
    try:
        db=dbcon()
        c=db.cursor()
        c.execute("CREATE TABLE carinfo (carnum	TEXT, phonenum INTEGER, PRIMARY KEY(carnum))")
        db.commit()
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()
        
def create_userinfo():
    try:
        db=dbcon()
        c=db.cursor()
        c.execute("CREATE TABLE userinfo (usernum TEXT, username TEXT, userid TEXT, userpw TEXT, location TEXT, PRIMARY KEY(usernum))")
        db.commit()
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()

def create_illigal_parking():
    try:
        db=dbcon()
        c=db.cursor()
        c.execute("CREATE TABLE illigal_parking (illigal_num INTEGER, carnum TEXT, illigal_time TEXT, cctvname text, FOREIGN KEY (carnum) REFERENCES carinfo(carnum), PRIMARY KEY (illigal_num) )")
        db.commit()
    except Exception as e:
        print ('db error:', e)
    finally:
        db.close()

def insert_carinfo(carnum,phonenum):
    try:
        db=dbcon()
        c=db.cursor()
        setdata=(carNum,phoneNum)
        c.execute("INSERT INTO carinfo VALUES (?,?)",setdata)
        db.commit()
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()

def insert_userinfo(usernum,username,userid,userpw,location):
    try:
        db=dbcon()
        c=db.cursor()
        setdata=(usernum,username,userid,userpw,location)
        c.execute("INSERT INTO userinfo VALUES (?,?,?,?,?)",setdata)
        db.commit()
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()

def insert_illigal_info(illigal_num,carNum,illigal_time,cctvname):
    try:
        db=dbcon()
        c=db.cursor()
        setdata=(illigal_num,carNum,illigal_time,cctvname)
        c.execute("INSERT INTO illigal_parking VALUES (?,?,?,?)",setdata)
        db.commit()
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()

def select_all_illigal_info():
    ret=list()
    try:
        db=dbcon()
        c=db.cursor()
        c.execute("SELECT * FROM illigal_parking")
        ret=c.fetchall()
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()
        return ret

def select_all_user():
    ret=list()
    try:
        db=dbcon()
        c=db.cursor()
        c.execute("SELECT * FROM userinfo")
        ret=c.fetchall()
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()
        return ret

def select_all_carinfo():
    ret=list()
    try:
        db=dbcon()
        c=db.cursor()
        c.execute("SELECT * FROM carinfo")
        ret=c.fetchall()
    except Exception as e:
        print('db error:',e)
    finally:
        db.close()
        return ret